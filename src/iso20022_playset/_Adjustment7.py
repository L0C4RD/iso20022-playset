from . import base_types
from ._AmountOrPercentage2Choice import AmountOrPercentage2Choice
from ._AdjustmentType1Choice import AdjustmentType1Choice
from ._AdjustmentDirection1Code import AdjustmentDirection1Code

class Adjustment7(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_AmtOrPctg", "_Drctn"]
	@property
	def AmtOrPctg(self):
		return self._AmtOrPctg

	@AmtOrPctg.setter
	def AmtOrPctg(self, value):
		self._AmtOrPctg = value if type(value) != base_types.auto else self.make_default("AmtOrPctg")

	@AmtOrPctg.deleter
	def AmtOrPctg(self):
		del self._AmtOrPctg
		self._AmtOrPctg = None

	@property
	def Drctn(self):
		return self._Drctn

	@Drctn.setter
	def Drctn(self, value):
		self._Drctn = value if type(value) != base_types.auto else self.make_default("Drctn")

	@Drctn.deleter
	def Drctn(self):
		del self._Drctn
		self._Drctn = None

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
		base_types.FieldEntry(name='AmtOrPctg', type=AmountOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drctn', type=AdjustmentDirection1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AdjustmentType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

