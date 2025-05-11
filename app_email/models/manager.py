from odoo import models,fields,api,_
from odoo.exceptions import ValidationError

class Manager(models.Model):
    _name = 'app_email.manager'

    name = fields.Char(string='Name',translate=True)
    email = fields.Char(string='Email')
    emp_id = fields.Many2one('app_email.emp', string='emp')
    

    