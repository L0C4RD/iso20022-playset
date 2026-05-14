from . import base_types
from ._ActionMessage12 import ActionMessage12
from ._Max35Text import Max35Text

class DeviceInputNotification7(base_types._BaseFieldType):

	__slots__ = ["_OutptCntt", "_XchgId"]
	@property
	def OutptCntt(self):
		return self._OutptCntt

	@OutptCntt.setter
	def OutptCntt(self, value):
		self._OutptCntt = value if type(value) != base_types.auto else self.make_default("OutptCntt")

	@OutptCntt.deleter
	def OutptCntt(self):
		del self._OutptCntt
		self._OutptCntt = None

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if type(value) != base_types.auto else self.make_default("XchgId")

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OutptCntt', type=ActionMessage12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

