from odoo import models, fields


class EmployeeCertificate(models.Model):
    _name = 'employee.certificate'
    _description = 'Employee Certificate'

    name = fields.Char(string='Certificate Name', required=True)
    certificate_number = fields.Char(string='Certificate Number')
    date_issued = fields.Date(string='Date Issued')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, ondelete='cascade')
    file = fields.Binary(string='Certificate File')

