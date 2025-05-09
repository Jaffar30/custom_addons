from odoo import models, fields, api, _

class Property(models.Model):
    _name = 'property'

    name = fields.Char(string='name')
    description = fields.Text(string='description')
    postcode = fields.Char(string='postcode')
    date_availability = fields.Date(string='date availability')
    expected_price = fields.Float(string='expected price')
    selling_price = fields.Float(string='selling price')
    bedrooms = fields.Integer(string='bedrooms')
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
    ], string='garden Oriantation')
    


    