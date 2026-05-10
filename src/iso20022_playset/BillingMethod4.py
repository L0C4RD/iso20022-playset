from . import base_types
from .BillingServiceParameters2 import BillingServiceParameters2
from .TaxCalculation1 import TaxCalculation1

class BillingMethod4(base_types._BaseFieldType):

	__slots__ = ["_TaxClctn", "_SvcDtl"]
	@property
	def TaxClctn(self):
		return self._TaxClctn

	@TaxClctn.setter
	def TaxClctn(self, value):
		self._TaxClctn = value if type(value) != auto else self.make_default("TaxClctn")

	@TaxClctn.deleter
	def TaxClctn(self):
		del self._TaxClctn
		self._TaxClctn = None

	@property
	def SvcDtl(self):
		return self._SvcDtl

	@SvcDtl.setter
	def SvcDtl(self, value):
		self._SvcDtl = value if type(value) != auto else self.make_default("SvcDtl")

	@SvcDtl.deleter
	def SvcDtl(self):
		del self._SvcDtl
		self._SvcDtl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxClctn', type=TaxCalculation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcDtl', type=BillingServiceParameters2, min=1, max=None, mutex_group=None, array=True),
	))

