import shutil
import time
import os
import optparse
import errno
import site
import pip
import logging
import imp
os.system('py -2 -m pip install --upgrade pip')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print ("BeautifulSoup lib not found!")
    import pip
    cmd = 'py -2 -m pip install BeautifulSoup4'
    print ("Please enter the root password to install the required package!")
    os.system(cmd)
    imp.reload(site)
try:
    import requests
except ImportError:
    print ("Requests lib not found!")
    import pip
    cmd = 'py -2 -m pip install requests'
    print ("Please enter the root password to install the required package!")
    os.system(cmd)
    imp.reload(site)
try:
    import urllib2
except ImportError:
    print ("urllib2 lib not found!")
    import pip
    cmd = 'py -2 -m pip install urllib2'
    print ("Please enter the root password to install the required package!")
    os.system(cmd)
    imp.reload(site)
try:
    from urlparse import urljoin
except ImportError:
    print ("urlparse lib not found!")
    import pip
    cmd = 'py -2 -m pip install urlparse'
    print ("Please enter the root password to install the required package!")
    os.system(cmd)
    imp.reload(site)

def b_soup(url):
    req = urllib2.Request(url, headers={'User-Agent' : "Browser"})
    html = urllib2.urlopen(req)
    return BeautifulSoup(html, 'html.parser')

def download_images(url, dir):
    counter = 0
    soup = b_soup(url)
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + " images found.")
    print ("Downloading images in specified destination directory.")
    image_links = [each.get('src') for each in images]
    for each in image_links:
        counter = counter + 1
        try:
            filename = each.strip().split('/')[-1].strip()
            filename = os.path.join(dir,\
                                    filename.replace('/', '_'))
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:
                    if exc.errno != errno.EExist:
                        raise
            print ("[+] Saving " + str(filename))
            src = urljoin(url, each)
            print ("Getting: " + filename)
            response = requests.get(src, stream=True)
            path = str(dir + '\Img.txt')
            fd = open(path, 'a')
            fd.write(str(counter) + '.' + str(src) + '\n\n' )
            # delay to avoid corrupted previews
            time.sleep(1)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            print ("An error occured. Continuing.")
        print ("Done.")
    out_file.close()
    fd.close()

def main():
    parser = optparse.OptionParser('usage %prog ' + \
                                   '-u <target url> -d <destination directory>')

    parser.add_option('-u', dest='tgtURL', type='string', \
                      help='specify target url')
    parser.add_option('-d', dest='dir', type='string', \
                      help='specify destination directory')

    (options, args) = parser.parse_args()

    url = options.tgtURL
    dir = options.dir

    if url == None or dir == None:
        print (parser.usage)
        exit(0)

    else:
        try:
            if os.path.exists(dir + '\Img.txt'):
                os.remove(dir + '\Img.txt')
            download_images(url, dir)
        except Exception as e:
            print ("[-] Error Downloading Images.")
            print ("[-] " + str(e))

if __name__ == '__main__':
    main()
