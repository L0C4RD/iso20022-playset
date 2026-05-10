import base_types
import PositionSetDimensions12
import PositionSetMetrics11

class PositionSet19(base_types._BaseFieldType):

	__slots__ = ["_Mtrcs", "_Dmnsns"]
	@property
	def Mtrcs(self):
		return self._Mtrcs

	@Mtrcs.setter
	def Mtrcs(self, value):
		self._Mtrcs = value if type(value) != auto else self.make_default("Mtrcs")

	@Mtrcs.deleter
	def Mtrcs(self):
		del self._Mtrcs
		self._Mtrcs = None

	@property
	def Dmnsns(self):
		return self._Dmnsns

	@Dmnsns.setter
	def Dmnsns(self, value):
		self._Dmnsns = value if type(value) != auto else self.make_default("Dmnsns")

	@Dmnsns.deleter
	def Dmnsns(self):
		del self._Dmnsns
		self._Dmnsns = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtrcs', type=PositionSetMetrics11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dmnsns', type=PositionSetDimensions12, min=1, max=1, mutex_group=None, array=False),
	))

