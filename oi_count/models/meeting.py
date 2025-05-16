from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Meeting(models.Model):
    _name = 'meeting'
    
    name = fields.Char(string='Meeting Name', required=True)
    meeting_option_ids = fields.One2many('meeting.option', 'meeting_id', string='Meeting Option')
    voter_ids = fields.Char(string='Voter ids',default="22")
    current_user = fields.Char(store=False,string='Current User',default=lambda self: self.env.user.id)
    did_voted = fields.Boolean(
        string='Did Voted',
        compute='_compute_did_voted',
        store=False
    )

    @api.depends('voter_ids', 'current_user')
    def _compute_did_voted(self):
        for record in self:
            # voter_ids is a Char field, not a One2many/Many2many
            # So we need to split it into a list to check if current_user is in it
            voter_list = record.voter_ids.split(',') if record.voter_ids else []
            record.did_voted = str(record.current_user) in voter_list

    @api.model_create_multi
    def create(self, vals_list):
        # Create the meeting records
        meetings = super(Meeting, self).create(vals_list)
        
        # For each new meeting, create default active options
        for meeting in meetings:
            # Get all active options
            active_options = self.env['option'].search([('active', '=', True)])
            
            # Create meeting options for each active option
            for option in active_options:
                self.env['meeting.option'].create({
                    'meeting_id': meeting.id,
                    'option_id': option.id,
                    'count': 0.0,
                })
                
        return meetings

