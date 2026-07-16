# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import UTCOffset1

class ActivityReportSetUpRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ReqId", "_UTCOffset"]
	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if value is not None else base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@property
	def UTCOffset(self):
		return self._UTCOffset

	@UTCOffset.setter
	def UTCOffset(self, value):
		self._UTCOffset = value if value is not None else base_types.UninitialisedField(self, 'UTCOffset', UTCOffset1, False)

	@UTCOffset.deleter
	def UTCOffset(self):
		del self._UTCOffset
		self._UTCOffset = base_types.UninitialisedField(self, 'UTCOffset', UTCOffset1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UTCOffset', type=UTCOffset1, min=1, max=1, mutex_group=None, array=False),
	))