# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData2
from . import AdditionalFee3
from . import Amount17
from . import ContentInformationType41
from . import Exact12Text
from . import Exact15Text
from . import FinancialInstitution9
from . import Header71
from . import ISO8583MessageReasonCode
from . import ISODateTime
from . import Jurisdiction2
from . import Max1000Text
from . import Max12NumericText
from . import Max256Text
from . import Max35Text
from . import PartyIdentification285
from . import PartyIdentification286
from . import ProgrammeMode5
from . import ProtectedData2
from . import Reconciliation4
from . import SettlementCategoryTotal2
from . import SettlementCategoryTotal3
from . import SettlementReportType1Code
from . import SettlementService6
from . import SupplementaryData1

class SettlementReportingInitiationV03(base_types._BaseFieldType):

	__slots__ = ["_AcqrrSttlmTtls", "_AddtlData", "_AddtlFee", "_AltrnMsgRsn", "_Dstn", "_FI", "_FndsTrfAmt", "_Hdr", "_IssrSttlmTtls", "_Jursdctn", "_LifeCyclId", "_MsgRsn", "_Orgtr", "_OthrInstn", "_OthrSttlmRptTp", "_OthrSttlmTtls", "_Prgrmm", "_PrtctdData", "_Rcncltn", "_Rcvr", "_RtrvlRefNb", "_SctyTrlr", "_Sndr", "_SplmtryData", "_SttlmInstn", "_SttlmRptTp", "_SttlmSvc", "_SysTracAudtNb", "_TrnsmssnDtTm", "_TtlSttlmAmt", "_TxDesc"]
	@property
	def AcqrrSttlmTtls(self):
		return self._AcqrrSttlmTtls

	@AcqrrSttlmTtls.setter
	def AcqrrSttlmTtls(self, value):
		self._AcqrrSttlmTtls = value if value is not None else base_types.UninitialisedField(self, 'AcqrrSttlmTtls', SettlementCategoryTotal3, False)

	@AcqrrSttlmTtls.deleter
	def AcqrrSttlmTtls(self):
		del self._AcqrrSttlmTtls
		self._AcqrrSttlmTtls = base_types.UninitialisedField(self, 'AcqrrSttlmTtls', SettlementCategoryTotal3, False)

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData2, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData2, True)

	@property
	def AddtlFee(self):
		return self._AddtlFee

	@AddtlFee.setter
	def AddtlFee(self, value):
		self._AddtlFee = value if value is not None else base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee3, True)

	@AddtlFee.deleter
	def AddtlFee(self):
		del self._AddtlFee
		self._AddtlFee = base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee3, True)

	@property
	def AltrnMsgRsn(self):
		return self._AltrnMsgRsn

	@AltrnMsgRsn.setter
	def AltrnMsgRsn(self, value):
		self._AltrnMsgRsn = value if value is not None else base_types.UninitialisedField(self, 'AltrnMsgRsn', Max256Text, True)

	@AltrnMsgRsn.deleter
	def AltrnMsgRsn(self):
		del self._AltrnMsgRsn
		self._AltrnMsgRsn = base_types.UninitialisedField(self, 'AltrnMsgRsn', Max256Text, True)

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if value is not None else base_types.UninitialisedField(self, 'Dstn', PartyIdentification286, False)

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = base_types.UninitialisedField(self, 'Dstn', PartyIdentification286, False)

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if value is not None else base_types.UninitialisedField(self, 'FI', FinancialInstitution9, False)

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = base_types.UninitialisedField(self, 'FI', FinancialInstitution9, False)

	@property
	def FndsTrfAmt(self):
		return self._FndsTrfAmt

	@FndsTrfAmt.setter
	def FndsTrfAmt(self, value):
		self._FndsTrfAmt = value if value is not None else base_types.UninitialisedField(self, 'FndsTrfAmt', Amount17, False)

	@FndsTrfAmt.deleter
	def FndsTrfAmt(self):
		del self._FndsTrfAmt
		self._FndsTrfAmt = base_types.UninitialisedField(self, 'FndsTrfAmt', Amount17, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header71, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header71, False)

	@property
	def IssrSttlmTtls(self):
		return self._IssrSttlmTtls

	@IssrSttlmTtls.setter
	def IssrSttlmTtls(self, value):
		self._IssrSttlmTtls = value if value is not None else base_types.UninitialisedField(self, 'IssrSttlmTtls', SettlementCategoryTotal3, False)

	@IssrSttlmTtls.deleter
	def IssrSttlmTtls(self):
		del self._IssrSttlmTtls
		self._IssrSttlmTtls = base_types.UninitialisedField(self, 'IssrSttlmTtls', SettlementCategoryTotal3, False)

	@property
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if value is not None else base_types.UninitialisedField(self, 'Jursdctn', Jurisdiction2, False)

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = base_types.UninitialisedField(self, 'Jursdctn', Jurisdiction2, False)

	@property
	def LifeCyclId(self):
		return self._LifeCyclId

	@LifeCyclId.setter
	def LifeCyclId(self, value):
		self._LifeCyclId = value if value is not None else base_types.UninitialisedField(self, 'LifeCyclId', Exact15Text, False)

	@LifeCyclId.deleter
	def LifeCyclId(self):
		del self._LifeCyclId
		self._LifeCyclId = base_types.UninitialisedField(self, 'LifeCyclId', Exact15Text, False)

	@property
	def MsgRsn(self):
		return self._MsgRsn

	@MsgRsn.setter
	def MsgRsn(self, value):
		self._MsgRsn = value if value is not None else base_types.UninitialisedField(self, 'MsgRsn', ISO8583MessageReasonCode, True)

	@MsgRsn.deleter
	def MsgRsn(self):
		del self._MsgRsn
		self._MsgRsn = base_types.UninitialisedField(self, 'MsgRsn', ISO8583MessageReasonCode, True)

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if value is not None else base_types.UninitialisedField(self, 'Orgtr', PartyIdentification286, False)

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = base_types.UninitialisedField(self, 'Orgtr', PartyIdentification286, False)

	@property
	def OthrInstn(self):
		return self._OthrInstn

	@OthrInstn.setter
	def OthrInstn(self, value):
		self._OthrInstn = value if value is not None else base_types.UninitialisedField(self, 'OthrInstn', PartyIdentification285, False)

	@OthrInstn.deleter
	def OthrInstn(self):
		del self._OthrInstn
		self._OthrInstn = base_types.UninitialisedField(self, 'OthrInstn', PartyIdentification285, False)

	@property
	def OthrSttlmRptTp(self):
		return self._OthrSttlmRptTp

	@OthrSttlmRptTp.setter
	def OthrSttlmRptTp(self, value):
		self._OthrSttlmRptTp = value if value is not None else base_types.UninitialisedField(self, 'OthrSttlmRptTp', Max35Text, False)

	@OthrSttlmRptTp.deleter
	def OthrSttlmRptTp(self):
		del self._OthrSttlmRptTp
		self._OthrSttlmRptTp = base_types.UninitialisedField(self, 'OthrSttlmRptTp', Max35Text, False)

	@property
	def OthrSttlmTtls(self):
		return self._OthrSttlmTtls

	@OthrSttlmTtls.setter
	def OthrSttlmTtls(self, value):
		self._OthrSttlmTtls = value if value is not None else base_types.UninitialisedField(self, 'OthrSttlmTtls', SettlementCategoryTotal3, False)

	@OthrSttlmTtls.deleter
	def OthrSttlmTtls(self):
		del self._OthrSttlmTtls
		self._OthrSttlmTtls = base_types.UninitialisedField(self, 'OthrSttlmTtls', SettlementCategoryTotal3, False)

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode5, True)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode5, True)

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdData', ProtectedData2, True)

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = base_types.UninitialisedField(self, 'PrtctdData', ProtectedData2, True)

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if value is not None else base_types.UninitialisedField(self, 'Rcncltn', Reconciliation4, False)

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = base_types.UninitialisedField(self, 'Rcncltn', Reconciliation4, False)

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if value is not None else base_types.UninitialisedField(self, 'Rcvr', PartyIdentification286, False)

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = base_types.UninitialisedField(self, 'Rcvr', PartyIdentification286, False)

	@property
	def RtrvlRefNb(self):
		return self._RtrvlRefNb

	@RtrvlRefNb.setter
	def RtrvlRefNb(self, value):
		self._RtrvlRefNb = value if value is not None else base_types.UninitialisedField(self, 'RtrvlRefNb', Exact12Text, False)

	@RtrvlRefNb.deleter
	def RtrvlRefNb(self):
		del self._RtrvlRefNb
		self._RtrvlRefNb = base_types.UninitialisedField(self, 'RtrvlRefNb', Exact12Text, False)

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if value is not None else base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType41, False)

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = base_types.UninitialisedField(self, 'SctyTrlr', ContentInformationType41, False)

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', PartyIdentification286, False)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', PartyIdentification286, False)

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
	def SttlmInstn(self):
		return self._SttlmInstn

	@SttlmInstn.setter
	def SttlmInstn(self, value):
		self._SttlmInstn = value if value is not None else base_types.UninitialisedField(self, 'SttlmInstn', PartyIdentification286, False)

	@SttlmInstn.deleter
	def SttlmInstn(self):
		del self._SttlmInstn
		self._SttlmInstn = base_types.UninitialisedField(self, 'SttlmInstn', PartyIdentification286, False)

	@property
	def SttlmRptTp(self):
		return self._SttlmRptTp

	@SttlmRptTp.setter
	def SttlmRptTp(self, value):
		self._SttlmRptTp = value if value is not None else base_types.UninitialisedField(self, 'SttlmRptTp', SettlementReportType1Code, False)

	@SttlmRptTp.deleter
	def SttlmRptTp(self):
		del self._SttlmRptTp
		self._SttlmRptTp = base_types.UninitialisedField(self, 'SttlmRptTp', SettlementReportType1Code, False)

	@property
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if value is not None else base_types.UninitialisedField(self, 'SttlmSvc', SettlementService6, False)

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = base_types.UninitialisedField(self, 'SttlmSvc', SettlementService6, False)

	@property
	def SysTracAudtNb(self):
		return self._SysTracAudtNb

	@SysTracAudtNb.setter
	def SysTracAudtNb(self, value):
		self._SysTracAudtNb = value if value is not None else base_types.UninitialisedField(self, 'SysTracAudtNb', Max12NumericText, False)

	@SysTracAudtNb.deleter
	def SysTracAudtNb(self):
		del self._SysTracAudtNb
		self._SysTracAudtNb = base_types.UninitialisedField(self, 'SysTracAudtNb', Max12NumericText, False)

	@property
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if value is not None else base_types.UninitialisedField(self, 'TrnsmssnDtTm', ISODateTime, False)

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = base_types.UninitialisedField(self, 'TrnsmssnDtTm', ISODateTime, False)

	@property
	def TtlSttlmAmt(self):
		return self._TtlSttlmAmt

	@TtlSttlmAmt.setter
	def TtlSttlmAmt(self, value):
		self._TtlSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlSttlmAmt', SettlementCategoryTotal2, False)

	@TtlSttlmAmt.deleter
	def TtlSttlmAmt(self):
		del self._TtlSttlmAmt
		self._TtlSttlmAmt = base_types.UninitialisedField(self, 'TtlSttlmAmt', SettlementCategoryTotal2, False)

	@property
	def TxDesc(self):
		return self._TxDesc

	@TxDesc.setter
	def TxDesc(self, value):
		self._TxDesc = value if value is not None else base_types.UninitialisedField(self, 'TxDesc', Max1000Text, False)

	@TxDesc.deleter
	def TxDesc(self):
		del self._TxDesc
		self._TxDesc = base_types.UninitialisedField(self, 'TxDesc', Max1000Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrSttlmTtls', type=SettlementCategoryTotal3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FI', type=FinancialInstitution9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndsTrfAmt', type=Amount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrSttlmTtls', type=SettlementCategoryTotal3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrInstn', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSttlmRptTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSttlmTtls', type=SettlementCategoryTotal3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmInstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmRptTp', type=SettlementReportType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmAmt', type=SettlementCategoryTotal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
	))