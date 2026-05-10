from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .MarginType2Choice import MarginType2Choice
from .Amount3 import Amount3

class InitialMarginExposure1(base_types._BaseFieldType):

	__slots__ = ["_CoreInd", "_Tp", "_Amt"]
	@property
	def CoreInd(self):
		return self._CoreInd

	@CoreInd.setter
	def CoreInd(self, value):
		self._CoreInd = value if type(value) != base_types.auto else self.make_default("CoreInd")

	@CoreInd.deleter
	def CoreInd(self):
		del self._CoreInd
		self._CoreInd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CoreInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MarginType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=Amount3, min=1, max=1, mutex_group=None, array=False),
	))

