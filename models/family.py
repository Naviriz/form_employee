# -*- coding: utf-8 -*-
from odoo import models, fields

class FormEmployeeAnak(models.Model):
    _name = 'form.employee.anak'
    _description = 'Data Anak Employee'

    employee_id = fields.Many2one('form.employee', string='Employee', ondelete='cascade')
    nama = fields.Char(string='Nama Anak', required=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    jenis_kelamin = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan')
    ], string='Jenis Kelamin')


class FormEmployeeTanggungan(models.Model):
    _name = 'form.employee.tanggungan'
    _description = 'Data Tanggungan Employee'

    employee_id = fields.Many2one('form.employee', string='Employee', ondelete='cascade')
    nama = fields.Char(string='Nama Tanggungan', required=True)
    hubungan = fields.Selection([
        ('anak', 'Anak'),
        ('istri', 'Istri'),
        ('suami', 'Suami'),
        ('lainnya', 'Lainnya')
    ], string='Hubungan', required=True)
