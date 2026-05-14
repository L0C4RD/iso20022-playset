from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BillingFeeRecord1 import BillingFeeRecord1
from ._Max40Text import Max40Text
from ._PercentageRate import PercentageRate
from ._TaxExemption1 import TaxExemption1

class BillingTaxRecord2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ChrgsAndFees", "_Desc", "_Rate", "_TaxXmptn", "_TaxblAmt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def ChrgsAndFees(self):
		return self._ChrgsAndFees

	@ChrgsAndFees.setter
	def ChrgsAndFees(self, value):
		self._ChrgsAndFees = value if type(value) != base_types.auto else self.make_default("ChrgsAndFees")

	@ChrgsAndFees.deleter
	def ChrgsAndFees(self):
		del self._ChrgsAndFees
		self._ChrgsAndFees = None

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
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def TaxXmptn(self):
		return self._TaxXmptn

	@TaxXmptn.setter
	def TaxXmptn(self, value):
		self._TaxXmptn = value if type(value) != base_types.auto else self.make_default("TaxXmptn")

	@TaxXmptn.deleter
	def TaxXmptn(self):
		del self._TaxXmptn
		self._TaxXmptn = None

	@property
	def TaxblAmt(self):
		return self._TaxblAmt

	@TaxblAmt.setter
	def TaxblAmt(self, value):
		self._TaxblAmt = value if type(value) != base_types.auto else self.make_default("TaxblAmt")

	@TaxblAmt.deleter
	def TaxblAmt(self):
		del self._TaxblAmt
		self._TaxblAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAndFees', type=BillingFeeRecord1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxXmptn', type=TaxExemption1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

