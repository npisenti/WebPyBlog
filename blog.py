import web
import base64
import os

urls = (
  '/', 'home',
  '/index', 'index',
  '/(.*)', 'post')

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('templates/', base='base')
render_partial = web.template.render('templates/')

class index:
    def GET(self):
        posts = map(lambda x: x[:-5], os.listdir('pages'))
        return render.index("WebPyBlog", posts)

class home:
    def GET(self):
        post_list = os.listdir('pages')
        posts = []
        for post in post_list:
            f = open('pages/' + post, 'rb')
            posts += [render_partial.post(post[:-5], f.read())]
            f.close()
            
        return render.blog("WebPyBlog", posts)

class post:
    def GET(self, url):
        try:
            f = open('pages/' + url + '.post', 'rb')
            content = f.read()
            f.close()
        except IOError:
            content = "This page does not exist!"
        
        return render.post(web.websafe(url), content)


if __name__ == "__main__":
    app.run()
    
    
    