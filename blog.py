import web
import base64
import os

urls = (
  '/', 'blog',
  '/(.*)', 'post')

app = web.application(urls, globals(), autoreload=True)

render = web.template.render('templates/', base='base')

class blog:
    def GET(self):
        content = map(lambda x: x[:-5], os.listdir('pages'))
        return render.blog("Templates demo", "Hello", 'posts:', content)


class post:
    def GET(self, url):
        try:
            f = open('pages/' + url + '.post', 'rb')
            content = f.read()
            f.close()
        except IOError:
            content = "This page does not exist!"
        
        #content = base64.b64decode(web.websafe(url))
        #content = os.getcwd()
        return render.post(web.websafe(url), web.websafe(url), content) 
        
if __name__ == "__main__":
    app.run()