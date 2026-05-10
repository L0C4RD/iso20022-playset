from . import base_types
from .PercentageRate import PercentageRate
from .Max2000Text import Max2000Text
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class UndertakingAmount1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_PlusTlrnce", "_AddtlInf"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def PlusTlrnce(self):
		return self._PlusTlrnce

	@PlusTlrnce.setter
	def PlusTlrnce(self, value):
		self._PlusTlrnce = value if type(value) != auto else self.make_default("PlusTlrnce")

	@PlusTlrnce.deleter
	def PlusTlrnce(self):
		del self._PlusTlrnce
		self._PlusTlrnce = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlusTlrnce', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

