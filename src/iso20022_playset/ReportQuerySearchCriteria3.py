import base_types
import CashBalance14
import EventType1Choice
import DatePeriodSearch1Choice
import PartyIdentification136
import Max4AlphaNumericText
import DateTimePeriod1Choice
import Max35Text
import AccountIdentificationSearchCriteria2Choice

class ReportQuerySearchCriteria3(base_types._BaseFieldType):

	__slots__ = ["_MsgNmId", "_Evt", "_Bal", "_DtSch", "_SchdldTm", "_PtyId", "_RspnsblPtyId", "_AcctId", "_RptNm"]
	@property
	def MsgNmId(self):
		return self._MsgNmId

	@MsgNmId.setter
	def MsgNmId(self, value):
		self._MsgNmId = value if type(value) != auto else self.make_default("MsgNmId")

	@MsgNmId.deleter
	def MsgNmId(self):
		del self._MsgNmId
		self._MsgNmId = None

	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if type(value) != auto else self.make_default("Evt")

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def DtSch(self):
		return self._DtSch

	@DtSch.setter
	def DtSch(self, value):
		self._DtSch = value if type(value) != auto else self.make_default("DtSch")

	@DtSch.deleter
	def DtSch(self):
		del self._DtSch
		self._DtSch = None

	@property
	def SchdldTm(self):
		return self._SchdldTm

	@SchdldTm.setter
	def SchdldTm(self, value):
		self._SchdldTm = value if type(value) != auto else self.make_default("SchdldTm")

	@SchdldTm.deleter
	def SchdldTm(self):
		del self._SchdldTm
		self._SchdldTm = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if type(value) != auto else self.make_default("RspnsblPtyId")

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def RptNm(self):
		return self._RptNm

	@RptNm.setter
	def RptNm(self, value):
		self._RptNm = value if type(value) != auto else self.make_default("RptNm")

	@RptNm.deleter
	def RptNm(self):
		del self._RptNm
		self._RptNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Evt', type=EventType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=CashBalance14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtSch', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdldTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentificationSearchCriteria2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptNm', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
	))

