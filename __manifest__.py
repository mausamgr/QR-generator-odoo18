{
    'name': 'Partner QR Code',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Generate QR codes for partners',
    'description': """
    """,
    'author': 'Name',
    'website': 'https://www.yourwebsite.com',
    'license': 'LGPL-3',
    'depends': ['base','account'],
    'data': [
        'views/view.xml',
        # 'views/s_snippets.xml',
        'views/templates.xml',
    ],
    'images': [],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'external_dependencies': {
        'python': ['qrcode'],
    },
    'sequence': 1,
}