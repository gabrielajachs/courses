from PIL import Image, ImageFilter

img = Image.open('/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/Pokedex/astro.jpg')
img.thumbnail((400, 400))
img.save("/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/resize_astro2.jpg")

print(img.size)