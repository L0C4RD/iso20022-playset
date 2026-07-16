# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISODateTime
from . import Max35Text
from . import Max4Text
from . import Pagination1
from . import PartyIdentification242Choice

class NettingCutOffReportData2(base_types._BaseFieldType):

	__slots__ = ["_ActvtnDt", "_CreDtTm", "_MsgId", "_MsgPgntn", "_NetSvcPtcptId", "_NetSvcTp", "_RptSvcr", "_RptTp"]
	@property
	def ActvtnDt(self):
		return self._ActvtnDt

	@ActvtnDt.setter
	def ActvtnDt(self, value):
		self._ActvtnDt = value if value is not None else base_types.UninitialisedField(self, 'ActvtnDt', ISODate, False)

	@ActvtnDt.deleter
	def ActvtnDt(self):
		del self._ActvtnDt
		self._ActvtnDt = base_types.UninitialisedField(self, 'ActvtnDt', ISODate, False)

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
	def RptSvcr(self):
		return self._RptSvcr

	@RptSvcr.setter
	def RptSvcr(self, value):
		self._RptSvcr = value if value is not None else base_types.UninitialisedField(self, 'RptSvcr', PartyIdentification242Choice, False)

	@RptSvcr.deleter
	def RptSvcr(self):
		del self._RptSvcr
		self._RptSvcr = base_types.UninitialisedField(self, 'RptSvcr', PartyIdentification242Choice, False)

	@property
	def RptTp(self):
		return self._RptTp

	@RptTp.setter
	def RptTp(self, value):
		self._RptTp = value if value is not None else base_types.UninitialisedField(self, 'RptTp', Max4Text, False)

	@RptTp.deleter
	def RptTp(self):
		del self._RptTp
		self._RptTp = base_types.UninitialisedField(self, 'RptTp', Max4Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcPtcptId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetSvcTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSvcr', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptTp', type=Max4Text, min=1, max=1, mutex_group=None, array=False),
	))