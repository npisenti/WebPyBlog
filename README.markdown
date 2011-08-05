# Projects

## WebPyBlog

This was just a fun project to try out the web.py platform. I wanted to write a lightweight blog implementation, which could be deployed with very little setup. Any comments/suggestions on the code are welcome!  I'm just a hobbyist programmer and this is my first web.py project, so hopefully there are no glaring security holes...

### How to manage content on WebPyBlog

The "Projects", "About", and "Contact" pages are example static pages. They are kept in the pages folder, and named

	01-projects.page
	02-about.page
	03-contact.page

Hopefully that naming scheme is clear...

The posts are kept (surprisingly) in the "posts" folder. They are named like:

	YYYY-MM-DD-Post-Name.post

If you want to publish something at a future date, simply give it a date in the future. It won't be accessible or displayed until that day arrives.

### Manage your posts and pages using Git

I was inspired by the Haskell-implemented [Gitit wiki](http://gitit.net/), which uses Git to manage its wiki pages. It seemed like an elegant solution, and I was personally growing tired of the clunky-slow Wordpress editing environment. Thus, use your text editor of choice, commit changes to a git repository, and push it out to your server. I recommend tracking the whole WebPyBlog project folder, that way you can push out changes to the CSS or base code as needed.

Thats about it! Enjoy!