# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PercentageRangeBoundary1

class FromToPercentageRange1(base_types._BaseFieldType):

	__slots__ = ["_Fr", "_To"]
	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if value is not None else base_types.UninitialisedField(self, 'Fr', PercentageRangeBoundary1, False)

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = base_types.UninitialisedField(self, 'Fr', PercentageRangeBoundary1, False)

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if value is not None else base_types.UninitialisedField(self, 'To', PercentageRangeBoundary1, False)

	@To.deleter
	def To(self):
		del self._To
		self._To = base_types.UninitialisedField(self, 'To', PercentageRangeBoundary1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fr', type=PercentageRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=PercentageRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
	))