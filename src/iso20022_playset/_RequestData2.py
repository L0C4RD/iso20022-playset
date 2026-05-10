from . import base_types
from ._Max35Text import Max35Text
from ._Max4Text import Max4Text
from ._PartyIdentification242Choice import PartyIdentification242Choice
from ._ISODate import ISODate

class RequestData2(base_types._BaseFieldType):

	__slots__ = ["_NetSvcTp", "_NetSvcPtcptId", "_ReqdActvtnDt", "_ReqTp", "_MsgId", "_ReqSvcr"]
	@property
	def NetSvcTp(self):
		return self._NetSvcTp

	@NetSvcTp.setter
	def NetSvcTp(self, value):
		self._NetSvcTp = value if type(value) != base_types.auto else self.make_default("NetSvcTp")

	@NetSvcTp.deleter
	def NetSvcTp(self):
		del self._NetSvcTp
		self._NetSvcTp = None

	@property
	def NetSvcPtcptId(self):
		return self._NetSvcPtcptId

	@NetSvcPtcptId.setter
	def NetSvcPtcptId(self, value):
		self._NetSvcPtcptId = value if type(value) != base_types.auto else self.make_default("NetSvcPtcptId")

	@NetSvcPtcptId.deleter
	def NetSvcPtcptId(self):
		del self._NetSvcPtcptId
		self._NetSvcPtcptId = None

	@property
	def ReqdActvtnDt(self):
		return self._ReqdActvtnDt

	@ReqdActvtnDt.setter
	def ReqdActvtnDt(self, value):
		self._ReqdActvtnDt = value if type(value) != base_types.auto else self.make_default("ReqdActvtnDt")

	@ReqdActvtnDt.deleter
	def ReqdActvtnDt(self):
		del self._ReqdActvtnDt
		self._ReqdActvtnDt = None

	@property
	def ReqTp(self):
		return self._ReqTp

	@ReqTp.setter
	def ReqTp(self, value):
		self._ReqTp = value if type(value) != base_types.auto else self.make_default("ReqTp")

	@ReqTp.deleter
	def ReqTp(self):
		del self._ReqTp
		self._ReqTp = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def ReqSvcr(self):
		return self._ReqSvcr

	@ReqSvcr.setter
	def ReqSvcr(self, value):
		self._ReqSvcr = value if type(value) != base_types.auto else self.make_default("ReqSvcr")

	@ReqSvcr.deleter
	def ReqSvcr(self):
		del self._ReqSvcr
		self._ReqSvcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetSvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcPtcptId', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdActvtnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqTp', type=Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqSvcr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
	))

