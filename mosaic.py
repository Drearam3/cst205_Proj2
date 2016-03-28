
from PIL import Image
import webcolors


#-----------------------------------------------------------------------------

#putting all photos into an array

#-----------------------------------------------------------------------------
r_avg = 0
g_avg = 0
b_avg = 0

colorvalue = [""]

def rgb_to_hex(r,g,b):
    return '#%02x%02x%02x' % (int(r),int(g),int(b))

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
        actual_name = "None"
    return actual_name, closest_name



for i in range (0, 109): #number changes depending on how many images there are

    hX = ""
    path = "/Users/Drea/Desktop/Proj2/cst205_Proj2/"
        
    #all images have to be .jpg
    tile_filename = ".jpg"
    
    #Changes the current number to a string to be appended to the filename
    file_Num = str(i+1)
    
    #Appends the folder path, string number, and ".jpg" to create the full filename
    tile_filename = path + file_Num + tile_filename
    
    tile_image = Image.open(tile_filename) #opens tile image
    tile_image = tile_image.resize((16, 16), Image.ANTIALIAS) #Change image size based on big pic
    tile_image.save(tile_filename, tile_image.format)

    tile_image = Image.open(tile_filename)

    for x in range(0, 16): 
        for y in range(0, 16): #Resets the pixel list
            xy = (x,y)
            r, g, b= tile_image.getpixel(xy)

        
             
            r_avg = (r + r_avg) / 2
            g_avg = (g + g_avg) / 2
            b_avg = (b + b_avg) / 2

    r_avg = int(r_avg)
    g_avg = int(g_avg)
    b_avg = int(b_avg)
    hX = rgb_to_hex(r_avg, g_avg, b_avg)
    color = (r_avg, g_avg, b_avg)
    actual, close = get_colour_name(color)
    
##    print(tile_filename)
##    print(r_avg, g_avg, b_avg)
##    print(actual)
##    print(close)

color = (239, 255, 246)
color2 = (255, 255, 255)
color_name, close_color_name = get_colour_name(color)
color2_name, close_color2_name = get_colour_name(color2)

print("Color name of first color is: " + color_name)
print("Closer Color name of first color is: " + close_color_name)
print("Color name of second color is: " + color2_name)
print("Closer Color name of second color is: " + close_color2_name)
if(close_color_name == close_color2_name):
    print("We have a Match")
	







   
    


