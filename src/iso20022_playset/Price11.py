import base_types
import YieldedOrValueType2Choice
import PriceRateOrAmount1Choice

class Price11(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Val"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=YieldedOrValueType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmount1Choice, min=1, max=1, mutex_group=None, array=False),
	))

