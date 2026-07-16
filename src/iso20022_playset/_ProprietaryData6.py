# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SkipPayload

class ProprietaryData6(base_types._BaseFieldType):

	__slots__ = ["_Any"]
	@property
	def Any(self):
		return self._Any

	@Any.setter
	def Any(self, value):
		self._Any = value if value is not None else base_types.UninitialisedField(self, 'Any', SkipPayload, False)

	@Any.deleter
	def Any(self):
		del self._Any
		self._Any = base_types.UninitialisedField(self, 'Any', SkipPayload, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Any', type=SkipPayload, min=1, max=1, mutex_group=None, array=False),
	))