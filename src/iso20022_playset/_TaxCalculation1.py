# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import AmountAndDirection34
from . import BillingServicesAmount3
from . import BillingServicesTax3

class TaxCalculation1(base_types._BaseFieldType):

	__slots__ = ["_HstCcy", "_TaxId", "_TaxblSvcChrgConvs", "_TtlTax", "_TtlTaxblSvcChrgHstAmt"]
	@property
	def HstCcy(self):
		return self._HstCcy

	@HstCcy.setter
	def HstCcy(self, value):
		self._HstCcy = value if value is not None else base_types.UninitialisedField(self, 'HstCcy', ActiveOrHistoricCurrencyCode, False)

	@HstCcy.deleter
	def HstCcy(self):
		del self._HstCcy
		self._HstCcy = base_types.UninitialisedField(self, 'HstCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if value is not None else base_types.UninitialisedField(self, 'TaxId', BillingServicesTax3, True)

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = base_types.UninitialisedField(self, 'TaxId', BillingServicesTax3, True)

	@property
	def TaxblSvcChrgConvs(self):
		return self._TaxblSvcChrgConvs

	@TaxblSvcChrgConvs.setter
	def TaxblSvcChrgConvs(self, value):
		self._TaxblSvcChrgConvs = value if value is not None else base_types.UninitialisedField(self, 'TaxblSvcChrgConvs', BillingServicesAmount3, True)

	@TaxblSvcChrgConvs.deleter
	def TaxblSvcChrgConvs(self):
		del self._TaxblSvcChrgConvs
		self._TaxblSvcChrgConvs = base_types.UninitialisedField(self, 'TaxblSvcChrgConvs', BillingServicesAmount3, True)

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if value is not None else base_types.UninitialisedField(self, 'TtlTax', AmountAndDirection34, False)

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = base_types.UninitialisedField(self, 'TtlTax', AmountAndDirection34, False)

	@property
	def TtlTaxblSvcChrgHstAmt(self):
		return self._TtlTaxblSvcChrgHstAmt

	@TtlTaxblSvcChrgHstAmt.setter
	def TtlTaxblSvcChrgHstAmt(self, value):
		self._TtlTaxblSvcChrgHstAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlTaxblSvcChrgHstAmt', AmountAndDirection34, False)

	@TtlTaxblSvcChrgHstAmt.deleter
	def TtlTaxblSvcChrgHstAmt(self):
		del self._TtlTaxblSvcChrgHstAmt
		self._TtlTaxblSvcChrgHstAmt = base_types.UninitialisedField(self, 'TtlTaxblSvcChrgHstAmt', AmountAndDirection34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax3, min=1, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxblSvcChrgConvs', type=BillingServicesAmount3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlTax', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxblSvcChrgHstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))