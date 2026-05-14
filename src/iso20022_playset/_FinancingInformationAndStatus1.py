# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancingAllowedSummary1 import FinancingAllowedSummary1
from ._InvoiceFinancingDetails1 import InvoiceFinancingDetails1

class FinancingInformationAndStatus1(base_types._BaseFieldType):

	__slots__ = ["_FincgAllwdSummry", "_InvcFincgDtls"]
	@property
	def FincgAllwdSummry(self):
		return self._FincgAllwdSummry

	@FincgAllwdSummry.setter
	def FincgAllwdSummry(self, value):
		self._FincgAllwdSummry = value if type(value) != base_types.auto else self.make_default("FincgAllwdSummry")

	@FincgAllwdSummry.deleter
	def FincgAllwdSummry(self):
		del self._FincgAllwdSummry
		self._FincgAllwdSummry = None

	@property
	def InvcFincgDtls(self):
		return self._InvcFincgDtls

	@InvcFincgDtls.setter
	def InvcFincgDtls(self, value):
		self._InvcFincgDtls = value if type(value) != base_types.auto else self.make_default("InvcFincgDtls")

	@InvcFincgDtls.deleter
	def InvcFincgDtls(self):
		del self._InvcFincgDtls
		self._InvcFincgDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FincgAllwdSummry', type=FinancingAllowedSummary1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcFincgDtls', type=InvoiceFinancingDetails1, min=1, max=None, mutex_group=None, array=True),
	))