from odoo import models, fields

class EmployeeToDoTask(models.Model):
    _name = 'employee.todo.task'
    _description = 'Employee To-Do Task'
    _inherit = ['mail.activity.mixin']  # Inherit for activity tracking

    task_name = fields.Char(string="Task Name", required=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string="Priority", default='medium')
    deadline = fields.Date(string="Deadline")
    progress = fields.Selection([
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], string="Progress", default='not_started')
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)