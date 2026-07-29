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

html_baseurl = 'https://communities-anytime-downloadkaspersky.readthedocs-hosted.com/en/latest/'
sitemap_url_scheme = "{link}"

# conf.py

html_title = "Download Kaspersky Total Security in your Windows PC"
html_short_title = "Download Kaspersky Total Security"
html_static_path = ['_static']
html_extra_path = ['_static/google5ffeff63dcb91d99.html'] 


# Meta Tags Configuration
html_context = {
    'metatags': '''
        <meta name="description" content="Kaspersky Total Security protects PCs, Macs, and phones from viruses, ransomware, and online threats, all in one easy multi-device plan.">
        <meta name="Download Kaspersky Total Security" content="docs, guide, setup, tutorial">
     
    '''
}


