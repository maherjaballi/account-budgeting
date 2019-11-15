# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_budget_oca = fields.Boolean(string='account budget',
        help='This module allows accountants to manage analytic and crossovered budgets. \n'
            'Once the Budgets are defined (in Invoicing/Budgets/Budgets), the Project Managers \n'
            'can set the planned amount on each Analytic Account. \n'
            'The accountant has the possibility to see the total of amount planned for each \n'
            'Budget in order to ensure the total planned is not greater/lower than what he \n'
            'planned for this Budget. Each list of record can also be switched to a graphical \n'
            'view of it. \n'
             '-This installs the module account_budget_oca.')
    
    module_account_budget_template = fields.Boolean(string='account budget template',
        help='A budget template contains different budgetary positions and defines a periodicity \n'
              'to create with a button the corresponding lines. \n')

    