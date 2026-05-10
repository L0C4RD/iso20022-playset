from . import base_types
from .InputData6 import InputData6
from .ActionMessage11 import ActionMessage11

class DeviceInputRequest6(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_InptData"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	@property
	def InptData(self):
		return self._InptData

	@InptData.setter
	def InptData(self, value):
		self._InptData = value if type(value) != auto else self.make_default("InptData")

	@InptData.deleter
	def InptData(self):
		del self._InptData
		self._InptData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InptData', type=InputData6, min=1, max=1, mutex_group=None, array=False),
	))

