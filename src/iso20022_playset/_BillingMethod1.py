from . import base_types
from ._BillingServicesAmount2 import BillingServicesAmount2
from ._BillingServicesAmount1 import BillingServicesAmount1
from ._AmountAndDirection34 import AmountAndDirection34
from ._BillingServicesTax1 import BillingServicesTax1

class BillingMethod1(base_types._BaseFieldType):

	__slots__ = ["_SvcChrgHstAmt", "_TaxId", "_SvcTax", "_TtlChrg"]
	@property
	def SvcChrgHstAmt(self):
		return self._SvcChrgHstAmt

	@SvcChrgHstAmt.setter
	def SvcChrgHstAmt(self, value):
		self._SvcChrgHstAmt = value if type(value) != base_types.auto else self.make_default("SvcChrgHstAmt")

	@SvcChrgHstAmt.deleter
	def SvcChrgHstAmt(self):
		del self._SvcChrgHstAmt
		self._SvcChrgHstAmt = None

	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if type(value) != base_types.auto else self.make_default("TaxId")

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = None

	@property
	def SvcTax(self):
		return self._SvcTax

	@SvcTax.setter
	def SvcTax(self, value):
		self._SvcTax = value if type(value) != base_types.auto else self.make_default("SvcTax")

	@SvcTax.deleter
	def SvcTax(self):
		del self._SvcTax
		self._SvcTax = None

	@property
	def TtlChrg(self):
		return self._TtlChrg

	@TtlChrg.setter
	def TtlChrg(self, value):
		self._TtlChrg = value if type(value) != base_types.auto else self.make_default("TtlChrg")

	@TtlChrg.deleter
	def TtlChrg(self):
		del self._TtlChrg
		self._TtlChrg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcChrgHstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax1, min=1, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcTax', type=BillingServicesAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrg', type=BillingServicesAmount2, min=1, max=1, mutex_group=None, array=False),
	))

