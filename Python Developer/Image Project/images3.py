from PIL import Image, ImageFilter

img = Image.open('/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
resize = filtered_img.resize((300, 300))
resize.save("/home/gabrielajachs/Documents/GitHub/courses/Python Developer/image-playground/resize.png", 'png')
