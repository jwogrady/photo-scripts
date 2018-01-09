import os
import sys
""" 
Renames the filenames within the same directory to be Unix friendly
(1) Changes spaces to hyphens
(2) Makes lowercase (not a Unix requirement, just looks better ;)
Usage:
python rename.py
"""

dr = os.path.dirname(os.path.realpath(sys.argv[0]))

for subdir, dirs, files in os.walk(dr):
    for filename in files:
        subdirectoryPath = os.path.relpath(subdir, dr) #get the path to your subdirectory
        filePath = os.path.join(subdirectoryPath, filename) #get the path to your file
        print(filePath)
        print(filename)

        n = filePath.replace(' ', '-')
        n = n.replace('/', "-")
        n = n.replace('_', '-')
        n = n.lower()

        newFilePath = filePath.replace(filename, n) #create the new name

        print(newFilePath)
        print(n)

        os.rename(filePath, newFilePath)
    
# flatten directory struction
# mv ./*/**/*(.D) . 

# resize image
# magick mogrify -resize 1080 *.jpg
