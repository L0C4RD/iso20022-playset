# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import AmountAndForeignExchange1
from . import BillingTaxRecord2
from . import Max20AlphaNumericText
from . import Max350Text
from . import Number

class ServiceItemTotals10(base_types._BaseFieldType):

	__slots__ = ["_BalCcy", "_Desc", "_ItmTp", "_Qty", "_Tax", "_TtlInvcAmt", "_UnitPric"]
	@property
	def BalCcy(self):
		return self._BalCcy

	@BalCcy.setter
	def BalCcy(self, value):
		self._BalCcy = value if value is not None else base_types.UninitialisedField(self, 'BalCcy', ActiveCurrencyCode, False)

	@BalCcy.deleter
	def BalCcy(self):
		del self._BalCcy
		self._BalCcy = base_types.UninitialisedField(self, 'BalCcy', ActiveCurrencyCode, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max350Text, False)

	@property
	def ItmTp(self):
		return self._ItmTp

	@ItmTp.setter
	def ItmTp(self, value):
		self._ItmTp = value if value is not None else base_types.UninitialisedField(self, 'ItmTp', Max20AlphaNumericText, False)

	@ItmTp.deleter
	def ItmTp(self):
		del self._ItmTp
		self._ItmTp = base_types.UninitialisedField(self, 'ItmTp', Max20AlphaNumericText, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Number, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Number, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', BillingTaxRecord2, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', BillingTaxRecord2, True)

	@property
	def TtlInvcAmt(self):
		return self._TtlInvcAmt

	@TtlInvcAmt.setter
	def TtlInvcAmt(self, value):
		self._TtlInvcAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlInvcAmt', AmountAndForeignExchange1, False)

	@TtlInvcAmt.deleter
	def TtlInvcAmt(self):
		del self._TtlInvcAmt
		self._TtlInvcAmt = base_types.UninitialisedField(self, 'TtlInvcAmt', AmountAndForeignExchange1, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', ActiveCurrencyAndAmount, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmTp', type=Max20AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=BillingTaxRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlInvcAmt', type=AmountAndForeignExchange1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))