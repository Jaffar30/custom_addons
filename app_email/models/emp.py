from odoo import models,fields,api,_
from odoo.exceptions import ValidationError

class Emp(models.Model):
    _name = 'app_email.emp'

    name = fields.Char(string='Name',translate=True)
    email = fields.Char(string='Email')
    manager_email = fields.Char(string='Manager Email')
    age = fields.Integer(string='Age')
    prob_date = fields.Date(string='Probation Date')
    stage = fields.Selection([
        ('prob', 'Probation'),
        ('employed', 'Employed'),
    ], string='Stage')

    def emp_email_cron(self):
        print('==========================================================================================')
        emps = self.env['app_email.emp'].search([('stage','=','prob')])
        print(emps)
        for emp in emps:
            emp_prob_left_days = (emp.prob_date - fields.Date.today()).days
            if (emp_prob_left_days % 3 == 0) or ((emp_prob_left_days < 6) and (emp_prob_left_days > 0)):
                print(f"{emp.name} get email at day number {emp_prob_left_days}")
                if emp.email:
                    template = template = self.env.ref('app_email.email_template_emp_probation')
                    template.with_context(lang='ar_001').send_mail(emp.id, force_send=True)
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


    