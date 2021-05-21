from PIL import Image, ImageFilter

img = Image.open('/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/Pokedex/astro.jpg')
new_img = img.resize((400, 400))
new_img.save("/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/resize_astro.jpg")
