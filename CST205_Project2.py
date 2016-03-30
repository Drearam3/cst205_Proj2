
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
        actual_name = None
    return actual_name, closest_name
   
#----------------------------------------------------------------------------


#-------------------------------------Mosaic----------------------------------

def create_mosaic(original_picture, file):

    
    #path to folder with the tile images
    path = os.path.dirname(file) + "/"

    #width and height that image to be mosaicked will be resized to

    tile_height = 8
    tile_width = 8
    tiles = 9
    actual = [""]
    close = [""]
    my_actual = actual
    my_close = close

    print(file)
            

    #resizing of "original picture" <- picture to be mosaicked
    basewidth = 200
    original_picture = Image.open(file)
    wpercent = (basewidth/float(original_picture.size[0]))
    hsize = int((float(original_picture.size[1])*float(wpercent)))
    original_picture = original_picture.resize((basewidth,hsize), Image.ANTIALIAS)
    original_picture.save('Original.jpg')
    
    org_width, org_height = original_picture.size

    
    #width and height of actual mosaic
    output_size = ((org_width * tile_width), (org_height * tile_height))

    #creation of empty image that tile pictures will be pasted onto
    mosaic = Image.new('RGB', output_size)

    
##----------------------------------Puts tile colors into array-------------------------------------------------------------
            #Big Loop that goes through each of the tile images individually and resizes them
        # a width of 16 pixels and a height of 16 pixels
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

            
                 
                r_avg = (r + r_avg) / 2
                g_avg = (g + g_avg) / 2
                b_avg = (b + b_avg) / 2

        r_avg = int(r_avg)
        g_avg = int(g_avg)
        b_avg = int(b_avg)
        tile_color_to_match = (r_avg, g_avg, b_avg)

        tile_actual_name, tile_closest_name = get_colour_name(tile_color_to_match)
        if( 125 < r_avg < 255 and 0 < g_avg < 160 and 0 < b_avg < 150):
            tile_actual_name = "Red";
        elif( 0 < r_avg < 160 and 125 < g_avg < 255 and 0 < b_avg < 150):
            tile_actual_name = "Blue";
        elif( 140 < r_avg < 255 and 140 < g_avg < 255 and 20 < b_avg < 200):
            tile_actual_name = "Yellow";
        elif( 100 < r_avg < 255 and 50 < g_avg < 200 and 0 < b_avg < 140):
            tile_actual_name = "Orange";
        elif( 0 < r_avg < 160 and 0 < g_avg < 160 and 125 < b_avg < 255):
            tile_actual_name = "Green";
        elif( 170 < r_avg < 255 and 170 < g_avg < 255 and 170 < b_avg < 255):
            tile_actual_name = "White";
 

        my_actual.append(tile_actual_name)
        my_close.append(tile_closest_name)
##-------------------------------------------------------------------------------------------------------------------------------
##---------------------------Finds colors of each pixel in big pic and finds match in tile list----------------------------------

##    for width in range(0, 100):
    for height in range(0, org_height):
##        for height in range (0, 75):
        for width in range(0, org_width):
            pixel = (width, height)
            R, G, B = original_picture.getpixel(pixel)
            
            org_color_to_match = (R, G, B)
            org_actual_name, org_closest_name = get_colour_name(org_color_to_match)


##-------------------------------------------------------------------------------------------------------------------------------

##------------------------------------------
        #CODE GOES HERE
##------------------------------------------
            for i in range (0, tiles):

                if (org_closest_name == my_close[i]):
                    tile_filename = path + str(i) + ".jpg"
                    mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                    print(height, width)
                    break
                elif( 120 < R < 255 and 0 < G < 160 and 0 < B < 160):
                    org_actual_name = "Red";
                    if(org_actual_name == my_actual[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        break
                elif( 0 < R < 160 and 120 < G < 255 and 0 < B < 160):
                    org_actual_name = "Blue";
                    if(org_actual_name == my_actual[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        break
                elif( 130 < R < 255 and 130 < G < 255 and 0 < B < 200):
                    org_actual_name = "Yellow";
                    if(org_actual_name == my_actual[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        break
                elif( 100 < R < 255 and 50 < G < 200 and 0 < B < 140):
                    org_actual_name = "Orange";
                    if(org_actual_name == my_actual[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        break
                elif( 0 < R < 160 and 0 < G < 160 and 120 < B < 255):
                    org_actual_name = "Green";
                    if(org_actual_name == my_actual[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        break
                elif( 0 < R < 255 and 0 < G < 255 and 0 < B < 255):
                    org_actual_name = "White";
                    if(org_actual_name == my_actual[i]):
                        tile_filename = path + str(i) + ".jpg"
                        mosaic.paste(Image.open(tile_filename), ((width * tile_width), (height * tile_height)))
                        print(height, width)
                        break
                
                
    mosaic.save("output.jpg")
    mosaic.show()
###-------------------------------------MAIN----------------------------------------------

file = fd.askopenfile()
filename = str(file.name)
print(filename)
original_image = Image.open(filename)
create_mosaic(original_image, filename)


