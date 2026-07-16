# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositionSetDimensions14
from . import PositionSetMetrics7

class PositionSet16(base_types._BaseFieldType):

	__slots__ = ["_Dmnsns", "_Mtrcs"]
	@property
	def Dmnsns(self):
		return self._Dmnsns

	@Dmnsns.setter
	def Dmnsns(self, value):
		self._Dmnsns = value if value is not None else base_types.UninitialisedField(self, 'Dmnsns', PositionSetDimensions14, False)

	@Dmnsns.deleter
	def Dmnsns(self):
		del self._Dmnsns
		self._Dmnsns = base_types.UninitialisedField(self, 'Dmnsns', PositionSetDimensions14, False)

	@property
	def Mtrcs(self):
		return self._Mtrcs

	@Mtrcs.setter
	def Mtrcs(self, value):
		self._Mtrcs = value if value is not None else base_types.UninitialisedField(self, 'Mtrcs', PositionSetMetrics7, False)

	@Mtrcs.deleter
	def Mtrcs(self):
		del self._Mtrcs
		self._Mtrcs = base_types.UninitialisedField(self, 'Mtrcs', PositionSetMetrics7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dmnsns', type=PositionSetDimensions14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtrcs', type=PositionSetMetrics7, min=1, max=1, mutex_group=None, array=False),
	))