# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancingAllowedSummary1
from . import InvoiceFinancingDetails1

class FinancingInformationAndStatus1(base_types._BaseFieldType):

	__slots__ = ["_FincgAllwdSummry", "_InvcFincgDtls"]
	@property
	def FincgAllwdSummry(self):
		return self._FincgAllwdSummry

	@FincgAllwdSummry.setter
	def FincgAllwdSummry(self, value):
		self._FincgAllwdSummry = value if value is not None else base_types.UninitialisedField(self, 'FincgAllwdSummry', FinancingAllowedSummary1, False)

	@FincgAllwdSummry.deleter
	def FincgAllwdSummry(self):
		del self._FincgAllwdSummry
		self._FincgAllwdSummry = base_types.UninitialisedField(self, 'FincgAllwdSummry', FinancingAllowedSummary1, False)

	@property
	def InvcFincgDtls(self):
		return self._InvcFincgDtls

	@InvcFincgDtls.setter
	def InvcFincgDtls(self, value):
		self._InvcFincgDtls = value if value is not None else base_types.UninitialisedField(self, 'InvcFincgDtls', InvoiceFinancingDetails1, True)

	@InvcFincgDtls.deleter
	def InvcFincgDtls(self):
		del self._InvcFincgDtls
		self._InvcFincgDtls = base_types.UninitialisedField(self, 'InvcFincgDtls', InvoiceFinancingDetails1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FincgAllwdSummry', type=FinancingAllowedSummary1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcFincgDtls', type=InvoiceFinancingDetails1, min=1, max=None, mutex_group=None, array=True),
	))