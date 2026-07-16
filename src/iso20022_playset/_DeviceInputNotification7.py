# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import Max35Text

class DeviceInputNotification7(base_types._BaseFieldType):

	__slots__ = ["_OutptCntt", "_XchgId"]
	@property
	def OutptCntt(self):
		return self._OutptCntt

	@OutptCntt.setter
	def OutptCntt(self, value):
		self._OutptCntt = value if value is not None else base_types.UninitialisedField(self, 'OutptCntt', ActionMessage12, False)

	@OutptCntt.deleter
	def OutptCntt(self):
		del self._OutptCntt
		self._OutptCntt = base_types.UninitialisedField(self, 'OutptCntt', ActionMessage12, False)

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if value is not None else base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OutptCntt', type=ActionMessage12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))