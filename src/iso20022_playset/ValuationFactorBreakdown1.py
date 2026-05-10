from . import base_types
from .BaseOneRate import BaseOneRate

class ValuationFactorBreakdown1(base_types._BaseFieldType):

	__slots__ = ["_InfltnFctr", "_PoolFctr", "_ValtnFctr", "_Hrcut"]
	@property
	def InfltnFctr(self):
		return self._InfltnFctr

	@InfltnFctr.setter
	def InfltnFctr(self, value):
		self._InfltnFctr = value if type(value) != auto else self.make_default("InfltnFctr")

	@InfltnFctr.deleter
	def InfltnFctr(self):
		del self._InfltnFctr
		self._InfltnFctr = None

	@property
	def PoolFctr(self):
		return self._PoolFctr

	@PoolFctr.setter
	def PoolFctr(self, value):
		self._PoolFctr = value if type(value) != auto else self.make_default("PoolFctr")

	@PoolFctr.deleter
	def PoolFctr(self):
		del self._PoolFctr
		self._PoolFctr = None

	@property
	def ValtnFctr(self):
		return self._ValtnFctr

	@ValtnFctr.setter
	def ValtnFctr(self, value):
		self._ValtnFctr = value if type(value) != auto else self.make_default("ValtnFctr")

	@ValtnFctr.deleter
	def ValtnFctr(self):
		del self._ValtnFctr
		self._ValtnFctr = None

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfltnFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFctr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

