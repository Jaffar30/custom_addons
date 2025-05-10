from odoo import models, fields, api, _
from odoo.exceptions import ValidationError,UserError


class Property(models.Model):
    _name = 'property'

    name = fields.Char(string='name',required=1,default='New',size=20)
    description = fields.Text(string='description')
    postcode = fields.Char(string='postcode',required=1)
    date_availability = fields.Date(string='date availability')
    expected_price = fields.Float(string='expected price',digits='(0,5)')
    selling_price = fields.Float(string='selling price')
    bedrooms = fields.Integer(string='bedrooms',required=1)
    living_area = fields.Integer(string='living area')
    facades = fields.Integer(string='facades')
    garage = fields.Boolean(string='garage')
    garden = fields.Boolean(string='garden')
    garden_area = fields.Integer(string='garden_area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('east', 'East'),
        ('south', 'South'),
        ('west', 'West'),
    ], string='garden Oriantation',default='north')

    _sql_constraints = [
        ('unique_name','unique("name")','The name must be unique')
    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_grater_zero(self):
        for record in self:
            if record.bedrooms < 1:
                raise ValidationError(_("The number of bedrooms must be greater than 0."))

    


# valifation : (inside the postgress: _sql_constrains) , (inside logic tear inside the python file : api.constrains) , (clint side:domain ??)  
    


    