from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Option(models.Model):
    _name = 'option'
   
    name = fields.Char(string='Option Name')
    code = fields.Char(string='Option Code')
    active = fields.Boolean(string='Active', default=True)
    