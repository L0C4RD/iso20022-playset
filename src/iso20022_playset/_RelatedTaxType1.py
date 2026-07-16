# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import TaxType3FormatChoice

class RelatedTaxType1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_TaxTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if value is not None else base_types.UninitialisedField(self, 'TaxTp', TaxType3FormatChoice, False)

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = base_types.UninitialisedField(self, 'TaxTp', TaxType3FormatChoice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTp', type=TaxType3FormatChoice, min=1, max=1, mutex_group=None, array=False),
	))