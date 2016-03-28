from PIL import Image

#putting all photos into an array

filename = ".jpg"
imArray = [""]

#counter for photos
    #Each image is a number from 1-57
photoNumCount = 1
for i in range (0, 56):
    #Changes the int photoNumCount to a string
    imNum2 = str(photoNumCount)
    #Appends the string number to ".jpg" to create the full filename
    filename2 = imNum2 + filename
    imArray.append(Image.open(filename2))
    photoNumCount +=1


#calling random photos from array and compressing them to be 400x400
num = imArray[36]
##num.show()
num = num.resize((160, 90), Image.ANTIALIAS)
num.show()


##filename = "1.jpg"
