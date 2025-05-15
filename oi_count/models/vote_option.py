from odoo import models, fields, api, _

class VoteOption(models.Model):
    _name = 'vote.option'

    name = fields.Char(string='Name')
    count = fields.Float(string='Count', default=0.0, readonly=True)
    code = fields.Char(string='Code')
    # currunt_user = fields.Char(default=lambda self: self.env.user)
    # incremented_user = fields.Char()
        
    def increment_count(self):
        for record in self:
            # if self.env.user not in record.incremented_user:
                record.count += 1
                # record.incremented_user = currunt_user
