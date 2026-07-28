project = 'communities-anywhere'
copyright = '2026'
author = 'Admin'

extensions = [ 'sphinx.ext.autodoc',
               'sphinx.ext.napoleon',
               'sphinx_sitemap',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster' # Screenshot wala classic white theme

# conf.py

html_title = "Download Kaspersky Total Security in your Windows PC"
html_short_title = "Download Kaspersky Total Security"

# Meta Tags Configuration
html_context = {
    'metatags': '''
        <meta name="description" content="To download purchased Kaspersky, sign in to your My Kaspersky account, go to Subscriptions, and click Download.">
        <meta name="Download Kaspersky Total Security" content="docs, guide, setup, tutorial">
    '''
}


