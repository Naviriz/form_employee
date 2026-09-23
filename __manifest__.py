# -*- coding: utf-8 -*-
{
    'name': 'Form Employee',
    'version': '19.0.1.0.1',
    'category': 'Human Resources',
    'summary': 'Custom Module Form Employee berdasarkan Data Pribadi, Keluarga, Kependudukan, Kontak, Bank, dan Pendidikan',
    'description': """
        Module Form Employee Kustom
        ===========================
        Fitur Utama:
        - Data Pribadi & Identitas (Agama, Tempat/Tgl Lahir, Umur otomatis, Golongan Darah)
        - Status Keluarga (Ayah, Ibu, Pernikahan, Pasangan, List Data Anak)
        - Kependudukan & Kewarganegaraan (No KTP, NPWP, BPJS TK/KPJ, BPJS Kesehatan, Status PTKP & Tanggungan)
        - Kontak & Sosial Media (Telp 1, Telp 2, Kontak Tambahan, LinkedIn, Facebook, Instagram)
        - Kontak Darurat (List Kontak Darurat & Alamat)
        - Informasi Bank & Payroll (List Rekening Bank)
        - Riwayat Pendidikan & Lampiran Ijazah (Gelar, Institusi, Periode, File Ijazah)
        - Visual Layout disesuaikan dengan standar Odoo HR Employee Form View.
    """,
    'author': 'Arnando Ristanta - Solusi247',
    'website': 'https://www.solusi247.com',
    'depends': ['base', 'mail', 'hr'],
    'assets': {
        'web.assets_backend': [
            'form_employee/static/src/css/employee_form_responsive.css',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
