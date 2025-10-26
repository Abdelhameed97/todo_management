import json
import requests

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'task_name'

    task_name = fields.Char(tracking=1, required=True, size=50)
    ref = fields.Char(readonly=True, default="New")
    assign_to = fields.Many2one('res.partner', required=True, tracking=1)
    description = fields.Text()
    due_date = fields.Date(required=True, tracking=1)
    is_late = fields.Boolean()
    estimated_time = fields.Float()
    spent_time = fields.Float(compute="_compute_spent_time", store=True)
    progress = fields.Float(
        string="Progress (%)",
        compute="_compute_progress",
        store=True
    )
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed')
    ], default='new', tracking=1)

    lines_ids = fields.One2many('todo.task.line', 'todo_task_id')

    # _sql_constraints=[
    #     ('unique_task_name', 'unique(task_name)', 'Task Already Exist!')
    # ]
    _constraints = [
        models.Constraint('UNIQUE(task_name)', 'Task Already Exist!')
    ]

    @api.constrains('spent_time', 'estimated_time')
    def _check_time_limits(self):
        for rec in self:
            if rec.estimated_time and rec.spent_time > rec.estimated_time:
                raise ValidationError("Spent time can't exceed estimated time!")

    @api.depends('lines_ids.time')
    def _compute_spent_time(self):
        for rec in self:
            rec.spent_time = sum(line.time for line in rec.lines_ids)

    @api.depends('estimated_time', 'spent_time')
    def _compute_progress(self):
        for rec in self:
            if rec.estimated_time:
                rec.progress = (rec.spent_time / rec.estimated_time) * 100
            else:
                rec.progress = 0

    def action_new(self):
        for rec in self:
            rec.status= 'new'
            print("Inside Action New")

    def action_in_progress(self):
        for rec in self:
            rec.status= 'in_progress'
            print("Inside Action IN Progress")

    def action_completed(self):
        for rec in self:
            rec.status= 'completed'
            print("Inside Action Completed")


    def close_task(self):
        for rec in self:
            print("Inside close task server action")
            rec.status = 'closed'

    def check_due_date(self):
        # this variable for read all records in  todo.task()
        tasks_ids = self.search([])
        # loop on all tasks and make your logic
        for rec in tasks_ids:
            if rec.status in ['completed', 'closed']:
                continue
            elif rec.due_date and rec.due_date < fields.Date.today():
                rec.is_late = True

        print("inside check_due_date()")

    @api.model
    def create(self, vals):
        res = super(TodoTask, self).create(vals)

        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('todo_sequence')
        return res

    def action_open_assign_task(self):
        action = self.env['ir.actions.actions']._for_xml_id('todo_management.assign_task_action')
        action['context']= {'default_task_ids': [(6, 0, self.ids)]}
        return action

    def get_tasks(self):
        payloud = dict()
        response = requests.get("http://localhost:8069/v1/todo/read_tasks", data=payloud)
        if response.status_code == 200:
            print("successful process!")
            content = response.content
            print("content", content)
            vals = json.loads(content)
            print("vals", vals)
        else:
            print("failed process!")

class TodoTaskLine(models.Model):
    _name = 'todo.task.line'

    todo_task_id = fields.Many2one('todo.task', required=True, ondelete="cascade")
    date = fields.Date()
    description = fields.Text()
    time = fields.Float()
