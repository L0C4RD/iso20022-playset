# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PositionSetCollateralDimensions3 import PositionSetCollateralDimensions3
from ._PositionSetCollateralMetrics2 import PositionSetCollateralMetrics2

class PositionSet22(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='Dmnsns', type=PositionSetCollateralDimensions3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtrcs', type=PositionSetCollateralMetrics2, min=1, max=1, mutex_group=None, array=False),
	))