# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BillingServicesAmount1
from . import BillingServicesTax1

class BillingMethod2(base_types._BaseFieldType):

	__slots__ = ["_SvcChrgHstAmt", "_SvcTax", "_TaxId"]
	@property
	def SvcChrgHstAmt(self):
		return self._SvcChrgHstAmt

	@SvcChrgHstAmt.setter
	def SvcChrgHstAmt(self, value):
		self._SvcChrgHstAmt = value if value is not None else base_types.UninitialisedField(self, 'SvcChrgHstAmt', AmountAndDirection34, False)

	@SvcChrgHstAmt.deleter
	def SvcChrgHstAmt(self):
		del self._SvcChrgHstAmt
		self._SvcChrgHstAmt = base_types.UninitialisedField(self, 'SvcChrgHstAmt', AmountAndDirection34, False)

	@property
	def SvcTax(self):
		return self._SvcTax

	@SvcTax.setter
	def SvcTax(self, value):
		self._SvcTax = value if value is not None else base_types.UninitialisedField(self, 'SvcTax', BillingServicesAmount1, False)

	@SvcTax.deleter
	def SvcTax(self):
		del self._SvcTax
		self._SvcTax = base_types.UninitialisedField(self, 'SvcTax', BillingServicesAmount1, False)

	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if value is not None else base_types.UninitialisedField(self, 'TaxId', BillingServicesTax1, True)

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = base_types.UninitialisedField(self, 'TaxId', BillingServicesTax1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcChrgHstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTax', type=BillingServicesAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax1, min=1, max=3, mutex_group=None, array=True),
	))