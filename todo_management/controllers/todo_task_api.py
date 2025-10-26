import json
import math
from urllib.parse import parse_qs

from odoo import http
from odoo.http import request
from . import todo_response

class TodoTaskApi(http.Controller):

    # create one task.
    @http.route("/v1/todo/create_task", method=['POST'], type="http", auth="none", csrf=False)
    def create_task(self):
        try:
            args = request.httprequest.data.decode()
            vals = json.loads(args)
            print(vals)
            ## validation layer for task_name and assign_to
            if not vals.get("task_name"):
                return todo_response.invalid_response("Task name is required!", 400)

            if not vals.get("assign_to"):
                return todo_response.invalid_response("assign_to field is required!", 400)

            res = request.env['todo.task'].sudo().create(vals)
            if res:
                return todo_response.valid_response({
                    "message": "Task created successfully!",
                    "task_name": res.task_name,
                    "assign_to": res.assign_to.name,
                    "due_date": res.due_date
                }, 201)
        except Exception as error:
            return request.make_json_response({
                "error": error
            }, status=400)

    #read all tasks
    @http.route("/v1/todo/read_tasks", method=['GET'], type="http", auth="none", csrf=False)
    def read_tasks(self):
        try:
            search_domain = []
            params = parse_qs(request.httprequest.query_string.decode('utf-8'))

            page = offset = 1
            limit = 10

            if params.get('status'):
                search_domain += [('status', '=', params.get('status'))]

            if params:
                if params.get("page"):
                    page = int(params.get("page")[0])
                    offset = (page*limit) - limit
                if params.get("limit"):
                    limit = int(params.get("limit")[0])

            tasks = request.env['todo.task'].sudo().search(search_domain, offset=offset, limit=limit, order="id DESC")
            tasks_count = request.env['todo.task'].sudo().search_count(search_domain)

            if tasks:
                return todo_response.valid_response([{
                    "task_name": task.task_name,
                    "assign_to": task.assign_to.name,
                    "due_date": task.due_date,
                    "status": task.status
                }for task in tasks],{
                    "page": page if page else 1,
                    "limit": limit,
                    "pages": math.ceil(tasks_count/limit) if limit else 1,
                    "records count": tasks_count
                } ,200)
            else:
                return request.make_json_response({
                    "message": "There is no records!"
                }, status=200)
        except Exception as error:
            return todo_response.invalid_response( error, 400)

    # read one task by its id
    @http.route("/v1/todo/read_task/<int:task_id>", method=['GET'], type="http", auth="none", csrf=False)
    def read_task(self, task_id):
        try:
            task = request.env['todo.task'].sudo().search([('id', '=', task_id)])
            if not task:
                return todo_response.invalid_response(f"Task with id={task_id} doesn't existed!",404)

            return todo_response.valid_response({
                "message": "Read task successfully!",
                "task_name": task.task_name,
                "assign_to": task.assign_to.name,
                "due_date": task.due_date,
                "status": task.status,
                "description": task.description
            }, {},200)
        except Exception as error:
            return todo_response.invalid_response(error, 400)

    # update one task by its id
    @http.route("/v1/todo/update_task/<int:task_id>", method=['PUT'], type="http", auth="none", csrf=False)
    def update_task(self, task_id):
        try:
            task = request.env['todo.task'].sudo().search([('id', '=', task_id)])
            if not task:
                return todo_response.invalid_response(f"Task with id={task_id} doesn't existed!", 404)

            args = request.httprequest.data.decode()
            vals = json.loads(args)
            task.write(vals)

            return todo_response.valid_response({
                "task_name": task.task_name,
                "assign_to": task.assign_to.name,
                "due_date": task.due_date,
                "status": task.status,
                "description": task.description
            },{},200)
        except Exception as error:
            return todo_response.invalid_response( error, 400)

    # delete one task by its id
    @http.route("/v1/todo/delete_task/<int:task_id>", method=['DELETE'], type="http", auth="none", csrf=False)
    def delete_task(self, task_id):
        try:
            task = request.env['todo.task'].sudo().search([('id', '=', task_id)])
            if not task:
                return todo_response.invalid_response(f"Task with id={task_id} doesn't existed!", 404)

            task.unlink()
            return request.make_json_response({
                "message": "Task deleted successfully!"
            }, status=200)
        except Exception as error:
            return todo_response.invalid_response(error, 400)