# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text
from . import OriginalBusinessQuery1
from . import Pagination1
from . import RequestType4Choice

class MessageHeader8(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_MsgId", "_MsgPgntn", "_OrgnlBizQry", "_QryNm", "_ReqTp"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if value is not None else base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = base_types.UninitialisedField(self, 'MsgPgntn', Pagination1, False)

	@property
	def OrgnlBizQry(self):
		return self._OrgnlBizQry

	@OrgnlBizQry.setter
	def OrgnlBizQry(self, value):
		self._OrgnlBizQry = value if value is not None else base_types.UninitialisedField(self, 'OrgnlBizQry', OriginalBusinessQuery1, False)

	@OrgnlBizQry.deleter
	def OrgnlBizQry(self):
		del self._OrgnlBizQry
		self._OrgnlBizQry = base_types.UninitialisedField(self, 'OrgnlBizQry', OriginalBusinessQuery1, False)

	@property
	def QryNm(self):
		return self._QryNm

	@QryNm.setter
	def QryNm(self, value):
		self._QryNm = value if value is not None else base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	@QryNm.deleter
	def QryNm(self):
		del self._QryNm
		self._QryNm = base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	@property
	def ReqTp(self):
		return self._ReqTp

	@ReqTp.setter
	def ReqTp(self, value):
		self._ReqTp = value if value is not None else base_types.UninitialisedField(self, 'ReqTp', RequestType4Choice, False)

	@ReqTp.deleter
	def ReqTp(self):
		del self._ReqTp
		self._ReqTp = base_types.UninitialisedField(self, 'ReqTp', RequestType4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizQry', type=OriginalBusinessQuery1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqTp', type=RequestType4Choice, min=0, max=1, mutex_group=None, array=False),
	))