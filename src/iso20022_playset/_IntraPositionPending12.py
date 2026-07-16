# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventType56Choice
from . import DateAndDateTime2Choice
from . import FinancialInstrumentAttributes92
from . import FinancialInstrumentQuantity1Choice
from . import GenericIdentification37
from . import ISODateTime
from . import Linkages57
from . import Max350Text
from . import Max35Text
from . import PendingStatusAndReason4
from . import PriorityNumeric4Choice
from . import SecuritiesSubBalanceTypeAndQuantityBreakdown3
from . import SecurityIdentification19
from . import SupplementaryData1
from . import SystemPartyIdentification8

class IntraPositionPending12(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrTxId", "_AcctSvcrTxId", "_AckdStsTmStmp", "_BalFr", "_BalTo", "_CorpActnEvtId", "_CorpActnEvtTp", "_CreDtTm", "_FinInstrmAttrbts", "_FinInstrmId", "_InstrPrcgAddtlDtls", "_IntnddSttlmDt", "_Lnkgs", "_MktInfrstrctrTxId", "_MsgOrgtr", "_PoolId", "_PrcrTxId", "_Prty", "_SctiesSubBalId", "_SplmtryData", "_StsAndRsn", "_StsDt", "_SttlmQty"]
	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrTxId', Max35Text, False)

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = base_types.UninitialisedField(self, 'AcctOwnrTxId', Max35Text, False)

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@property
	def AckdStsTmStmp(self):
		return self._AckdStsTmStmp

	@AckdStsTmStmp.setter
	def AckdStsTmStmp(self, value):
		self._AckdStsTmStmp = value if value is not None else base_types.UninitialisedField(self, 'AckdStsTmStmp', ISODateTime, False)

	@AckdStsTmStmp.deleter
	def AckdStsTmStmp(self):
		del self._AckdStsTmStmp
		self._AckdStsTmStmp = base_types.UninitialisedField(self, 'AckdStsTmStmp', ISODateTime, False)

	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if value is not None else base_types.UninitialisedField(self, 'BalFr', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = base_types.UninitialisedField(self, 'BalFr', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if value is not None else base_types.UninitialisedField(self, 'BalTo', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = base_types.UninitialisedField(self, 'BalTo', SecuritiesSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtId', Max35Text, False)

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = base_types.UninitialisedField(self, 'CorpActnEvtId', Max35Text, False)

	@property
	def CorpActnEvtTp(self):
		return self._CorpActnEvtTp

	@CorpActnEvtTp.setter
	def CorpActnEvtTp(self, value):
		self._CorpActnEvtTp = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtTp', CorporateActionEventType56Choice, False)

	@CorpActnEvtTp.deleter
	def CorpActnEvtTp(self):
		del self._CorpActnEvtTp
		self._CorpActnEvtTp = base_types.UninitialisedField(self, 'CorpActnEvtTp', CorporateActionEventType56Choice, False)

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
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes92, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes92, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', Max350Text, False)

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', Max350Text, False)

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntnddSttlmDt', DateAndDateTime2Choice, False)

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = base_types.UninitialisedField(self, 'IntnddSttlmDt', DateAndDateTime2Choice, False)

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if value is not None else base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, False)

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, False)

	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if value is not None else base_types.UninitialisedField(self, 'PoolId', Max35Text, False)

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = base_types.UninitialisedField(self, 'PoolId', Max35Text, False)

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if value is not None else base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@property
	def SctiesSubBalId(self):
		return self._SctiesSubBalId

	@SctiesSubBalId.setter
	def SctiesSubBalId(self, value):
		self._SctiesSubBalId = value if value is not None else base_types.UninitialisedField(self, 'SctiesSubBalId', GenericIdentification37, False)

	@SctiesSubBalId.deleter
	def SctiesSubBalId(self):
		del self._SctiesSubBalId
		self._SctiesSubBalId = base_types.UninitialisedField(self, 'SctiesSubBalId', GenericIdentification37, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if value is not None else base_types.UninitialisedField(self, 'StsAndRsn', PendingStatusAndReason4, False)

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = base_types.UninitialisedField(self, 'StsAndRsn', PendingStatusAndReason4, False)

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if value is not None else base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if value is not None else base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity1Choice, False)

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = base_types.UninitialisedField(self, 'SttlmQty', FinancialInstrumentQuantity1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AckdStsTmStmp', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalFr', type=SecuritiesSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=SecuritiesSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtTp', type=CorporateActionEventType56Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes92, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalId', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsAndRsn', type=PendingStatusAndReason4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
	))