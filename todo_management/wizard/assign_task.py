from odoo import models, fields


class AssignTask(models.TransientModel):
    _name = 'assign.task'
    _description = 'Assign Task Wizard'

    task_ids = fields.Many2many('todo.task')
    assign_to = fields.Many2one('res.partner', required=True)

    def action_confirm(self):
        for task in self.task_ids:
            task.write({'assign_to': self.assign_to.id})

        # ✅ Show success notification instead of reload
        # return [
        #     {
        #         'type': 'ir.actions.client',
        #         'tag': 'display_notification',
        #         'params': {
        #             'title': 'Success',
        #             'message': 'Tasks have been successfully assigned!',
        #             'type': 'success',
        #             'sticky': False,
        #             'next': {
        #                 'type': 'ir.actions.act_window',
        #                 'name': 'Task Action',
        #                 'res_model': 'todo.task',
        #                 'view_mode': 'tree,form',
        #                 'target': 'current',
        #             }
        #         }
        #     }
        # ]
