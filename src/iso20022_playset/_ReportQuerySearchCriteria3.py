# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentificationSearchCriteria2Choice
from . import CashBalance14
from . import DatePeriodSearch1Choice
from . import DateTimePeriod1Choice
from . import EventType1Choice
from . import Max35Text
from . import Max4AlphaNumericText
from . import PartyIdentification136

class ReportQuerySearchCriteria3(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_Bal", "_DtSch", "_Evt", "_MsgNmId", "_PtyId", "_RptNm", "_RspnsblPtyId", "_SchdldTm"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentificationSearchCriteria2Choice, True)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentificationSearchCriteria2Choice, True)

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', CashBalance14, True)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', CashBalance14, True)

	@property
	def DtSch(self):
		return self._DtSch

	@DtSch.setter
	def DtSch(self, value):
		self._DtSch = value if value is not None else base_types.UninitialisedField(self, 'DtSch', DatePeriodSearch1Choice, False)

	@DtSch.deleter
	def DtSch(self):
		del self._DtSch
		self._DtSch = base_types.UninitialisedField(self, 'DtSch', DatePeriodSearch1Choice, False)

	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if value is not None else base_types.UninitialisedField(self, 'Evt', EventType1Choice, False)

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = base_types.UninitialisedField(self, 'Evt', EventType1Choice, False)

	@property
	def MsgNmId(self):
		return self._MsgNmId

	@MsgNmId.setter
	def MsgNmId(self, value):
		self._MsgNmId = value if value is not None else base_types.UninitialisedField(self, 'MsgNmId', Max35Text, False)

	@MsgNmId.deleter
	def MsgNmId(self):
		del self._MsgNmId
		self._MsgNmId = base_types.UninitialisedField(self, 'MsgNmId', Max35Text, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@property
	def RptNm(self):
		return self._RptNm

	@RptNm.setter
	def RptNm(self, value):
		self._RptNm = value if value is not None else base_types.UninitialisedField(self, 'RptNm', Max4AlphaNumericText, False)

	@RptNm.deleter
	def RptNm(self):
		del self._RptNm
		self._RptNm = base_types.UninitialisedField(self, 'RptNm', Max4AlphaNumericText, False)

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

	@property
	def SchdldTm(self):
		return self._SchdldTm

	@SchdldTm.setter
	def SchdldTm(self, value):
		self._SchdldTm = value if value is not None else base_types.UninitialisedField(self, 'SchdldTm', DateTimePeriod1Choice, False)

	@SchdldTm.deleter
	def SchdldTm(self):
		del self._SchdldTm
		self._SchdldTm = base_types.UninitialisedField(self, 'SchdldTm', DateTimePeriod1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentificationSearchCriteria2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Bal', type=CashBalance14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtSch', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Evt', type=EventType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNm', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdldTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
	))