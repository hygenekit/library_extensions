from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one(
        'res.partner',
        string='Author',
        required=True
    )

    category_id = fields.Many2many(
        'library.book.category',
        string='Categories'
    )


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'

    name = fields.Char(string='Category Name', required=True, unique=True)

    _sql_constraints = [
        ('name_unique',
         'unique(name)',
         'Category name must be unique!')
    ]
