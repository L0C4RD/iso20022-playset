from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .RoundingMethod1Code import RoundingMethod1Code

class SegregatedIndependentAmountMargin1(base_types._BaseFieldType):

	__slots__ = ["_MinTrfAmt", "_RndgMtd", "_RndgAmt"]
	@property
	def MinTrfAmt(self):
		return self._MinTrfAmt

	@MinTrfAmt.setter
	def MinTrfAmt(self, value):
		self._MinTrfAmt = value if type(value) != base_types.auto else self.make_default("MinTrfAmt")

	@MinTrfAmt.deleter
	def MinTrfAmt(self):
		del self._MinTrfAmt
		self._MinTrfAmt = None

	@property
	def RndgMtd(self):
		return self._RndgMtd

	@RndgMtd.setter
	def RndgMtd(self, value):
		self._RndgMtd = value if type(value) != base_types.auto else self.make_default("RndgMtd")

	@RndgMtd.deleter
	def RndgMtd(self):
		del self._RndgMtd
		self._RndgMtd = None

	@property
	def RndgAmt(self):
		return self._RndgAmt

	@RndgAmt.setter
	def RndgAmt(self, value):
		self._RndgAmt = value if type(value) != base_types.auto else self.make_default("RndgAmt")

	@RndgAmt.deleter
	def RndgAmt(self):
		del self._RndgAmt
		self._RndgAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinTrfAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgMtd', type=RoundingMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

