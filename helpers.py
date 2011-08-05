import web
import base64
import os
import settings
import markdown
from datetime import date




def render(params = {}, partial = False):
    static_pages = []
    
    for page in os.listdir('pages'):
        if page[-5:] != ".page":        # Checks to see if it has the right extension.
            continue
            
        page_dict = {} 
        page_dict['name'] = page[3:-5]
        page_dict['path'] = '/page/' + page[3:-5]
        static_pages += [page_dict]                     # Adds page info to list of static pages.
    
    pages = {'static_pages' : static_pages}             # Passes list of static pages to template.
    
    global_vars = dict(settings.GLOBAL_PARAMS.items() + params.items() + pages.items())
    global_vars['markdown'] = markdown.markdown
    
    if partial:
        return web.template.render('templates/', globals=global_vars)
    else:
        return web.template.render('templates/', base='layout', globals=global_vars)


def post_info_list():
    """ Returns a list of post names and paths """

    post_list = filter(lambda x: x[-5:] == ".post", os.listdir('posts'))
    posts = []

    for post in post_list:

        if check_date(post[0:10]):                  # Checks to see if it should be published.
            post_name = " ".join(post[11:-5].split("-"))    # Caluclates name based on naming convention.
            post_path = "/post/" + post[11:-5]              # Calculates path
            post_date = post[0:10]
            posts += [{'post_name': post_name, 'post_path' : post_path, 'post_date': post_date}]
    return posts



def check_date(date_string):
    """ Checks to see if the current date is later than date_string """
    today = date.today()
    try:
        should_publish = date(int(date_string[0:4]), int(date_string[5:7]), int(date_string[8:10])) <= today
    except:                         # To catch poorly formatted date_strings 
        should_publish = False
    
    return should_publish
    
    
    

def render_post_partials():
    """ Returns a list of rendered post partials """
    
    post_list = filter(lambda x: x[-5:] == ".post", reversed(os.listdir('posts')))
    posts = []
    
    for post in post_list:                    
        if check_date(post[0:10]):                  # Checks to see if it should be published.
            f = open('posts/' + post, 'rb')
            post_name = " ".join(post[11:-5].split("-"))    # Caluclates name based on naming convention.
            post_path = "/post/" + post[11:-5]              # Calculates path
            post_date = post[0:10]
            posts += [render(partial = True).post(post_name, post_path, post_date, f.read())]
            f.close()
    return posts




def render_post_or_none(url):
    
    valid_posts = filter(lambda x: x[-5:] == ".post", os.listdir('posts'))
    post_dict = {}
    
    for post in valid_posts:                            # Maps the post name to the file name
        post_dict[post[11:-5]] = post
    
    if (url in post_dict) and check_date(post_dict[url][0:10]):     # Checks to see if given URL leads to valid post file
        f = open('posts/' + post_dict[url], 'rb')
        post_content = f.read()
        post_name = " ".join(url.split("-"))
        post_date = post_dict[url][0:10]
        f.close()
    else:
        post_content = "This page does not exist!"
        post_name = "Not Found"
        post_date = "N/A"
    
    title = web.websafe(settings.SITE_NAME + " - " + post_name)
    post_path = "/post/" + url
    
    return render({'title' : title}).post(post_name, post_path, post_date, post_content)





def render_page_or_none(url):
    page_dict = {}
    valid_pages = filter(lambda x: x[-5:] == ".page", os.listdir('pages'))
    
    for page in valid_pages:
        page_dict[page[3:-5]] = page            # Maps page name to file path

    if (url in page_dict):
        f = open('pages/' + page_dict[url], 'rb')
        page_content = f.read()
        f.close()
    else:
        page_content = "This page does not exist!"

    title = web.websafe(settings.SITE_NAME + " - " + url)

    return render({'title' : title}).page(page_content)
