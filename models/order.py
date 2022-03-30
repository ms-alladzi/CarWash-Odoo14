from odoo import api, fields, models


class Order(models.Model):
    _name = 'cars.order'
    _description = 'Daftar Pemesanan'

    
    name = fields.Char(string='Kode Order')

    tgl_order = fields.Datetime(
        string='Tanggal Order',
        default=fields.Datetime.now
    )
    
    detailcuci_ids = fields.One2many(
        comodel_name='cars.detailorder',
        inverse_name='order_id',
        string='Detail Order'
    )

    jumlah_order = fields.Integer(
        compute='_compute_jumlah_order', 
        string='Jumlah Order'
    )
    
    total_harga = fields.Integer(
        compute='_compute_total_harga', 
        string='Total Harga'
    )
    
    @api.model
    def _compute_total_harga(self):
        for record in self:
            total = sum(self.env['cars.detailorder'].search([('order_id','=',record.id)]).mapped('jumlah_harga'))
            record.total_harga = total

    @api.depends('detailcuci_ids')
    def _compute_jumlah_order(self):
        for record in self:
            record.jumlah_order = len(record.detailcuci_ids)

class DetailOrder(models.Model):
    _name = 'cars.detailorder'
    _description = 'Detail Pesanan Cuci'
    _inherit = "cars.order"

    name = fields.Char(string='Kode Order')

    order_id = fields.Many2one(
        comodel_name='cars.order', 
        string='Pemesanan'
    )
    models_id = fields.Many2one(
        comodel_name='cars.jeniscucimobil', 
        string='Jenis Mobil'
    )

    harga = fields.Integer(
        compute='_compute_harga', 
        string='Harga (per mobil)'
    )

    detailcuci_ids = fields.One2many(
        comodel_name='cars.detailorder',
        inverse_name='order_id',
        string='Detail Order'
    )

    jumlah = fields.Integer(
        compute='_compute_jumlah', 
        string='Jumlah Mobil'
    )

    jumlah_harga = fields.Integer(
        compute='_compute_jumlah_harga', 
        string='Jumlah Harga'
    )

    @api.depends('detailcuci_ids')
    def _compute_jumlah(self):
        for record in self:
            record.jumlah = len(record.detailcuci_ids)

    @api.depends('harga')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga = record.models_id.harga

    @api.depends('models_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.models_id.harga
