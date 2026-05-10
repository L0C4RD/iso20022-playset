import base_types
import Max35Text
import PartyIdentification242Choice
import ISODateTime
import Pagination1
import ISODate
import ISOTime

class NetReportData2(base_types._BaseFieldType):

	__slots__ = ["_NetgCutOffTm", "_MsgPgntn", "_RptTp", "_ValDt", "_MsgId", "_NetRptSvcr", "_NetSvcTp", "_RptDt", "_CreDtTm"]
	@property
	def NetgCutOffTm(self):
		return self._NetgCutOffTm

	@NetgCutOffTm.setter
	def NetgCutOffTm(self, value):
		self._NetgCutOffTm = value if type(value) != auto else self.make_default("NetgCutOffTm")

	@NetgCutOffTm.deleter
	def NetgCutOffTm(self):
		del self._NetgCutOffTm
		self._NetgCutOffTm = None

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	@property
	def RptTp(self):
		return self._RptTp

	@RptTp.setter
	def RptTp(self, value):
		self._RptTp = value if type(value) != auto else self.make_default("RptTp")

	@RptTp.deleter
	def RptTp(self):
		del self._RptTp
		self._RptTp = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def NetRptSvcr(self):
		return self._NetRptSvcr

	@NetRptSvcr.setter
	def NetRptSvcr(self, value):
		self._NetRptSvcr = value if type(value) != auto else self.make_default("NetRptSvcr")

	@NetRptSvcr.deleter
	def NetRptSvcr(self):
		del self._NetRptSvcr
		self._NetRptSvcr = None

	@property
	def NetSvcTp(self):
		return self._NetSvcTp

	@NetSvcTp.setter
	def NetSvcTp(self, value):
		self._NetSvcTp = value if type(value) != auto else self.make_default("NetSvcTp")

	@NetSvcTp.deleter
	def NetSvcTp(self):
		del self._NetSvcTp
		self._NetSvcTp = None

	@property
	def RptDt(self):
		return self._RptDt

	@RptDt.setter
	def RptDt(self, value):
		self._RptDt = value if type(value) != auto else self.make_default("RptDt")

	@RptDt.deleter
	def RptDt(self):
		del self._RptDt
		self._RptDt = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetgCutOffTm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetRptSvcr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

