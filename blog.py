import web
import base64
import os
import settings

urls = (
  '/', 'home',
  '/index', 'index',
  '/(.*)', 'post')

app = web.application(urls, globals(), autoreload=True)


#render = web.template.render('templates/', base='layout')
render_partial = web.template.render('templates/')

def render(global_vars = {}, partial = False):
    if 'title' not in global_vars:
        global_vars['title'] = settings.SITE_NAME
        
    if partial:
        return web.template.render('templates/', globals=global_vars)
    else:
        return web.template.render('templates/', base='layout', globals=global_vars)



class home:
    def GET(self):
        post_list = os.listdir('pages')
        posts = []
        for post in post_list:
            f = open('pages/' + post, 'rb')
            posts += [render_partial.post(post[:-5], f.read())]
            f.close()
            
        return render().home(settings.SITE_NAME, posts)



class index:
    def GET(self):
        posts = map(lambda x: x[:-5], os.listdir('pages'))
        return render().index(settings.SITE_NAME, posts)



class post:
    def GET(self, url):
        try:
            f = open('pages/' + url + '.post', 'rb')
            content = f.read()
            f.close()
        except IOError:
            content = "This page does not exist!"
        
        return render.post(settings.SITE_NAME + " - " + web.websafe(url), content)


if __name__ == "__main__":
    app.run()
    
    
    