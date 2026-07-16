# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PositionSetTotal2

class PositionSetBuyerAndSeller2(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_Sellr"]
	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PositionSetTotal2, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PositionSetTotal2, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', PositionSetTotal2, False)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', PositionSetTotal2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Buyr', type=PositionSetTotal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PositionSetTotal2, min=0, max=1, mutex_group=None, array=False),
	))