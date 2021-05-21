from PIL import Image, ImageFilter

img = Image.open('/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save("/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/grey.png", 'png')