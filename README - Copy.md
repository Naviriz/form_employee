# Form Employee — Odoo 19

## Perbaikan pada versi ini

1. **Flow list → form diperjelas**
   - Action `action_form_employee` tetap menggunakan `list,form`.
   - Ditambahkan `ir.actions.act_window.view` untuk mengikat view List dan Form secara eksplisit.
   - Saat record karyawan dibuka dari daftar, Odoo diarahkan ke view `form.employee.form`, bukan ke view model lain.

2. **Halaman "Related Document Model Name" tidak lagi muncul sebagai akibat dari chatter**
   - Form sebelumnya menulis widget lama secara manual:
     `mail_followers`, `mail_activity`, dan `mail_thread`.
   - Pada Odoo 19, Form View mendukung semantic component `<chatter/>`; konfigurasi chatter custom sekarang memakai `<chatter/>`.
   - Ini juga menghilangkan sumber log `Missing widget: mail_followers`, `Missing widget: mail_activity`, dan `Missing widget: mail_thread` dari view karyawan.

3. **CSS custom disederhanakan dan diisolasi**
   - Semua selector tetap diawali `.o_form_employee` agar tidak mengubah backend Odoo global.
   - CSS tidak lagi memaksa `.oe_button_box` menjadi flex/grid custom atau memberi minimum width besar pada semua list.
   - Layout dua kolom hanya diterapkan pada wrapper `<div class="o_employee_primary_layout">`, sementara layout native `<group>` Odoo tetap dipertahankan.
   - Breakpoint mobile tetap tersedia untuk layar sempit.

4. **Menu icon yang menunjuk ke file yang tidak tersedia di source package dihapus**
   - Referensi `web_icon="form_employee,static/description/icon.png"` dihapus karena file `static/description/icon.png` tidak terdapat di source yang dikirim.

## Catatan penting: error CSS Odoo 19 di Windows

Console yang menunjukkan:

```text
Could not get content for base/static/src/scss/res_partner.scss
Could not get content for base/static/src/scss/res_users.scss
Could not get content for base/static/src/css/modules.css
```

bukan berasal dari stylesheet `employee_form_responsive.css` saja. Log server yang dikirim menunjukkan `addons paths` menggunakan campuran separator Windows `\\` dan `/`, misalnya path inti Odoo tampil sebagai:

```text
E:\\NGODING/SOLUSI247/odoo\\odoo\\addons
```

Pada Odoo 19 di Windows, pola ini terkait dengan kegagalan pencarian asset SCSS/CSS. Karena `odoo19.conf` berada di luar module zip, file konfigurasi tersebut tidak diubah oleh package ini.

### Rekomendasi `odoo19.conf`

Gunakan path Windows yang konsisten. Contoh:

```ini
[options]
addons_path = E:/NGODING/SOLUSI247/odoo/odoo/addons,E:/NGODING/SOLUSI247/odoo/addons,E:/NGODING/SOLUSI247/odoo/odoo/custom_folder
http_interface = 127.0.0.1
```

Catatan:
- Sesuaikan lokasi `addons_path` dengan folder Odoo Anda.
- Jangan isi `db_name = False`. Hapus baris tersebut bila tidak diperlukan, atau isi dengan nama database yang benar.
- Bila `--dev=xml` masuk ke daftar `update`, hapus dari daftar module. Untuk command line, `--dev=xml` harus menjadi option terpisah.

### Setelah konfigurasi diperbaiki

Restart Odoo dan upgrade module:

```powershell
python odoo-bin -c odoo19.conf -d TUTORIAL_ODOO19 -u form_employee --stop-after-init
python odoo-bin -c odoo19.conf -d TUTORIAL_ODOO19
```

Kemudian hard refresh browser (`Ctrl+Shift+R`). Dalam development mode, bersihkan cache browser/service worker bila asset lama masih tersimpan.

## Log yang masih terpisah dari module ini

Log seperti:

```text
module odoo_solusi: not installable, skipped
Missing model odoo.absensi
Missing model odoo.solusi
Missing model test.model
Missing model odoo.divisi
```

menunjukkan ada metadata/module lama atau module lain di database `TUTORIAL_ODOO19`. Error tersebut bukan referensi model yang didefinisikan oleh `form_employee`. Perbaiki setelah module ini berhasil di-load; jangan menghapus metadata database secara manual tanpa backup.

## Checklist pengujian

1. Restart Odoo.
2. Upgrade `form_employee`.
3. Buka **Data Karyawan → Daftar Karyawan**.
4. Klik salah satu baris karyawan.
5. Pastikan yang terbuka adalah Form `Data Karyawan` lengkap dengan foto profil, informasi kerja, tab data pribadi/keluarga, kependudukan, kontak, bank, pendidikan, dan chatter.
6. Pastikan tidak muncul halaman dengan kolom `Related Document Model Name`.
7. Uji pada lebar browser > 1390 px dan < 1390 px.
8. Periksa console. Log `Missing widget: mail_followers/mail_activity/mail_thread` seharusnya hilang setelah view ter-upgrade dan asset ter-refresh.
9. Bila error `Could not get content for base/static/...` masih muncul, fokuskan troubleshooting ke `addons_path` Windows Odoo 19 seperti di atas; itu bukan bug pada XML Form Employee.
