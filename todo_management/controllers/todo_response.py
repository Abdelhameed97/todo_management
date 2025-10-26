from odoo.http import request

def valid_response(data, meta_data, status):
    response_body = {
        "message": "done successfully!",
        "data": data,
    }
    if meta_data:
        response_body['meta_data'] = meta_data
    return request.make_json_response(response_body, status=status)

def invalid_response(error, status):
    response_body = {
        "error": error,
    }
    return request.make_json_response(response_body, status=status)