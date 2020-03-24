# -*- coding: utf-8 -*-
# (C) 2019 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResPartnerTitle(models.Model):
    _inherit = 'res.partner.title'

    name = fields.Char(data_mask="'title_' || id::text")
    shortcut = fields.Char(data_mask="NULL")