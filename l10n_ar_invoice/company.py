# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class res_company(osv.osv):
    _inherit = "res.company"
    _columns = {
        'map_supplier_invoice_journals': fields.boolean(string="Map Supplier Invoices Journals", help='Suggest and Check journal on supplier invoices based in their responsability. Suggested to be used on Argentinian Companies'),
        'map_customer_invoice_journals': fields.boolean(string="Map Customer Invoices Journals", help='Suggest and Check journal on customer invoices based in their responsability. Suggested to be used on Argentinian Companies'),
        'responsability_id': fields.related('partner_id', 'responsability_id', relation='afip.responsability', type='many2one', string="Responsability",),
        'iibb': fields.related('partner_id', 'iibb', type='char', string='Gross Income', size=64,),
        'start_date': fields.related('partner_id', 'start_date', type='date', string='Start-up Date', size=64,),
    }

    _defaults = {
        'map_supplier_invoice_journals': True,
        'map_customer_invoice_journals': True,
    }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
