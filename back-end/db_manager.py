#################################################################################
# main driver for database management                                           #
# largely invoking sql statements as python functions                           #
# NOTES: when the term "image" is used it often refers to images from a gallery #
# this is opposed to something reffering to a comic or comic page               #
#################################################################################
# TODO: after the project has a working proof of concept #
# make sure to delete redundant functions                #
##########################################################
import sqlite3
__db_path__ = "../main.db"

 
def execute_query(query, parameters):
    ret_val=[]
    con = sqlite3.connect(__db_path__)
    cur = con.cursor()
    try:
        cur.execute(query, parameters)
        rows = cur.fetchall()
        # the returned value will be a list of touples containing a single element
        # and so we iterate through the list to create one clean list of those values
        ret_val = [row[0] for row in rows]
    except Exception as e:
        print(e)
    finally:
        con.close()

    return ret_val

#######################
#  function structure #
#######################
'''
def sample_function(param: datatype):
    if not isinstance(param, datatype):
        raise TypeError(f"param was {type(param).__name__}, but should be datatype")

    query =/'/'/'
    COMMAND parameter /'/'/'

    execute_query(query, (param))

'''
########
# read #
########

def get_comic_pages_by_id(comic_id: int):
    if not isinstance(comic_id, int):
        raise TypeError(f"comic_id was {type(comic_id).__name__}, but should be int")
    query = '''
    SELECT img 
    FROM comic_page 
    WHERE parent_comic_id = ? 
    ORDER BY page'''

    comic_pages = execute_query(query, (comic_id))
    if comic_pages == []:
        print(f"no comic was found from id {comic_id}")

    return comic_pages

def get_gallery_by_artist_id(artist_id: int):
    if not isinstance(artist_id, int):
        raise TypeError(f"image_id was {type(image_id).__name__}, but should be int")

    query = '''
    SELECT img
    FROM gallery_image
    WHERE artist_id == ?
    '''

    gallery = execute_query(query, (artist_id))
    if gallery == []:
        print("no such artist has gallery images")

    return gallery

def get_image_by_id(image_id, order):
    if not isinstance(image_id, int):
        raise TypeError(f"image_id was {type(image_id).__name__}, but should be int")
    if not order in get_table_elements('gallery_image'):
        raise LookupError(
        f"order given was {order} but {order} is not a valid element in the gallery_image table"
        )

    query = '''
    SELECT img
    FROM gallery_image
    WHERE artist_id = ?
    ORDER BY ?
    '''    

    return execute_query(query, (order))

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

def store_comic_image(image, comic_id, page):
    if page == None:
        print(f"{image} {comic_id} {page}")

########
# misc #
########

def get_table_elements(table: str):
    if not table in execute_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"):
        raise LookupError(
        f"table given was {table} but {table} could not be found in the database"
        )
    
    query = '''
    SELECT column_name
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_NAME = ?
    '''
    return execute_query(query, (table))



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