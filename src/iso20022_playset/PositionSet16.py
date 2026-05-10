from . import base_types
from .PositionSetDimensions14 import PositionSetDimensions14
from .PositionSetMetrics7 import PositionSetMetrics7

class PositionSet16(base_types._BaseFieldType):

	__slots__ = ["_Dmnsns", "_Mtrcs"]
	@property
	def Dmnsns(self):
		return self._Dmnsns

	@Dmnsns.setter
	def Dmnsns(self, value):
		self._Dmnsns = value if type(value) != base_types.auto else self.make_default("Dmnsns")

	@Dmnsns.deleter
	def Dmnsns(self):
		del self._Dmnsns
		self._Dmnsns = None

	@property
	def Mtrcs(self):
		return self._Mtrcs

	@Mtrcs.setter
	def Mtrcs(self, value):
		self._Mtrcs = value if type(value) != base_types.auto else self.make_default("Mtrcs")

	@Mtrcs.deleter
	def Mtrcs(self):
		del self._Mtrcs
		self._Mtrcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dmnsns', type=PositionSetDimensions14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtrcs', type=PositionSetMetrics7, min=1, max=1, mutex_group=None, array=False),
	))

