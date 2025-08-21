{
    'name': 'Library Extensions',
    'version': '1.0',
    'category': 'Library',
    'summary': 'Adds author and category features to library books',
    'author': 'Gene Louise Lopez',
    'depends': ['library'],
    'data': [
        'views/library_category_views.xml',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}
