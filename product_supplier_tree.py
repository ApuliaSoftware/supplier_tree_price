# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2014 giuseppe (<g.dalo@cgsoftware.it>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from osv import fields, osv
from tools.translate import _


class pricelist_partnerinfo(osv.osv):

	_inherit = "pricelist.partnerinfo"
	_columns = {'partner_id': fields.related('suppinfo_id', 'name',
				 string="Supplier", type='many2one', relation='res.partner', store=True),
				'product_id': fields.related('suppinfo_id', 'product_id',
				 string="product", type='many2one', relation='product.product', store=True),
				'product_name': fields.related('suppinfo_id', 'product_name',
				 string="Product name Supplier", type='char', store=True, select=True),
				'product_code': fields.related('suppinfo_id', 'product_code',
				 string="Product code Supplier", type='char', store=True, select=True),				 				 
			   }

pricelist_partnerinfo()
