{
    'name': "To Do Management",
    'author': "Abdelhameed Mohamed",
    'category': "",
    'version': '19.0.0.1',
    'depends': ['base','mail'],
    'data': [
        'data/sequence.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_view.xml',
        'views/todo_task_view.xml',
        'report/todo_task_report.xml',
        'wizard/assign_task_view.xml'
             ],
    'assets': {
        'web.assets_backend': ['todo_management/static/src/css/todo_task.css'],
        'web.report_assets_common': ['todo_management/static/src/css/fonts.css']
    },
    'application': True,
}
