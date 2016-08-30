# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Swedish - Accounting',
    'version': '1.0',
    'category': 'Localization/Account Charts',
    'description': """
This is the module to manage the accounting chart for Sweden in Odoo.
==============================================================================

Install some swedish chart of accounts.
    """,
    'author': 'Linserv AB',
    'depends': [
        'account',
    ],
    'data': [
        'data/account_chart.xml',
        'data/account_tax.xml',
        'data/account_fiscal.xml',
        'account_chart_template.yml',
    ],
    'test': [
        '../account/test/account_bank_statement.yml',
        #'../account/test/account_cash_statement.yml',
        '../account/test/account_invoice_state.yml',
    ],
    'demo': [
        '../account/demo/account_bank_statement.yml',
        '../account/demo/account_invoice_demo.yml',
    ],
    'installable': True,
    'website': 'https://www.linserv.se',
}
