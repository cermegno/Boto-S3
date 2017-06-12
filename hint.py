import os
for each_photo in os.listdir("photos"):
    print "Uploading " + str(each_photo)
    src = os.path.join("photos", each_photo)
    print "full path to photo is : " + src
## Alterntively walk recursively a dir tree. It creates a string and 2 lists
##
##for (dirpath, dirnames, filenames) in os.walk("photos"):

