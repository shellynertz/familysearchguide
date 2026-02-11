project = 'familysearch-login-account'
author = 'familysearch-login-account'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Bing search verification
html_context = {
    'bing_verification_code': '739245F5D54BCBF40AC056DC0CBF5710'
}

# Base URL for sitemap
html_baseurl = 'https://familysearchguide.readthedocs.io/en/latest/'
