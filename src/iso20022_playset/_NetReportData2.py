# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISODateTime
from . import ISOTime
from . import Max35Text
from . import Pagination1
from . import PartyIdentification242Choice

class NetReportData2(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_MsgId", "_MsgPgntn", "_NetRptSvcr", "_NetSvcTp", "_NetgCutOffTm", "_RptDt", "_RptTp", "_ValDt"]
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
	def NetRptSvcr(self):
		return self._NetRptSvcr

	@NetRptSvcr.setter
	def NetRptSvcr(self, value):
		self._NetRptSvcr = value if value is not None else base_types.UninitialisedField(self, 'NetRptSvcr', PartyIdentification242Choice, False)

	@NetRptSvcr.deleter
	def NetRptSvcr(self):
		del self._NetRptSvcr
		self._NetRptSvcr = base_types.UninitialisedField(self, 'NetRptSvcr', PartyIdentification242Choice, False)

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
	def NetgCutOffTm(self):
		return self._NetgCutOffTm

	@NetgCutOffTm.setter
	def NetgCutOffTm(self, value):
		self._NetgCutOffTm = value if value is not None else base_types.UninitialisedField(self, 'NetgCutOffTm', ISOTime, False)

	@NetgCutOffTm.deleter
	def NetgCutOffTm(self):
		del self._NetgCutOffTm
		self._NetgCutOffTm = base_types.UninitialisedField(self, 'NetgCutOffTm', ISOTime, False)

	@property
	def RptDt(self):
		return self._RptDt

	@RptDt.setter
	def RptDt(self, value):
		self._RptDt = value if value is not None else base_types.UninitialisedField(self, 'RptDt', ISODate, False)

	@RptDt.deleter
	def RptDt(self):
		del self._RptDt
		self._RptDt = base_types.UninitialisedField(self, 'RptDt', ISODate, False)

	@property
	def RptTp(self):
		return self._RptTp

	@RptTp.setter
	def RptTp(self, value):
		self._RptTp = value if value is not None else base_types.UninitialisedField(self, 'RptTp', Max35Text, False)

	@RptTp.deleter
	def RptTp(self):
		del self._RptTp
		self._RptTp = base_types.UninitialisedField(self, 'RptTp', Max35Text, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetRptSvcr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetgCutOffTm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))