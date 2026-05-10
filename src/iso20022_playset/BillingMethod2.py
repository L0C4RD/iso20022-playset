from . import base_types
import BillingServicesAmount1
import BillingServicesTax1
import AmountAndDirection34

class BillingMethod2(base_types._BaseFieldType):

	__slots__ = ["_SvcTax", "_TaxId", "_SvcChrgHstAmt"]
	@property
	def SvcTax(self):
		return self._SvcTax

	@SvcTax.setter
	def SvcTax(self, value):
		self._SvcTax = value if type(value) != auto else self.make_default("SvcTax")

	@SvcTax.deleter
	def SvcTax(self):
		del self._SvcTax
		self._SvcTax = None

	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if type(value) != auto else self.make_default("TaxId")

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = None

	@property
	def SvcChrgHstAmt(self):
		return self._SvcChrgHstAmt

	@SvcChrgHstAmt.setter
	def SvcChrgHstAmt(self, value):
		self._SvcChrgHstAmt = value if type(value) != auto else self.make_default("SvcChrgHstAmt")

	@SvcChrgHstAmt.deleter
	def SvcChrgHstAmt(self):
		del self._SvcChrgHstAmt
		self._SvcChrgHstAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcTax', type=BillingServicesAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax1, min=1, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcChrgHstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))

