import sys
import os
import os.path

from PIL import Image
from PIL.ExifTags import TAGS

extentions = [".jpg", ".jpeg", ".gif", ".bmp", ".png"]


def extract(filename):

  # Path to the image
  imagename2 = filename

  # read the image data using PIL
  image = Image.open(imagename2)
  image.load()

  # Extract basic metadata
  info_dict = {
      "Filename": image.filename,
      "Image Size": image.size,
      "Image Height": image.height,
      "Image Width": image.width,
      "Image Format": image.format,
      "Image Mode": image.mode,
      "Image is Animated": getattr(image, "is_animated", False),
      "Frames in Image": getattr(image, "n_frames", 1)
  }

  print()
  print("--- Basic Meta Data:")
  print()

  for label,value in info_dict.items():
    if label == 'Filename':
      continue
    print(f"{label:25}: {value}")
  print()

  # Extract EXIF data
  for k, v in info_dict.items():
    if k == 'Image Format':
      real_format = v
      if real_format == 'JPEG' or real_format == 'jpeg' or real_format == 'JPG' or real_format == 'jpg':
        exifdata = image.getexif()
        if info_dict.items():
          print("--- Exif Meta Data:")
          print()
        tag = {}
        data = 0
        for tag_id in exifdata:
          # Get the tag name, instead of human unreadable tag id
          tag = TAGS.get(tag_id, tag_id)
          data = exifdata.get(tag_id)

          print(f"{tag:25} : {data}")
          # decode bytes 
          if isinstance(data, bytes):
            data = data.decode()
        print()


# Main Function
if __name__ == "__main__":
  n = len(sys.argv)
  names = []
  if n > 2:
    for i, arg in enumerate(sys.argv):
      names.append(sys.argv[i])
    del names[0]
    for n in names:
        # Check if file exists
        check_file = os.path.isfile(n)
        if check_file is False:
          print('No such file. Please provide the name of an existing file\n')
          break
        # Get Extention
        extention = os.path.splitext(n)[1]
        print(f"------ FILE: {n} ")
        if extention not in extentions:
          print('Wrong File Format: Accepted files are .jpg, .jpeg, .gif, .png, .bmp\n')
          break
        extract(n)
  elif n == 2:
    # Check if file exists
    check_file = os.path.isfile(sys.argv[1])
    if check_file is False:
        print('No such file. Please provide the name of an existing file\n')
        exit()
    # Get Extention
    extention = os.path.splitext(sys.argv[1])[1]
    print(f"------ FILE: {sys.argv[1]} ")
    if extention not in extentions:
      print('Wrong File Format: Accepted files are .jpg, .jpeg, .gif, .png, .bmp\n')
      exit()
    extract(sys.argv[1])
  else:
    print('Missing Argument. Please provide at least one filename.')
  

