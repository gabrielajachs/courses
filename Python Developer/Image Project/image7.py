#converting JPG to PNG
import sys
import os
from PIL import Image

#grab the first and second argument
path = sys.argv[1]
directory = sys.argv[2]


#check if newfolder/ exists, if not
#create it
if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
#loop through Pokedex
#convert images to png
#save to the new folder