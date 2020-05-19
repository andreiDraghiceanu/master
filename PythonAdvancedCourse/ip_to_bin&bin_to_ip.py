# ip = '192.168.1.1'
ip = '255.14.253.218'
# print('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]))

bin = [128, 64, 32, 16, 8, 4, 2, 1]



def ip_to_bin(ip):
    final = ""
    for x in ip.split('.'):
        val = int(x)
        for a in bin:
            if val >= a:
                final = final + '1'
                val = val - a
            else:
                final = final + '0'
        final = final + '.'
    final = final[:-1]
    return final

print(ip_to_bin(ip))


def bin_to_ip(final):
    blocks = list(final.split("."))
    dec_blocks = ""
    for block in blocks:
        dec_block = 0
        for x, i in zip(block, bin):
            if int(x) == 1:
                dec_block = dec_block + i
        dec_blocks = dec_blocks + str(dec_block) + "."
    dec_blocks = dec_blocks[:-1]
    return dec_blocks

print(bin_to_ip(ip_to_bin(ip)))