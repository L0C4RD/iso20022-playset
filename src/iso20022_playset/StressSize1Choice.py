from . import base_types
from .Absolute1 import Absolute1
from .BaseOneRate import BaseOneRate

class StressSize1Choice(base_types._BaseFieldType):

	__slots__ = ["_Abs", "_Rltv"]
	@property
	def Abs(self):
		return self._Abs

	@Abs.setter
	def Abs(self, value):
		self._Abs = value if type(value) != auto else self.make_default("Abs")

	@Abs.deleter
	def Abs(self):
		del self._Abs
		self._Abs = None

	@property
	def Rltv(self):
		return self._Rltv

	@Rltv.setter
	def Rltv(self, value):
		self._Rltv = value if type(value) != auto else self.make_default("Rltv")

	@Rltv.deleter
	def Rltv(self):
		del self._Rltv
		self._Rltv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Abs', type=Absolute1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rltv', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
	))

