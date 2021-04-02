{
    'name': "My library",
    'summary': "Manage books easily",
    'description': """
    Manage Library
    Description related to library.
    """,
    'author': "Javier Fernandez",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '13.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml'
    ],
    'demo': ['demo.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}