from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MeetingOption(models.Model):
    _name = 'meeting.option'

    meeting_id = fields.Many2one('meeting', string='Meeting')
    option_id = fields.Many2one('option', string='Option')
    count = fields.Float(string='Count', default=0.0)

    def increment_count(self):
        clicked_user = self.env.user
        meeting = self.meeting_id

        # Get current voter IDs as a set
        voter_ids_str = meeting.voter_ids or ""
        voter_ids = set(filter(None, voter_ids_str.split(',')))

        # Check if user already voted
        if str(clicked_user.id) in voter_ids:
            raise ValidationError("You have already voted for this meeting.")

        # Increment count and update voter_ids
        self.count += 1
        voter_ids.add(str(clicked_user.id))
        meeting.voter_ids = ",".join(voter_ids)








