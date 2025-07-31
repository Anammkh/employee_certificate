{
    'name': 'Employee Certificate',
    'version': '1.0',
    'depends': ['hr'],
    'author': 'Your Name',
    'category': 'Human Resources',
    'description': 'Manage employee certificates',
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
}

