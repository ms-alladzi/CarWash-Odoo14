from odoo import api, fields, models


class Jenis(models.Model):
    _name = 'cars.jenis'
    _description = 'Daftar Jenis Layanan Cuci Mobil'

    name = fields.Selection(
        string='Nama Pilihan Jenis', 
        selection=[('cuci mobil manual','Cuci Mobil Manual'), ('cuci mobil hidrolik','Cuci Mobil Hidrolik'), ('cuci mobil waterless','Cuci Mobil Waterless'), ('cuci mobil touchless','Cuci Mobil Touchless'), ('cuci mobil robotic','Cuci Mobil Robotic')],
    )

    air = fields.Selection(
        string='Jenis Air', 
        selection=[('normal water', 'Normal Water'), ('special water', 'Special Water')],
    )

    kotoran =  fields.Selection(
        string='Tipe Kotoran', 
        selection=[('ringan', 'Ringan'), ('sedang', 'Sedang'), ('berat', 'Berat')],
    )

    tersedia = fields.Boolean(
        string='Tersedia', 
        default=True
    )
    
    deskripsi = fields.Char(
        string='Deskripsi', 
        help='Isi dengan Alat yang Digunakan untuk Mencuci'
    )

    models_ids = fields.One2many(
        comodel_name='cars.jeniscucimobil', 
        inverse_name='jenis_id',
        string='Jenis Mobil'
    )
    