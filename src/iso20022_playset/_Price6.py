from . import base_types
from ._PriceRateOrAmountChoice import PriceRateOrAmountChoice
from ._PriceSource2Code import PriceSource2Code
from ._TypeOfPrice13Code import TypeOfPrice13Code

class Price6(base_types._BaseFieldType):

	__slots__ = ["_RateOrAmt", "_Src", "_Tp"]
	@property
	def RateOrAmt(self):
		return self._RateOrAmt

	@RateOrAmt.setter
	def RateOrAmt(self, value):
		self._RateOrAmt = value if type(value) != base_types.auto else self.make_default("RateOrAmt")

	@RateOrAmt.deleter
	def RateOrAmt(self):
		del self._RateOrAmt
		self._RateOrAmt = None

	@property
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if type(value) != base_types.auto else self.make_default("Src")

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateOrAmt', type=PriceRateOrAmountChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Src', type=PriceSource2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfPrice13Code, min=1, max=1, mutex_group=None, array=False),
	))

