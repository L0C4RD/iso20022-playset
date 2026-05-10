from . import base_types
from .Number import Number
from .ActionMessage11 import ActionMessage11

class DevicePoweroffCardReaderRequest6(base_types._BaseFieldType):

	__slots__ = ["_PwrOffMaxWtgTm", "_DispOutpt"]
	@property
	def PwrOffMaxWtgTm(self):
		return self._PwrOffMaxWtgTm

	@PwrOffMaxWtgTm.setter
	def PwrOffMaxWtgTm(self, value):
		self._PwrOffMaxWtgTm = value if type(value) != base_types.auto else self.make_default("PwrOffMaxWtgTm")

	@PwrOffMaxWtgTm.deleter
	def PwrOffMaxWtgTm(self):
		del self._PwrOffMaxWtgTm
		self._PwrOffMaxWtgTm = None

	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != base_types.auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PwrOffMaxWtgTm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
	))

