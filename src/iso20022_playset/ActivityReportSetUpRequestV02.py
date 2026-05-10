from . import base_types
from .MessageIdentification1 import MessageIdentification1
from .UTCOffset1 import UTCOffset1

class ActivityReportSetUpRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ReqId", "_UTCOffset"]
	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

	@property
	def UTCOffset(self):
		return self._UTCOffset

	@UTCOffset.setter
	def UTCOffset(self, value):
		self._UTCOffset = value if type(value) != auto else self.make_default("UTCOffset")

	@UTCOffset.deleter
	def UTCOffset(self):
		del self._UTCOffset
		self._UTCOffset = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UTCOffset', type=UTCOffset1, min=1, max=1, mutex_group=None, array=False),
	))

