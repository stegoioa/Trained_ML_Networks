#Preprocessing Many Images
#First, we create all the necessary functions

import imageio
import glob
from tqdm import tqdm
from PIL import Image
import os
        
def crop_square(image):        
    width, height = image.size
    
    # Crop the image, centered
    new_width = min(width,height)
    new_height = new_width
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    return image.crop((left, top, right, bottom))

def scale(img, scale_width, scale_height):
    # Scale the image
    img = img.resize((
        scale_width, 
        scale_height), 
        Image.ANTIALIAS)
            
    return img

def standardize(image):
    rgbimg = Image.new("RGB", image.size)
    rgbimg.paste(image)
    return rgbimg

def fail_below(image, check_width, check_height):
    width, height = image.size
    assert width == check_width
    assert height == check_height

from google.colab import drive
drive.mount('/content/drive')

#Next, we loop through each image. The images are loaded, and you can apply any desired transformations. Ultimately, the script saves the images as JPG.

SOURCE = "/path"
TARGET = "/path"

files = glob.glob(os.path.join(SOURCE,"*.jpg"))

for file in tqdm(files):
    try:
        target = ""
        name = os.path.basename(file)
        filename, _ = os.path.splitext(name)
        img = Image.open(file)
        img = standardize(img)
        img = crop_square(img)
        img = scale(img, 512, 512)
        #fail_below(img, 1024, 1024)

        target = os.path.join(TARGET,filename+".jpg")
        img.save(target, quality=25)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        break
    except AssertionError:
        print("Assertion")
        break
    except:
        print("Unexpected exception while processing image source: " \
              f"{file}, target: {target}" , exc_info=True)

SOURCE = "/content/drive/MyDrive/projects/paradigm_park/pix2pixhd_dataset/satellite"
TARGET = "/content/drive/MyDrive/projects/paradigm_park/pix2pixhd_dataset/final_training_sets/train_B"

files = glob.glob(os.path.join(SOURCE,"*.png"))

for file in tqdm(files):
    try:
        target = ""
        name = os.path.basename(file)
        filename, _ = os.path.splitext(name)
        img = Image.open(file)
        img = standardize(img)
        img = crop_square(img)
        img = scale(img, 1024, 1024)
        #fail_below(img, 1024, 1024)

        target = os.path.join(TARGET,filename+".jpg")
        img.save(target, quality=25)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        break
    except AssertionError:
        print("Assertion")
        break
    except:
        print("Unexpected exception while processing image source: " \
              f"{file}, target: {target}" , exc_info=True)

#Zip the preprocessed files and store them somewhere.

