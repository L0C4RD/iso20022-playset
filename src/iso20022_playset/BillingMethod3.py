from . import base_types
from .BillingServicesTax2 import BillingServicesTax2
from .AmountAndDirection34 import AmountAndDirection34

class BillingMethod3(base_types._BaseFieldType):

	__slots__ = ["_TaxId", "_SvcTaxPricAmt"]
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
	def SvcTaxPricAmt(self):
		return self._SvcTaxPricAmt

	@SvcTaxPricAmt.setter
	def SvcTaxPricAmt(self, value):
		self._SvcTaxPricAmt = value if type(value) != base_types.auto else self.make_default("SvcTaxPricAmt")

	@SvcTaxPricAmt.deleter
	def SvcTaxPricAmt(self):
		del self._SvcTaxPricAmt
		self._SvcTaxPricAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax2, min=1, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcTaxPricAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))

