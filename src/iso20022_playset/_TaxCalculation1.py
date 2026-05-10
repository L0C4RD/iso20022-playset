from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._BillingServicesAmount3 import BillingServicesAmount3
from ._AmountAndDirection34 import AmountAndDirection34
from ._BillingServicesTax3 import BillingServicesTax3

class TaxCalculation1(base_types._BaseFieldType):

	__slots__ = ["_TaxId", "_TaxblSvcChrgConvs", "_HstCcy", "_TtlTaxblSvcChrgHstAmt", "_TtlTax"]
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
	def TaxblSvcChrgConvs(self):
		return self._TaxblSvcChrgConvs

	@TaxblSvcChrgConvs.setter
	def TaxblSvcChrgConvs(self, value):
		self._TaxblSvcChrgConvs = value if type(value) != base_types.auto else self.make_default("TaxblSvcChrgConvs")

	@TaxblSvcChrgConvs.deleter
	def TaxblSvcChrgConvs(self):
		del self._TaxblSvcChrgConvs
		self._TaxblSvcChrgConvs = None

	@property
	def HstCcy(self):
		return self._HstCcy

	@HstCcy.setter
	def HstCcy(self, value):
		self._HstCcy = value if type(value) != base_types.auto else self.make_default("HstCcy")

	@HstCcy.deleter
	def HstCcy(self):
		del self._HstCcy
		self._HstCcy = None

	@property
	def TtlTaxblSvcChrgHstAmt(self):
		return self._TtlTaxblSvcChrgHstAmt

	@TtlTaxblSvcChrgHstAmt.setter
	def TtlTaxblSvcChrgHstAmt(self, value):
		self._TtlTaxblSvcChrgHstAmt = value if type(value) != base_types.auto else self.make_default("TtlTaxblSvcChrgHstAmt")

	@TtlTaxblSvcChrgHstAmt.deleter
	def TtlTaxblSvcChrgHstAmt(self):
		del self._TtlTaxblSvcChrgHstAmt
		self._TtlTaxblSvcChrgHstAmt = None

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if type(value) != base_types.auto else self.make_default("TtlTax")

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax3, min=1, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblSvcChrgConvs', type=BillingServicesAmount3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxblSvcChrgHstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTax', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))

