##-----------------------PROJECT2---------------------------------------------
##  Names: Andrea Ramirez, Diego Medina, Raeleen Watson, Cameron Morefield
##  Due Date: 04/01/16
##  Title: CST205_Project2.py





from PIL import Image
from tkinter import filedialog as fd
import webcolors
import os


#---------------BORROWED-------------------------------------------


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = 'NoColor'
    return actual_name, closest_name

def closest_to_general(color_name):
    red = ['crimson', 'firebrick', 'indianred', 'darkorange', 'orangered', 'salmon', 'tomato', 'red','scarlet', 'freespeechred', 'maroon']

    orange = ['orangered', 'chocolate', 'darkorange', 'coral', 'orange', 'mandarinorange']

    yellow = ['darkgoldenrod', 'goldenrod', 'yellow', 'gold']

    lightYellow = ['goldenrod', 'sandybrown', 'moccasin', 'lemonchiffon', 'beige']

    green = ['darkgreen', 'darkgreencopper', 'darkolivegreen', 'olive', 'forestgreen', 'olivedrab', 'seagreen', 'green']

    lightGreen = ['darkseagreen', 'greenyellow', 'lawngreen', 'lightseagreen', 'limegreen', 'mediumseagreen', 'mediumspringgreen',
                    'palegreen', 'springgreen', 'yellowgreen', 'chartreuse', 'lime', 'freespeechgreen']
    
    blue = ['cadetblue', 'darkslateblue', 'mediumblue', 'mediumslateblue', 'midnightblue','navyblue', 'royalblue',
            'blue', 'blue1','blue2', 'blue3', 'blue4', 'navy', 'darkslategray', 'darkslategrey', 'darkturquoise',
            'midnightblue', 'navyblue', 'neonblue', 'newmidnightblue', 'freespeechblue']

    lightBlue = ['cornflowerblue', 'darkturquoise',  'deepskyblue','dodgerblue', 'lightblue', 'lightskyblue', 'aquamarine',
                    'mediumturquoise', 'skyblue', 'steelblue', 'mediumaquamarine', 'aqua', 'trueirisblue', 'cyan', 'teal', 'turquoise',
                    'summersky', 'irisblue','skyblue', 'darkcyan', 'lightgrey']

    violet = ['blueViolet', 'slateblue', 'mediumslateblue','darkorchid', 'darkviolet', 'purple', 'violetblue', 'darkpurple', 'darkslateblue', 'indigo']

    lightViolet = ['slateBlue', 'richBlue', 'mediumorchid', 'mediumpurple', 'plum', 'violet','slateblue']

    pink = ['pink', 'deeppink', 'hotpink', 'mediumvioletred','lightpink', 'palevioletred', 'violetred', 'spicypink', 'freespeechmagenta',
            'darksalmon', 'lightcoral', 'magenta', 'fushia', 'neonpink']

    lightPink = ['orchid']

    brown = ['dustyrose', 'rosybrown', 'saddlebrown', 'sandybrown', 'brown', 'darkbrown', 'darktan', 'darkwood', 'lightwood',
                'mediumwood', 'semi-sweetchocolate', 'sienna', 'verydarkbrown', 'darkolivegreen']

    tan = ['burlywood', 'peru', 'tan', 'newtan', 'khaki', 'lightsalmon', 'peachpuff', 'lightgoldenrod', 'mediumgoldenrod']

    
    white = ['azure', 'linen', 'blanchedalmond', 'seashell', 'lightgoldenrodyellow', 'ghostwhite', 'oldlace', 'bisque', 'mistyrose',
            'cornsilk', 'antiquewhite', 'floralwhite','silver', 'aliceblue', 'snow', 'lavender', 'mintcream', 'whitesmoke', 'gainsboro',
            'lightgrey', 'ivory','wheat', 'honeydew','lavenderblush', 'lightyellow', 'papayawhip', 'lightcyan', 'lightsteelBlue',
            'paleturquoise','powderblue', 'thistle', 'palegoldenrod', 'lightcyan', 'lightsteelblue', 'lightgray']
    
    gray = ['grey', 'gray', 'darkgrey', 'lightslategrey', 'lightslategray', 'dimgray', 'dimgrey'] 

    if(color_name in red):
        color_name = 'red'
    elif(color_name in orange):
        color_name = 'orange'
    elif(color_name in yellow):
        color_name = 'yellow'
    elif(color_name in lightYellow):
        color_name = 'lightyellow'
    elif(color_name in green):
        color_name = 'green'
    elif(color_name in lightGreen):
        color_name = 'lightgreen'
    elif(color_name in blue):
        color_name = 'blue'
    elif(color_name in lightBlue):
        color_name = 'lightblue'
    elif(color_name in violet):
        color_name = 'violet'
    elif(color_name in lightViolet):
        color_name = 'lightviolet'
    elif(color_name in pink):
        color_name = 'pink'
    elif(color_name in lightPink):
        color_name = 'lightpink'
    elif(color_name in brown):
        color_name = 'brown'
    elif(color_name in tan):
        color_name = 'tan'
    elif(color_name in white):
        color_name = 'white'
    elif(color_name in gray):
        color_name = 'gray'

    return color_name


   
#----------------------------------------------------------------------------


#-------------------------------------Mosaic----------------------------------

def create_mosaic(original_picture, file):

    
    #path to folder with the tile images
    #Gets path based on the location of the original image
        ##original image must be in the same folder as the tiles
    path = os.path.dirname(file) + "/"

    #width and height that image to be mosaicked will be resized to
    tile_height = 8
    tile_width = 8
    ##Number of tile images
    tiles = 83
    ##Lists to put color names into
    actual = [""]
    close = [""]
    my_actual = actual
    my_close = close

    print(file)
            

    #resizing of "original picture" <- picture to be mosaicked
    ##The width of the original image is sized down to at least 200px
        ##The height is scaled based on the width
    basewidth = 100
    original_picture = Image.open(file)
    ##calculations for resizing image while keeping ratio
    wpercent = (basewidth/float(original_picture.size[0]))
    hsize = int((float(original_picture.size[1])*float(wpercent)))
    original_picture = original_picture.resize((basewidth,hsize), Image.ANTIALIAS)
    ##Saves the newly resized image as 'Original.jpg'
    original_picture.save('Original.jpg')

    ##Getting height and width of scaled image
    org_width, org_height = original_picture.size

    
    #calculates width and height of actual mosaic by
        ##multiplying dimensions of tile pics and original pic
    output_size = ((org_width * tile_width), (org_height * tile_height))

    #creation of empty image that tile pictures will be pasted onto
    mosaic = Image.new('RGB', output_size)

    
##----------------------------------Puts tile colors into array-------------------------------------------------------------
    #Big Loop that goes through each of the tile images individually and resizes them
    # a width of 8 pixels and a height of 8 pixels
    for i in range (0, tiles): #number changes depending on how many images there are
        
        #all images have to be .jpg
        tile_filename = ".jpg"
        
        #Changes the current number to a string to be appended to the filename
        file_Num = str(i+1)
        
        #Appends the folder path, string number, and ".jpg" to create the full filename
        tile_filename = path + file_Num + tile_filename
        
        tile_image = Image.open(tile_filename) #opens tile image
        tile_image = tile_image.resize((tile_width, tile_height), Image.ANTIALIAS) #Change image size based on big pic
        tile_image.save(tile_filename, tile_image.format)
        tile_image = Image.open(tile_filename)
        r_avg = 0
        g_avg = 0
        b_avg = 0

        for x in range(0, tile_width): 
            for y in range(0, tile_height): #Resets the pixel list
                xy = (x,y)
                r, g, b= tile_image.getpixel(xy)

                
                ##Gets the average red, blue, and green color for each pixel in tiles
                r_avg = (r + r_avg) / 2
                g_avg = (g + g_avg) / 2
                b_avg = (b + b_avg) / 2

        ##changes values into integers
        r_avg = int(r_avg)
        g_avg = int(g_avg)
        b_avg = int(b_avg)
        ##puts the three values togethe
        tile_color_to_match = (r_avg, g_avg, b_avg)

        ##Gets the name of the tile.
            ##Gets specific name and general name
        tile_actual_name, tile_closest_name = get_colour_name(tile_color_to_match)
                    ##if no general name can be found, it is assigned a name based off its value

        tile_actual_name = closest_to_general(tile_closest_name)


        ##Puts the color names in respective lists
        my_actual.append(tile_actual_name)
        my_close.append(tile_closest_name)
##-------------------------------------------------------------------------------------------------------------------------------
##---------------------------Finds colors of each pixel in big pic and finds match in tile list----------------------------------
##    for width in range
    for height in range(0, org_height):
        for width in range(0, org_width):
            pixel = (width, height)
            #Gets the red, blue and green from each pixel in orginal image
            R, G, B = original_picture.getpixel(pixel)
            
            org_color_to_match = (R, G, B)
            org_actual_name, org_closest_name = get_colour_name(org_color_to_match)
            org_actual_name = closest_to_general(org_closest_name)



                ##if the original pixel does not have a match in the specific name list,
                    ## it is given a general name and looks through the list with the general names of tile colors.
            if(org_closest_name in my_close):
                for i in range (0, tiles):
                    if (org_closest_name == my_close[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        i = tiles - 1
                        break
            if(org_actual_name in my_actual):
                for i in range (0, tiles):
                    if (org_actual_name == my_actual[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        i = tiles - 1
                        break
##file = fd.askopenfile()
##filename = str(file.name)
##original_image = Image.open(filename)
##create_mosaic(original_image, filename)


                    
           
            
    mosaic.save("output.jpg")
    mosaic.show()
###-------------------------------------MAIN----------------------------------------------

##Beginning of file. 


#Asks the user to select a file.
    ##FILE SELECTED MUST BE IN THE FOLDER THAT THE TILES ARE IN. 

def runProgram(event):
    file = fd.askopenfile()
    filename = str(file.name)
    original_image = Image.open(filename)
    create_mosaic(original_image, filename)

###-------------------------------------MAIN----------------------------------------------



###-------------------------------------GUI----------------------------------------------
#main window
root = fd.Tk()
root.configure(background = "black")


########### FRAME

#top frame 
topFrame = fd.Frame(root)
topFrame.configure(background = "black")
topFrame.pack()
#bottom frame
bottomFrame = fd.Frame(root)
bottomFrame.pack()




########### PHOTOS

#creates a photo object
csumbPhoto = fd.PhotoImage(file = "csumbLogo.png")
mozaicWordPhoto = fd.PhotoImage(file = "mozaicGroupTxt.png")

#label with the photo object
csumbLabel = fd.Label(topFrame, image = csumbPhoto)
csumbLabel.pack()

mozaicWordLabel = fd.Label(topFrame, image = mozaicWordPhoto)
mozaicWordLabel.configure(background = "black")
mozaicWordLabel.pack()





############ BUTTON

#mozaic button to compile
mozaicButton = fd.Button(bottomFrame, width = 60, height = 5, text = "Press To Begin", fg = "navy", bg = "white", )
mozaicButton.bind("<Button-1>",runProgram)
mozaicButton.pack()


##
###infinite loop so the window will continue to display
##root.mainloop()
