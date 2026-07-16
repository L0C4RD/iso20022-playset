# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import VolumeMetrics5

class PositionSetMetrics7(base_types._BaseFieldType):

	__slots__ = ["_VolMtrcs"]
	@property
	def VolMtrcs(self):
		return self._VolMtrcs

	@VolMtrcs.setter
	def VolMtrcs(self, value):
		self._VolMtrcs = value if value is not None else base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics5, False)

	@VolMtrcs.deleter
	def VolMtrcs(self):
		del self._VolMtrcs
		self._VolMtrcs = base_types.UninitialisedField(self, 'VolMtrcs', VolumeMetrics5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='VolMtrcs', type=VolumeMetrics5, min=1, max=1, mutex_group=None, array=False),
	))