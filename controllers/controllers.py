# -*- coding: utf-8 -*-
# from odoo import http


# class Miniproject(http.Controller):
#     @http.route('/miniproject/miniproject/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/miniproject/miniproject/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('miniproject.listing', {
#             'root': '/miniproject/miniproject',
#             'objects': http.request.env['miniproject.miniproject'].search([]),
#         })

#     @http.route('/miniproject/miniproject/objects/<model("miniproject.miniproject"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('miniproject.object', {
#             'object': obj
#         })
