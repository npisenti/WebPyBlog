import web
import base64
import os
import settings
import markdown
from datetime import date


def render(params = {}, partial = False):
    global_vars = dict(settings.GLOBAL_PARAMS.items() + params.items())
    global_vars['markdown'] = markdown.markdown
    if partial:
        return web.template.render('templates/', globals=global_vars)
    else:
        return web.template.render('templates/', base='layout', globals=global_vars)


def check_date(date_string):
    today = date.today()
    return date(int(date_string[0:4]), int(date_string[5:7]), int(date_string[8:10])) <= today

def posting_list():
    post_list = os.listdir('posts')
    posts = []
    for post in post_list:
        if check_date(post[0:10]):  
            f = open('posts/' + post, 'rb')
            post_name = " ".join(post[11:-5].split("-"))
            posts += [render(partial = True).post(post_name, post[11:-5], f.read())]
            f.close()
    return posts

def render_post_or_none(url):
    post_dir = {}
    for post in os.listdir('posts'):
        post_dir[post[11:-5]] = post
    
    if (url in post_dir) and check_date(post_dir[url][0:10]):
        f = open('posts/' + post_dir[url], 'rb')
        post_content = f.read()
        post_name = web.websafe(" ".join(url.split("-")))
        f.close()
    else:
        post_content = "This page does not exist!"
        post_name = "Not Found."
    
    title = settings.SITE_NAME + " - " + post_name
    
    return render({'title' : title}).post(post_name, url, post_content)
    
