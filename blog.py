import web
import base64
import os
import settings

urls = (
  '/', 'home',
  '/index', 'index',
  '/(.*)', 'post')

app = web.application(urls, globals(), autoreload=True)



def render(global_vars = {}, partial = False):
    if 'title' not in global_vars:
        global_vars['title'] = settings.SITE_NAME
        
    if partial:
        return web.template.render('templates/', globals=global_vars)
    else:
        return web.template.render('templates/', base='layout', globals=global_vars)





class index:
    def GET(self):
        posts = map(lambda x: x[:-5], os.listdir('posts'))
        return render().index(settings.SITE_NAME, posts)

class home:
    def GET(self):
        post_list = os.listdir('posts')
        posts = []
        for post in post_list:
            f = open('posts/' + post, 'rb')
            posts += [render_partial.post(post[:-5], f.read())]
            f.close()
            
        return render().home(settings.SITE_NAME, posts)





class post:
    def GET(self, url):
        try:
            f = open('posts/' + url + '.post', 'rb')
            content = f.read()
            f.close()
            name = web.websafe(url)
        except IOError:
            content = "This page does not exist!"
            name = "Not Found."
        
        title = settings.SITE_NAME + " - " + name
        
        return render({'title' : title}).post(name, content)




if __name__ == "__main__":
    app.run()
    
    
    