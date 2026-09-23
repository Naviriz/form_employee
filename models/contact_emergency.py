# -*- coding: utf-8 -*-
from odoo import models, fields

class FormEmployeeTelepon(models.Model):
    _name = 'form.employee.telepon'
    _description = 'No Telepon Tambahan Employee'

    employee_id = fields.Many2one('form.employee', string='Employee', ondelete='cascade')
    nomor = fields.Char(string='Nomor Telepon', required=True)


class FormEmployeeKontakDarurat(models.Model):
    _name = 'form.employee.kontak_darurat'
    _description = 'Kontak Darurat Employee'

    employee_id = fields.Many2one('form.employee', string='Employee', ondelete='cascade')
    nama = fields.Char(string='Nama Kontak', required=True)
    hubungan = fields.Selection([
        ('orang_tua', 'Orang Tua'),
        ('pasangan', 'Pasangan'),
        ('saudara', 'Saudara'),
        ('kerabat', 'Kerabat'),
        ('lainnya', 'Lainnya')
    ], string='Hubungan')
    telepon1 = fields.Char(string='No. Telepon 1')
    telepon2 = fields.Char(string='No. Telepon 2')
    alamat = fields.Text(string='Alamat')
