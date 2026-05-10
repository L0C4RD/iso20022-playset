from . import base_types
import GrossDividendRate2
import RateValueType2FormatChoice
import ActiveCurrencyAndAmount

class GrossDividendRate1Choice(base_types._BaseFieldType):

	__slots__ = ["_NotSpcfdRate", "_Amt", "_RateTpAmt"]
	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if type(value) != auto else self.make_default("NotSpcfdRate")

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = None

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
	def RateTpAmt(self):
		return self._RateTpAmt

	@RateTpAmt.setter
	def RateTpAmt(self, value):
		self._RateTpAmt = value if type(value) != auto else self.make_default("RateTpAmt")

	@RateTpAmt.deleter
	def RateTpAmt(self):
		del self._RateTpAmt
		self._RateTpAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType2FormatChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAmt', type=GrossDividendRate2, min=0, max=1, mutex_group=1, array=False),
	))

