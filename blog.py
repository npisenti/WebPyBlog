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
        posts = post_info_list()
        title = settings.SITE_NAME + " - Index" 
        return render({'title' : title }).index(posts)

class home:
    def GET(self):
        posts = render_post_partials()
        return render().home(posts)


class post:
    def GET(self, url):
        return render_post_or_none(url)

class page:
    def GET(self, url):
        return render_page_or_none(url)



if __name__ == "__main__":
    app.run()
    
    
    
