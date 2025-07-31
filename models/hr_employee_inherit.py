from odoo import models, fields


class HREmployee(models.Model):
    _inherit = 'hr.employee'

    certificate_ids = fields.One2many('employee.certificate', 'employee_id', string='Certificates')

    def print_certificate_report(self):
        return self.env.ref('employee_certificate.action_report_certificate').report_action(self)

