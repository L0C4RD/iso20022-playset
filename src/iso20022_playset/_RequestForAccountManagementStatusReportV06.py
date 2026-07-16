# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountManagementMessageReference5
from . import MessageIdentification1

class RequestForAccountManagementStatusReportV06(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_ReqDtls"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def ReqDtls(self):
		return self._ReqDtls

	@ReqDtls.setter
	def ReqDtls(self, value):
		self._ReqDtls = value if value is not None else base_types.UninitialisedField(self, 'ReqDtls', AccountManagementMessageReference5, False)

	@ReqDtls.deleter
	def ReqDtls(self):
		del self._ReqDtls
		self._ReqDtls = base_types.UninitialisedField(self, 'ReqDtls', AccountManagementMessageReference5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqDtls', type=AccountManagementMessageReference5, min=1, max=1, mutex_group=None, array=False),
	))