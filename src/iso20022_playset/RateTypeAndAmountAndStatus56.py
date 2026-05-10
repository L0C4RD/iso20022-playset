from . import base_types
from .RateType77Choice import RateType77Choice
from .RateStatus3Choice import RateStatus3Choice
from .ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount

class RateTypeAndAmountAndStatus56(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_RateSts", "_RateTp"]
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
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateSts', type=RateStatus3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType77Choice, min=1, max=1, mutex_group=None, array=False),
	))

