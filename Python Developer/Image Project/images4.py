from PIL import Image, ImageFilter

img = Image.open('/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/crop.png", 'png')
