from odoo import fields

from odoo.tests.common import TransactionCase

class TestTodoTask(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestTodoTask, self).setUp()

        self.todo_task_01_record = self.env['todo.task'].create({
            'task_name': 'Create task 4 from postman',
            'assign_to': 35,
            'due_date': fields.Date.today(),
            'status': 'new'}
        )

    def test_01_todo_task_values(self):
        task_id = self.todo_task_01_record

        self.assertRecordValues(task_id, [{
            'task_name': 'Create task 4 from postman',
            'assign_to': 3,
            'due_date': fields.Date.today(),
        }])