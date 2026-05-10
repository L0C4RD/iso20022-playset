from . import base_types
from .PlusOrMinusIndicator import PlusOrMinusIndicator
from .AmountOrRate1Choice import AmountOrRate1Choice

class SpreadRate1(base_types._BaseFieldType):

	__slots__ = ["_Sgn", "_RateOrAmt"]
	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != base_types.auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateOrAmt', type=AmountOrRate1Choice, min=1, max=1, mutex_group=None, array=False),
	))

