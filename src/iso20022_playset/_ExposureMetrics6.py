# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PostedMarginOrCollateral4

class ExposureMetrics6(base_types._BaseFieldType):

	__slots__ = ["_PstdMrgnOrColl"]
	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if value is not None else base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral4, False)

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PstdMrgnOrColl', type=PostedMarginOrCollateral4, min=0, max=1, mutex_group=None, array=False),
	))