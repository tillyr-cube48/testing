# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Easier Odoo Deployment',
    'category': 'Discuss',
    'depends': ['mail'],
    'description': """
    Easier Odoo Deployment
    """,
    'author': 'cube48 AG',
    'website': 'https://www.cube48.de',
    'data': [
        'data/github_repository_data.xml',
        'wizard/create_branch_view.xml',
        'wizard/merge_branch_view.xml',
        'wizard/create_repository_view.xml',
        'views/github_account_views.xml',
        'views/github_repository_views.xml',
        'views/res_server_view.xml',
        'views/res_users_views.xml',
        'security/ir.model.access.csv'
    ],
}
