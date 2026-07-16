# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingServiceParameters2
from . import TaxCalculation1

class BillingMethod4(base_types._BaseFieldType):

	__slots__ = ["_SvcDtl", "_TaxClctn"]
	@property
	def SvcDtl(self):
		return self._SvcDtl

	@SvcDtl.setter
	def SvcDtl(self, value):
		self._SvcDtl = value if value is not None else base_types.UninitialisedField(self, 'SvcDtl', BillingServiceParameters2, True)

	@SvcDtl.deleter
	def SvcDtl(self):
		del self._SvcDtl
		self._SvcDtl = base_types.UninitialisedField(self, 'SvcDtl', BillingServiceParameters2, True)

	@property
	def TaxClctn(self):
		return self._TaxClctn

	@TaxClctn.setter
	def TaxClctn(self, value):
		self._TaxClctn = value if value is not None else base_types.UninitialisedField(self, 'TaxClctn', TaxCalculation1, False)

	@TaxClctn.deleter
	def TaxClctn(self):
		del self._TaxClctn
		self._TaxClctn = base_types.UninitialisedField(self, 'TaxClctn', TaxCalculation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcDtl', type=BillingServiceParameters2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxClctn', type=TaxCalculation1, min=1, max=1, mutex_group=None, array=False),
	))