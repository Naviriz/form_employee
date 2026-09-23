# -*- coding: utf-8 -*-
from odoo import models, fields

class FormEmployeePendidikan(models.Model):
    _name = 'form.employee.pendidikan'
    _description = 'Riwayat Pendidikan Employee'

    employee_id = fields.Many2one('form.employee', string='Employee', ondelete='cascade')
    gelar = fields.Selection([
        ('sma_smk', 'SMA / SMK'),
        ('d1', 'D1'),
        ('d2', 'D2'),
        ('d3', 'D3'),
        ('s1', 'S1'),
        ('s2', 'S2'),
        ('s3', 'S3')
    ], string='Gelar / Jenjang')
    nama_gelar = fields.Char(string='Singkatan Gelar', help='Contoh: S.Kom')
    bidang = fields.Char(string='Bidang Studi')
    institusi = fields.Char(string='Sekolah / Universitas')
    mulai = fields.Integer(string='Tahun Mulai')
    selesai = fields.Integer(string='Tahun Selesai')
    ijazah_file = fields.Binary(string='File Ijazah')
    ijazah_filename = fields.Char(string='Nama File Ijazah')
