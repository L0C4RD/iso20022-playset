# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BillingServicesTax2

class BillingMethod3(base_types._BaseFieldType):

	__slots__ = ["_SvcTaxPricAmt", "_TaxId"]
	@property
	def SvcTaxPricAmt(self):
		return self._SvcTaxPricAmt

	@SvcTaxPricAmt.setter
	def SvcTaxPricAmt(self, value):
		self._SvcTaxPricAmt = value if value is not None else base_types.UninitialisedField(self, 'SvcTaxPricAmt', AmountAndDirection34, False)

	@SvcTaxPricAmt.deleter
	def SvcTaxPricAmt(self):
		del self._SvcTaxPricAmt
		self._SvcTaxPricAmt = base_types.UninitialisedField(self, 'SvcTaxPricAmt', AmountAndDirection34, False)

	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if value is not None else base_types.UninitialisedField(self, 'TaxId', BillingServicesTax2, True)

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = base_types.UninitialisedField(self, 'TaxId', BillingServicesTax2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcTaxPricAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax2, min=1, max=3, mutex_group=None, array=True),
	))