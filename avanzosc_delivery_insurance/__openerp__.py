
# -*- encoding: utf-8 -*-
##############################################################################
#
#    Daniel Campos (danielcampos@avanzosc.es) Date: 24/10/2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################


{
    "name": "Avanzosc delivery insurance",
    "version": "1.0",
    "description": """
                This module adds:
                - Insurance cost to delivery chart.
                    """,
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": ["delivery"],
    "category": "Generic Modules",
    "init_xml": [],
    "demo_xml": [],
    "update_xml": ["views/delivery_carryer_view.xml"],
    "active": False,
    "installable": True
}