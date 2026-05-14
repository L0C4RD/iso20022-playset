# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection34 import AmountAndDirection34
from ._BillingServicesAmount1 import BillingServicesAmount1
from ._BillingServicesTax1 import BillingServicesTax1

class BillingMethod2(base_types._BaseFieldType):

	__slots__ = ["_SvcChrgHstAmt", "_SvcTax", "_TaxId"]
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
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if type(value) != base_types.auto else self.make_default("TaxId")

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcChrgHstAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcTax', type=BillingServicesAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxId', type=BillingServicesTax1, min=1, max=3, mutex_group=None, array=True),
	))