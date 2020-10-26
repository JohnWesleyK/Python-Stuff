# pip install pillow

# How to open images

from PIL import Image

mac = Image.open('example.jpg')
# print(type(mac))
# mac.show()  # you can see the image
# print(mac.size) # you can see the size of the image
# print(mac.filename) # you can see the filename with this
# print(mac.format_description) # specific description

'''
Cropping
img.crop((x, y, width, height))
x,w in same direction
y,h in same direction
crop = mac.crop((0,0,100,100))
crop.show()
'''

# pencils = Image.open('pencils.jpg')
# pencils.show()
# print(pencils.size)  # 1950, 1300
# x, y = 0, 1100
# w = 1950 / 3
# h = 1300
# pencil_crop = pencils.crop((x, y, w, h))
# pencil_crop.show()

# # mac.show()
# # print(mac.size) # 1993, 1257
# halfway_horizontal = 1993/2
#
# x = halfway_horizontal - 200
# w = halfway_horizontal + 200
#
# y = 800
# h = 1257
# mac_crop = mac.crop((x,y,w,h))
# mac_crop.show()

'''
Copying images
img.paste(im=img_name, box=(x,y))
'''

halfway_horizontal = 1993 / 2
halfway_vertical = 1257 / 2

x = halfway_horizontal - 200
w = halfway_horizontal + 200

y = 800
h = 1257

mac_crop = mac.crop((x, y, w, h))
# print(mac_crop.size) # 400, 457
# mac.paste(im=mac_crop, box=(0, 0))
#
# mac.paste(im=mac_crop, box=(400, 0))
# mac.paste(im=mac_crop, box=(800, 0))
# mac.paste(im=mac_crop, box=(1200, 0))
# mac.paste(im=mac_crop, box=(1600, 0))
#
# mac.paste(im=mac_crop, box=(800, 457))
#
# mac.show()

'''
Re-sizing Images
img.resize(new_width, new_height)
'''
# mac_resized = mac.resize((3000,500))
# mac_resized.show()

'''
Color Transparency
RGBA - Red, Green, Blue, Alpha

Re-Setting Alpha:
img.putalpha(number) 0 <= number <= 255

img1.paste(im=img2, box=(0, 0), mask=img2)
'''
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
purple = Image.open('purple.png')

# Re-Setting Alpha
red.putalpha(208)
# red.show()
purple.putalpha(208)
# purple.show()

red.paste(im=purple, box=(0, 0), mask=purple)
red.show()

'''
Saving Images
img.save("Path")
'''
red.save("mixed_color.png")
