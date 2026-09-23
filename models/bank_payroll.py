# -*- coding: utf-8 -*-
from odoo import models, fields

class FormEmployeeRekening(models.Model):
    _name = 'form.employee.rekening'
    _description = 'Rekening Bank Employee'

    employee_id = fields.Many2one('form.employee', string='Employee', ondelete='cascade')
    nama_pemilik = fields.Char(string='Nama Pemilik Rekening', required=True)
    bank = fields.Selection([
        ('bca', 'BCA'),
        ('bri', 'BRI'),
        ('bni', 'BNI'),
        ('mandiri', 'Mandiri'),
        ('btn', 'BTN'),
        ('cimb', 'CIMB Niaga'),
        ('danamon', 'Danamon'),
        ('permata', 'Permata')
    ], string='Nama Bank', required=True)
    nomor_rekening = fields.Char(string='Nomor Rekening', required=True)
