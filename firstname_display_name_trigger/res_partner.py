# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Yannick Vaucher
#    Copyright 2013 Camptocamp SA
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
from openerp.osv import orm, fields


class ResPartner(orm.Model):
    _inherit = 'res.partner'

    def _display_name_compute(self, cr, uid, ids, name, args, context=None):
        return dict(self.name_get(cr, uid, ids, context=context))

    _display_name_store_triggers = {
        'res.partner': (lambda self,cr,uid,ids,context=None: self.search(cr, uid, [('id','child_of',ids)]),
                        ['parent_id', 'is_company', 'name', 'firstname', 'lastname'], 10)
    }

    # indirection to avoid passing a copy of the overridable method when declaring the function field
    _display_name = lambda self, *args, **kwargs: self._display_name_compute(*args, **kwargs)

    _columns = {
        # extra field to allow ORDER BY to match visible names
        'display_name': fields.function(_display_name, type='char', string='Name', store=_display_name_store_triggers),
        }
