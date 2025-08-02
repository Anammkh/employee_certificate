{
    'name': 'Employee Certificate',
    'version': '16.0.1.0.0',
    'summary': 'Manage employee certificates linked to employees',
    'description': """
This module allows HR managers to manage employee certificates and generate PDF reports.
""",
    'author': 'Khoirul Anam',
    'website': 'https://github.com/Anammkh',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    'depends': ['hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/employee_certificate_views.xml',
        'views/hr_employee_inherit.xml',
        'report/certificate_template.xml',
        'report/certificate_report.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
