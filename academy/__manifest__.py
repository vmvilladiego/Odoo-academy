# -*- coding: utf-8 -*-
{
    'name' : 'Odoo Academy',
    'version' : '1.0',
    'summary': 'Module to handle Course and Sessions',
    'description': """
        Module to Handle
        ====================
        - Courses
        - Sessions
        - Attendees
            """,
    'license': 'OPL-1',
    'author': 'MIGUEL VILLADIEGO GARCIA',
    'website': 'vmvg.com',
    'category': 'Custom Modules/Tech Training',
    'depends' : ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'views/academy_menuitems.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'application': True,
}
