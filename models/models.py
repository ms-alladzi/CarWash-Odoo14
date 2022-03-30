# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Model(models.Model):
    _name = 'cars.model'
    _description = 'Model Cuci Mobil'

    ukuran = fields.Selection(
        string='Ukuran Mobil', 
        selection=[('mobil ukuran kecil', 'Mobil Ukuran Kecil'), ('mobil ukuran sedang','Mobil Ukuran Sedang'), ('mobil ukuran besar','Mobil Ukuran Besar')]
    )

    tipe = fields.Selection(
        string='Tipe/Jenis Mobil', 
        selection=[('mobil matic', 'Mobil Matic'), ('mobil Manual','Mobil Manual')]
    )

class cuci_mobil(models.Model):
    _name = 'cars.jeniscucimobil'
    _description = 'Daftar Jenis Cuci Mobil'
    _inherit = "cars.model"
    
    name = fields.Char(
        string='Nama Mobil',
    )

    air = fields.Selection(
        string='Jenis Air', 
        selection=[('normal water', 'Normal Water'), ('special water', 'Special Water')],
    )

    harga = fields.Integer(
        string='Harga Cuci Mobil', 
        required=True
    )
    
    active = fields.Boolean(
        default=True
    )
    
    deskripsi = fields.Char(
        string='Deskripsi', 
        help='Isi dengan Alat yang Digunakan untuk Mencuci'
    )

    jenis_id = fields.Many2one(
        comodel_name='cars.jenis', 
        string='Jenis Cuci Mobil'
    )

    @api.constrains('name')
    def _constrains_name(self):
        for rec in self:
            duplicate = self.env['cars.jeniscucimobil'].search([('name','=',rec.name)])
            if len(duplicate)>1:
                raise ValidationError("Mobil Cucian %s Sudah Ada di Daftar!! %s" % (str(rec.name).upper(),str(len(duplicate))))