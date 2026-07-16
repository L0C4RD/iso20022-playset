# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import DecimalNumber
from . import Max35Text
from . import Max40Text

class BillingServicesTax3(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Nb", "_Rate", "_TtlTaxAmt"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max40Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max40Text, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', DecimalNumber, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', DecimalNumber, False)

	@property
	def TtlTaxAmt(self):
		return self._TtlTaxAmt

	@TtlTaxAmt.setter
	def TtlTaxAmt(self, value):
		self._TtlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlTaxAmt', AmountAndDirection34, False)

	@TtlTaxAmt.deleter
	def TtlTaxAmt(self):
		del self._TtlTaxAmt
		self._TtlTaxAmt = base_types.UninitialisedField(self, 'TtlTaxAmt', AmountAndDirection34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))