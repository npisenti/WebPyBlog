import web
import settings
from helpers import *

urls = (
  '/', 'home',
  '/index', 'index',
  '/page/(.*)', 'page',
  '/post/(.*)', 'post')

app = web.application(urls, globals(), autoreload=True)




class index:
    def GET(self):
        posts = map(lambda x: x[:-5], os.listdir('posts'))
        return render().index(settings.SITE_NAME, posts)

class home:
    def GET(self):
        posts = posting_list()
        return render().home(posts)


class post:
    def GET(self, url):
        return render_post_or_none(url)

class page:
    def GET(self, url):
        return render_page_or_none(url)

if __name__ == "__main__":
    app.run()
    
    
    
