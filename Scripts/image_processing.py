from PIL import Image, ImageFilter


img = Image.open('./Pictures/pikachu.jpg')
filter_img = img.filter(ImageFilter.BLUR)
filter_img.save("./Pictures/blur.png", "png")

filter_img = img.filter(ImageFilter.SMOOTH)
filter_img.save("./Pictures/smooth.png", "png")

filter_img = img.filter(ImageFilter.SHARPEN)
filter_img.save("./Pictures/sharp.png", "png")

filter_img = img.convert('L')  # black&white
filter_img.save("./Pictures/gray.png", "png")
# filter_img.show()
filter_img = filter_img.rotate(180)
# filter_img.show()
resize = filter_img.resize((300, 300))
# resize.show()
box = (100, 100, 400, 400)
crop = filter_img.crop(box)
# crop.show()


img = Image.open("./Pictures/astro.jpg")
img.thumbnail((400, 400))
img.save('./Pictures/thumbnail.jpg')
img.show()

# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))

