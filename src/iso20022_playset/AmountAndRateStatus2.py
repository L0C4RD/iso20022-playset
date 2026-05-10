from . import base_types
import RestrictedFINActiveCurrencyAnd13DecimalAmount
import RateStatus1Code

class AmountAndRateStatus2(base_types._BaseFieldType):

	__slots__ = ["_RateSts", "_Amt"]
	@property
	def RateSts(self):
		return self._RateSts

	@RateSts.setter
	def RateSts(self, value):
		self._RateSts = value if type(value) != auto else self.make_default("RateSts")

	@RateSts.deleter
	def RateSts(self):
		del self._RateSts
		self._RateSts = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateSts', type=RateStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))

