from odoo import fields, models

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _rec_name = "name"

    name = fields.Char("Category Name", required=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The category name must be unique!')
    ]