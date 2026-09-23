# -*- coding: utf-8 -*-
from datetime import date

from odoo import api, fields, models


class FormEmployee(models.Model):
    _name = 'form.employee'
    _description = 'Data Karyawan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name, id'

    # --- Profil Header ---
    name = fields.Char(string='Nama Lengkap', required=True, tracking=True)
    job_title = fields.Char(string='Jabatan / Job Title', tracking=True)
    image_1920 = fields.Image(string='Foto Profil')

    work_mobile = fields.Char(string='Work Mobile')
    work_phone = fields.Char(string='Work Phone')
    work_email = fields.Char(string='Work Email')
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
    )
    department_id = fields.Char(string='Department')
    manager_id = fields.Many2one('form.employee', string='Manager')
    coach_id = fields.Many2one('form.employee', string='Coach')

    # --- 1. Data Pribadi ---
    alamat_domisili = fields.Text(string='Alamat Domisili')
    same_as_ktp = fields.Boolean(string='Sama dengan Alamat KTP')
    email = fields.Char(string='Email Pribadi', required=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir', required=True)
    umur = fields.Integer(string='Umur', compute='_compute_umur', store=True)
    jenis_kelamin = fields.Selection([
        ('male', 'Laki-laki'),
        ('female', 'Perempuan'),
    ], string='Jenis Kelamin')
    golongan_darah = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O'),
    ], string='Golongan Darah')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    agama = fields.Selection([
        ('islam', 'Islam'),
        ('kristen', 'Kristen'),
        ('katolik', 'Katolik'),
        ('hindu', 'Hindu'),
        ('buddha', 'Buddha'),
        ('konghucu', 'Konghucu'),
    ], string='Agama')

    # --- 2. Status Keluarga ---
    nama_ayah = fields.Char(string='Nama Ayah')
    nama_ibu = fields.Char(string='Nama Ibu')
    status_pernikahan = fields.Selection([
        ('single', 'Belum Menikah'),
        ('married', 'Menikah'),
        ('divorced', 'Cerai'),
    ], string='Status Pernikahan', required=True)
    nama_pasangan = fields.Char(string='Nama Pasangan')
    anak_ids = fields.One2many('form.employee.anak', 'employee_id', string='Data Anak')

    # --- 3. Kependudukan & Kewarganegaraan ---
    no_ktp = fields.Char(string='No. KTP', size=16)
    alamat_ktp = fields.Text(string='Alamat KTP')
    no_npwp = fields.Char(string='No. NPWP', size=15)
    nama_npwp = fields.Char(string='Nama NPWP')
    alamat_npwp = fields.Text(string='Alamat NPWP')
    no_kpj = fields.Char(string='No. KPJ (BPJS TK)')
    no_bpjs = fields.Char(string='No. BPJS Kesehatan')
    status_ptkp = fields.Selection([
        ('TK0', 'TK0 (tanpa tanggungan)'),
        ('TK1', 'TK1 (1 tanggungan)'),
        ('TK2', 'TK2 (2 tanggungan)'),
        ('TK3', 'TK3 (3 tanggungan)'),
        ('K0', 'K0 (tanpa tanggungan)'),
        ('K1', 'K1 (1 tanggungan)'),
        ('K2', 'K2 (2 tanggungan)'),
        ('K3', 'K3 (3 tanggungan)'),
        ('KI0', 'K/I/0 (tanpa tanggungan)'),
        ('KI1', 'K/I/1 (1 tanggungan)'),
        ('KI2', 'K/I/2 (2 tanggungan)'),
        ('KI3', 'K/I/3 (3 tanggungan)'),
    ], string='Status PTKP')
    tanggungan_ids = fields.One2many(
        'form.employee.tanggungan',
        'employee_id',
        string='Data Tanggungan',
    )

    # --- 4. Kontak ---
    telepon1 = fields.Char(string='No. Telepon 1')
    telepon2 = fields.Char(string='No. Telepon 2')
    telepon_tambahan_ids = fields.One2many(
        'form.employee.telepon',
        'employee_id',
        string='No. Telepon Tambahan',
    )
    linkedin = fields.Char(string='LinkedIn')
    facebook = fields.Char(string='Facebook')
    instagram = fields.Char(string='Instagram')

    # --- 5. Kontak Darurat ---
    kontak_darurat_ids = fields.One2many(
        'form.employee.kontak_darurat',
        'employee_id',
        string='Kontak Darurat',
    )

    # --- 6. Informasi Bank & Payroll ---
    rekening_ids = fields.One2many(
        'form.employee.rekening',
        'employee_id',
        string='Informasi Bank & Payroll',
    )

    # --- 7. Pendidikan ---
    pendidikan_ids = fields.One2many(
        'form.employee.pendidikan',
        'employee_id',
        string='Pendidikan',
    )

    # --- Ringkasan data untuk tombol statistik ---
    pendidikan_count = fields.Integer(compute='_compute_related_counts')
    anak_count = fields.Integer(compute='_compute_related_counts')
    tanggungan_count = fields.Integer(compute='_compute_related_counts')
    kontak_darurat_count = fields.Integer(compute='_compute_related_counts')
    rekening_count = fields.Integer(compute='_compute_related_counts')
    telepon_tambahan_count = fields.Integer(compute='_compute_related_counts')

    @api.depends(
        'pendidikan_ids',
        'anak_ids',
        'tanggungan_ids',
        'kontak_darurat_ids',
        'rekening_ids',
        'telepon_tambahan_ids',
    )
    def _compute_related_counts(self):
        for rec in self:
            rec.pendidikan_count = len(rec.pendidikan_ids)
            rec.anak_count = len(rec.anak_ids)
            rec.tanggungan_count = len(rec.tanggungan_ids)
            rec.kontak_darurat_count = len(rec.kontak_darurat_ids)
            rec.rekening_count = len(rec.rekening_ids)
            rec.telepon_tambahan_count = len(rec.telepon_tambahan_ids)

    @api.depends('tanggal_lahir')
    def _compute_umur(self):
        for rec in self:
            if rec.tanggal_lahir:
                today = date.today()
                dob = rec.tanggal_lahir
                rec.umur = today.year - dob.year - (
                    (today.month, today.day) < (dob.month, dob.day)
                )
            else:
                rec.umur = 0

    @api.onchange('same_as_ktp', 'alamat_ktp')
    def _onchange_same_as_ktp(self):
        if self.same_as_ktp and self.alamat_ktp:
            self.alamat_domisili = self.alamat_ktp
