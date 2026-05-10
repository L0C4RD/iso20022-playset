import base_types
import Max4Text
import CurrencyAndAmount
import PercentageRate

class EarlyPaymentsVAT1(base_types._BaseFieldType):

	__slots__ = ["_DscntTaxTp", "_DscntTaxAmt", "_TaxRate"]
	@property
	def DscntTaxTp(self):
		return self._DscntTaxTp

	@DscntTaxTp.setter
	def DscntTaxTp(self, value):
		self._DscntTaxTp = value if type(value) != auto else self.make_default("DscntTaxTp")

	@DscntTaxTp.deleter
	def DscntTaxTp(self):
		del self._DscntTaxTp
		self._DscntTaxTp = None

	@property
	def DscntTaxAmt(self):
		return self._DscntTaxAmt

	@DscntTaxAmt.setter
	def DscntTaxAmt(self, value):
		self._DscntTaxAmt = value if type(value) != auto else self.make_default("DscntTaxAmt")

	@DscntTaxAmt.deleter
	def DscntTaxAmt(self):
		del self._DscntTaxAmt
		self._DscntTaxAmt = None

	@property
	def TaxRate(self):
		return self._TaxRate

	@TaxRate.setter
	def TaxRate(self, value):
		self._TaxRate = value if type(value) != auto else self.make_default("TaxRate")

	@TaxRate.deleter
	def TaxRate(self):
		del self._TaxRate
		self._TaxRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DscntTaxTp', type=Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntTaxAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))

