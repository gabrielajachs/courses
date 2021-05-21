from PIL import Image, ImageFilter

img = Image.open('/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
crooked = filtered_img.rotate(180)
crooked.save("/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/rotate.png", 'png')
