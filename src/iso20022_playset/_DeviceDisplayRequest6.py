from . import base_types
from ._ActionMessage11 import ActionMessage11

class DeviceDisplayRequest6(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt"]
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
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=1, max=None, mutex_group=None, array=True),
	))

