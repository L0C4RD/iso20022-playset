# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text
from . import Max4Text
from . import PartyIdentification242Choice

class RequestData2(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_NetSvcPtcptId", "_NetSvcTp", "_ReqSvcr", "_ReqTp", "_ReqdActvtnDt"]
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
	def NetSvcPtcptId(self):
		return self._NetSvcPtcptId

	@NetSvcPtcptId.setter
	def NetSvcPtcptId(self, value):
		self._NetSvcPtcptId = value if value is not None else base_types.UninitialisedField(self, 'NetSvcPtcptId', PartyIdentification242Choice, False)

	@NetSvcPtcptId.deleter
	def NetSvcPtcptId(self):
		del self._NetSvcPtcptId
		self._NetSvcPtcptId = base_types.UninitialisedField(self, 'NetSvcPtcptId', PartyIdentification242Choice, False)

	@property
	def NetSvcTp(self):
		return self._NetSvcTp

	@NetSvcTp.setter
	def NetSvcTp(self, value):
		self._NetSvcTp = value if value is not None else base_types.UninitialisedField(self, 'NetSvcTp', Max35Text, False)

	@NetSvcTp.deleter
	def NetSvcTp(self):
		del self._NetSvcTp
		self._NetSvcTp = base_types.UninitialisedField(self, 'NetSvcTp', Max35Text, False)

	@property
	def ReqSvcr(self):
		return self._ReqSvcr

	@ReqSvcr.setter
	def ReqSvcr(self, value):
		self._ReqSvcr = value if value is not None else base_types.UninitialisedField(self, 'ReqSvcr', PartyIdentification242Choice, False)

	@ReqSvcr.deleter
	def ReqSvcr(self):
		del self._ReqSvcr
		self._ReqSvcr = base_types.UninitialisedField(self, 'ReqSvcr', PartyIdentification242Choice, False)

	@property
	def ReqTp(self):
		return self._ReqTp

	@ReqTp.setter
	def ReqTp(self, value):
		self._ReqTp = value if value is not None else base_types.UninitialisedField(self, 'ReqTp', Max4Text, False)

	@ReqTp.deleter
	def ReqTp(self):
		del self._ReqTp
		self._ReqTp = base_types.UninitialisedField(self, 'ReqTp', Max4Text, False)

	@property
	def ReqdActvtnDt(self):
		return self._ReqdActvtnDt

	@ReqdActvtnDt.setter
	def ReqdActvtnDt(self, value):
		self._ReqdActvtnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdActvtnDt', ISODate, False)

	@ReqdActvtnDt.deleter
	def ReqdActvtnDt(self):
		del self._ReqdActvtnDt
		self._ReqdActvtnDt = base_types.UninitialisedField(self, 'ReqdActvtnDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcPtcptId', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqSvcr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqTp', type=Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdActvtnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))