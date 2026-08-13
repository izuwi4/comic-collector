#################################################################################
# main driver for database management                                           #
# largely invoking sql statements as python functions                           #
# NOTES: when the term "image" is used it often refers to images from a gallery #
# this is opposed to something reffering to a comic or comic page               #
#################################################################################

import sqlite3



def __init__():
    #setup
    con = sqlite3.connect("../main.db") 
    cur = con.cursor()

    ###########
    # getters #
    ###########

def get_comic_by_id(id):
    print(id)

def get_image_by_id(id):
    print(id)

def get_artist_by_id(id):
    print(id)

def get_comic_image_by_page(page_num):
    print(page_num)

def get_tags_comic(comic_id):
    print(comic_id)

def get_tags_gallery_image(image_id):
    print(image_id)

    ##########
    # update #
    ##########

def add_tag_comic(tag, comic_id):
    print(f"{tag} {comic_id}")

def remove_tag_comic(tag, comic_id):
    print(f"{tag} {comic_id}")

def add_tag_image(tag, image_id):
    print(f"{tag} {image_id}")

def remove_tag_image(tag, image_id):
    print(f"{tag} {image_id}")

    ##############
    # store data #
    ##############

def sotre_gallery_image(image, image_name, image_path, tags):
    print(f"{image} {image_name} {image_path} {tags}")

def store_comic_image(image, comic_id, page, append=True):
    if append:
        print(f"{image} {comic_id} {page}")


################################################### 
#     this is gordon the goat, he eats bugs       #
# please fix the bugs in your program to feed him #
#        don't let gordon go hungry!              #
###################################################⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠠⠴⠶⠾⠿⠿⠿⢶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿⣆⠐⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠹⠦⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⣀⠐⣶⣿⣿⣿⣿⣿⡄⢀⣀⣀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣿⡆⢹⡿⠻⢿⣿⣿⣷⠈⠿⠛⠁⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣾⣷⣤⣉⣠⣾⣷⣦⣼⣿⣿⣿⣧⠀⠀⠀⠀⠀
#⠀⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀
#⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀
#⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠻⢧⣘⡷⠀⠀⠀
#⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⣉⠛⠿⣷⣦⣌⠁⠀⠀⠀
#⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⠘⠀⠀⢹⣿⣶⣶⠀⠀⠀⠀⠀⠀
#⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⢺⣿⠀⠀⠀⠘⣿⣿⡟⠀⠀⠀⠀⠀⠀
#⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠁⠀⠀⠀⠀⠻⡟⠃⠀⠀⠀⠀⠀⠀
#⠀⠛⠛⠛⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               