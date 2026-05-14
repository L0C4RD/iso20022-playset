from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AmountAndForeignExchange1 import AmountAndForeignExchange1
from ._BillingTaxRecord2 import BillingTaxRecord2
from ._CreditDebitCode import CreditDebitCode
from ._Max20AlphaNumericText import Max20AlphaNumericText
from ._Max350Text import Max350Text
from ._Number import Number

class ServiceItemTotals11(base_types._BaseFieldType):

	__slots__ = ["_BalCcy", "_CdtDbtInd", "_Desc", "_ItmTp", "_Qty", "_Tax", "_TtlInvcAmt", "_UnitPric"]
	@property
	def BalCcy(self):
		return self._BalCcy

	@BalCcy.setter
	def BalCcy(self, value):
		self._BalCcy = value if type(value) != base_types.auto else self.make_default("BalCcy")

	@BalCcy.deleter
	def BalCcy(self):
		del self._BalCcy
		self._BalCcy = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def ItmTp(self):
		return self._ItmTp

	@ItmTp.setter
	def ItmTp(self, value):
		self._ItmTp = value if type(value) != base_types.auto else self.make_default("ItmTp")

	@ItmTp.deleter
	def ItmTp(self):
		del self._ItmTp
		self._ItmTp = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def TtlInvcAmt(self):
		return self._TtlInvcAmt

	@TtlInvcAmt.setter
	def TtlInvcAmt(self, value):
		self._TtlInvcAmt = value if type(value) != base_types.auto else self.make_default("TtlInvcAmt")

	@TtlInvcAmt.deleter
	def TtlInvcAmt(self):
		del self._TtlInvcAmt
		self._TtlInvcAmt = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmTp', type=Max20AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=BillingTaxRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlInvcAmt', type=AmountAndForeignExchange1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

