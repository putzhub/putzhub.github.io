AUTHOR = 'Pierce Putz'
SITENAME = 'putz.space'
SITEURL = ' '
#SITESUBTITLE = "Welcome to my humble abode!"

PATH = 'content'
THEME = 'theme/landing'
ARTICLE_PATHS = ['news']
STATIC_PATHS = ['images']


TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

#Webring
WEBRING_FEED_URLS = [
    "https://web.putz.space/feeds/all.atom.xml",
    "https://air.ludoloon.studio/feeds/all.atom.xml",
    "https://ludoloon.studio/feeds/all.atom.xml",
    "https://music.putz.space/feeds/all.atom.xml",
]
WEBRING_ARTICLES_PER_FEED = 10
WEBRING_MAX_ARTICLES = 24

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Image Process
IMAGE_PROCESS = False       #Don't use the Image process plugin for this site

#Sitemap
SITEMAP = {
    "exclude": ["tag/", "category/"],
    "format": "xml",
#    "changefreqs": {
#        "pages": "weekly",
#        "articles": "weekly",
#        "pages": "weekly"
#    }
}