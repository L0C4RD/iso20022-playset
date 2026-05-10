from . import base_types
from ._RateStatus4Choice import RateStatus4Choice
from ._RateType83Choice import RateType83Choice
from ._RestrictedFINActiveCurrencyAnd13DecimalAmount import RestrictedFINActiveCurrencyAnd13DecimalAmount

class RateTypeAndAmountAndStatus62(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_RateSts", "_RateTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def RateSts(self):
		return self._RateSts

	@RateSts.setter
	def RateSts(self, value):
		self._RateSts = value if type(value) != base_types.auto else self.make_default("RateSts")

	@RateSts.deleter
	def RateSts(self):
		del self._RateSts
		self._RateSts = None

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateSts', type=RateStatus4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=RateType83Choice, min=1, max=1, mutex_group=None, array=False),
	))

