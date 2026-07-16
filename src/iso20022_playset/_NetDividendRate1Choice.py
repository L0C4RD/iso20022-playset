# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import NetDividendRate2
from . import RateValueType6FormatChoice

class NetDividendRate1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_NotSpcfdRate", "_RateTpAmt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdRate', RateValueType6FormatChoice, False)

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = base_types.UninitialisedField(self, 'NotSpcfdRate', RateValueType6FormatChoice, False)

	@property
	def RateTpAmt(self):
		return self._RateTpAmt

	@RateTpAmt.setter
	def RateTpAmt(self, value):
		self._RateTpAmt = value if value is not None else base_types.UninitialisedField(self, 'RateTpAmt', NetDividendRate2, False)

	@RateTpAmt.deleter
	def RateTpAmt(self):
		del self._RateTpAmt
		self._RateTpAmt = base_types.UninitialisedField(self, 'RateTpAmt', NetDividendRate2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType6FormatChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAmt', type=NetDividendRate2, min=0, max=1, mutex_group=1, array=False),
	))