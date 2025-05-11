from odoo import models,fields,api,_
from odoo.exceptions import ValidationError

class Emp(models.Model):
    _name = 'app_email.emp'

    name = fields.Char(string='Name',translate=True)
    email = fields.Char(string='Email')
    manager_ids = fields.One2many('app_email.manager', 'emp_id', string='manager')
    age = fields.Integer(string='Age')
    prob_date = fields.Date(string='Probation Date')
    stage = fields.Selection([
        ('prob', 'Probation'),
        ('employed', 'Employed'),
    ], string='Stage')

    def emp_email_cron(self):
        print('==========================================================================================')
        emps = self.env['app_email.emp'].search([('name','=','Ali')])
        for emp in emps:
                    template = template = self.env.ref('app_email.email_template_emp_probation')
                    template.with_context(lang='ar_001').send_mail(emp.id)
        print('==========================================================================================')
        # prob_date = "2025-05-30" 
        # today_date = fields.Date.today()
        # left_days = (fields.Date.from_string(prob_date) - today_date).days
        # print(f"Left days: {left_days}")
        # print('==========================================================================================')
        # for day in range(left_days, -1, -1):  # start from left_days, stop at 0 (inclusive), decrement by 1
        #     if(day%3==0 or day<6):
        #         print('==========================================================================================')
        #         print(f"The Cron will trigger on the day number {day}")
        #         print('==========================================================================================')


    