# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositionSetDimensions16
from . import PositionSetMetrics14

class PositionSet21(base_types._BaseFieldType):

	__slots__ = ["_Dmnsns", "_Mtrcs"]
	@property
	def Dmnsns(self):
		return self._Dmnsns

	@Dmnsns.setter
	def Dmnsns(self, value):
		self._Dmnsns = value if value is not None else base_types.UninitialisedField(self, 'Dmnsns', PositionSetDimensions16, False)

	@Dmnsns.deleter
	def Dmnsns(self):
		del self._Dmnsns
		self._Dmnsns = base_types.UninitialisedField(self, 'Dmnsns', PositionSetDimensions16, False)

	@property
	def Mtrcs(self):
		return self._Mtrcs

	@Mtrcs.setter
	def Mtrcs(self, value):
		self._Mtrcs = value if value is not None else base_types.UninitialisedField(self, 'Mtrcs', PositionSetMetrics14, False)

	@Mtrcs.deleter
	def Mtrcs(self):
		del self._Mtrcs
		self._Mtrcs = base_types.UninitialisedField(self, 'Mtrcs', PositionSetMetrics14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dmnsns', type=PositionSetDimensions16, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtrcs', type=PositionSetMetrics14, min=1, max=1, mutex_group=None, array=False),
	))