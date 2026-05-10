from . import base_types
from ._Max4Text import Max4Text
from ._Pagination1 import Pagination1
from ._PartyIdentification242Choice import PartyIdentification242Choice
from ._Max35Text import Max35Text
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime

class NettingCutOffReportData2(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_RptTp", "_RptSvcr", "_MsgId", "_MsgPgntn", "_NetSvcTp", "_NetSvcPtcptId", "_ActvtnDt"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def RptTp(self):
		return self._RptTp

	@RptTp.setter
	def RptTp(self, value):
		self._RptTp = value if type(value) != base_types.auto else self.make_default("RptTp")

	@RptTp.deleter
	def RptTp(self):
		del self._RptTp
		self._RptTp = None

	@property
	def RptSvcr(self):
		return self._RptSvcr

	@RptSvcr.setter
	def RptSvcr(self, value):
		self._RptSvcr = value if type(value) != base_types.auto else self.make_default("RptSvcr")

	@RptSvcr.deleter
	def RptSvcr(self):
		del self._RptSvcr
		self._RptSvcr = None

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
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != base_types.auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

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
	def ActvtnDt(self):
		return self._ActvtnDt

	@ActvtnDt.setter
	def ActvtnDt(self, value):
		self._ActvtnDt = value if type(value) != base_types.auto else self.make_default("ActvtnDt")

	@ActvtnDt.deleter
	def ActvtnDt(self):
		del self._ActvtnDt
		self._ActvtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTp', type=Max4Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSvcr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcPtcptId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActvtnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

