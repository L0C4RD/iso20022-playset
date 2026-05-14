from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._AdditionalFee4 import AdditionalFee4
from ._Amount17 import Amount17
from ._ContentInformationType41 import ContentInformationType41
from ._DestinationData1 import DestinationData1
from ._EncryptedData2 import EncryptedData2
from ._Exact12Text import Exact12Text
from ._Exact15Text import Exact15Text
from ._FinancialInstitutionData1 import FinancialInstitutionData1
from ._Header72 import Header72
from ._ISO8583MessageReasonCode import ISO8583MessageReasonCode
from ._ISODateTime import ISODateTime
from ._Jurisdiction2 import Jurisdiction2
from ._Max1000Text import Max1000Text
from ._Max12NumericText import Max12NumericText
from ._Max256Text import Max256Text
from ._OriginatorData2 import OriginatorData2
from ._ProgrammeMode6 import ProgrammeMode6
from ._ReceiverData1 import ReceiverData1
from ._Reconciliation5 import Reconciliation5
from ._SenderData1 import SenderData1
from ._SettlementCategoryTotal3 import SettlementCategoryTotal3
from ._SettlementInstitutionData1 import SettlementInstitutionData1
from ._SettlementReportType2Code import SettlementReportType2Code
from ._SettlementService7 import SettlementService7

class SettlementReportingInitiationV04(base_types._BaseFieldType):

	__slots__ = ["_AcqrrSttlmTtls", "_AddtlFee", "_AltrnMsgRsn", "_Dstn", "_FI", "_FndsTrfAmt", "_Hdr", "_IssrSttlmTtls", "_Jursdctn", "_LifeCyclId", "_MsgRsn", "_NtlData", "_Orgtr", "_OthrInstn", "_OthrSttlmTtls", "_Prgrmm", "_PrtctdData", "_PrvtData", "_Rcncltn", "_Rcvr", "_RtrvlRefNb", "_SctyTrlr", "_Sndr", "_SttlmInstn", "_SttlmRptTp", "_SttlmSvc", "_SysTracAudtNb", "_TrnsmssnDtTm", "_TtlSttlmAmt", "_TxDesc"]
	@property
	def AcqrrSttlmTtls(self):
		return self._AcqrrSttlmTtls

	@AcqrrSttlmTtls.setter
	def AcqrrSttlmTtls(self, value):
		self._AcqrrSttlmTtls = value if type(value) != base_types.auto else self.make_default("AcqrrSttlmTtls")

	@AcqrrSttlmTtls.deleter
	def AcqrrSttlmTtls(self):
		del self._AcqrrSttlmTtls
		self._AcqrrSttlmTtls = None

	@property
	def AddtlFee(self):
		return self._AddtlFee

	@AddtlFee.setter
	def AddtlFee(self, value):
		self._AddtlFee = value if type(value) != base_types.auto else self.make_default("AddtlFee")

	@AddtlFee.deleter
	def AddtlFee(self):
		del self._AddtlFee
		self._AddtlFee = None

	@property
	def AltrnMsgRsn(self):
		return self._AltrnMsgRsn

	@AltrnMsgRsn.setter
	def AltrnMsgRsn(self, value):
		self._AltrnMsgRsn = value if type(value) != base_types.auto else self.make_default("AltrnMsgRsn")

	@AltrnMsgRsn.deleter
	def AltrnMsgRsn(self):
		del self._AltrnMsgRsn
		self._AltrnMsgRsn = None

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if type(value) != base_types.auto else self.make_default("Dstn")

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = None

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if type(value) != base_types.auto else self.make_default("FI")

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = None

	@property
	def FndsTrfAmt(self):
		return self._FndsTrfAmt

	@FndsTrfAmt.setter
	def FndsTrfAmt(self, value):
		self._FndsTrfAmt = value if type(value) != base_types.auto else self.make_default("FndsTrfAmt")

	@FndsTrfAmt.deleter
	def FndsTrfAmt(self):
		del self._FndsTrfAmt
		self._FndsTrfAmt = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def IssrSttlmTtls(self):
		return self._IssrSttlmTtls

	@IssrSttlmTtls.setter
	def IssrSttlmTtls(self, value):
		self._IssrSttlmTtls = value if type(value) != base_types.auto else self.make_default("IssrSttlmTtls")

	@IssrSttlmTtls.deleter
	def IssrSttlmTtls(self):
		del self._IssrSttlmTtls
		self._IssrSttlmTtls = None

	@property
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if type(value) != base_types.auto else self.make_default("Jursdctn")

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = None

	@property
	def LifeCyclId(self):
		return self._LifeCyclId

	@LifeCyclId.setter
	def LifeCyclId(self, value):
		self._LifeCyclId = value if type(value) != base_types.auto else self.make_default("LifeCyclId")

	@LifeCyclId.deleter
	def LifeCyclId(self):
		del self._LifeCyclId
		self._LifeCyclId = None

	@property
	def MsgRsn(self):
		return self._MsgRsn

	@MsgRsn.setter
	def MsgRsn(self, value):
		self._MsgRsn = value if type(value) != base_types.auto else self.make_default("MsgRsn")

	@MsgRsn.deleter
	def MsgRsn(self):
		del self._MsgRsn
		self._MsgRsn = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != base_types.auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	@property
	def OthrInstn(self):
		return self._OthrInstn

	@OthrInstn.setter
	def OthrInstn(self, value):
		self._OthrInstn = value if type(value) != base_types.auto else self.make_default("OthrInstn")

	@OthrInstn.deleter
	def OthrInstn(self):
		del self._OthrInstn
		self._OthrInstn = None

	@property
	def OthrSttlmTtls(self):
		return self._OthrSttlmTtls

	@OthrSttlmTtls.setter
	def OthrSttlmTtls(self, value):
		self._OthrSttlmTtls = value if type(value) != base_types.auto else self.make_default("OthrSttlmTtls")

	@OthrSttlmTtls.deleter
	def OthrSttlmTtls(self):
		del self._OthrSttlmTtls
		self._OthrSttlmTtls = None

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if type(value) != base_types.auto else self.make_default("Prgrmm")

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = None

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if type(value) != base_types.auto else self.make_default("PrtctdData")

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if type(value) != base_types.auto else self.make_default("Rcncltn")

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = None

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if type(value) != base_types.auto else self.make_default("Rcvr")

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = None

	@property
	def RtrvlRefNb(self):
		return self._RtrvlRefNb

	@RtrvlRefNb.setter
	def RtrvlRefNb(self, value):
		self._RtrvlRefNb = value if type(value) != base_types.auto else self.make_default("RtrvlRefNb")

	@RtrvlRefNb.deleter
	def RtrvlRefNb(self):
		del self._RtrvlRefNb
		self._RtrvlRefNb = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != base_types.auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if type(value) != base_types.auto else self.make_default("Sndr")

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = None

	@property
	def SttlmInstn(self):
		return self._SttlmInstn

	@SttlmInstn.setter
	def SttlmInstn(self, value):
		self._SttlmInstn = value if type(value) != base_types.auto else self.make_default("SttlmInstn")

	@SttlmInstn.deleter
	def SttlmInstn(self):
		del self._SttlmInstn
		self._SttlmInstn = None

	@property
	def SttlmRptTp(self):
		return self._SttlmRptTp

	@SttlmRptTp.setter
	def SttlmRptTp(self, value):
		self._SttlmRptTp = value if type(value) != base_types.auto else self.make_default("SttlmRptTp")

	@SttlmRptTp.deleter
	def SttlmRptTp(self):
		del self._SttlmRptTp
		self._SttlmRptTp = None

	@property
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if type(value) != base_types.auto else self.make_default("SttlmSvc")

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = None

	@property
	def SysTracAudtNb(self):
		return self._SysTracAudtNb

	@SysTracAudtNb.setter
	def SysTracAudtNb(self, value):
		self._SysTracAudtNb = value if type(value) != base_types.auto else self.make_default("SysTracAudtNb")

	@SysTracAudtNb.deleter
	def SysTracAudtNb(self):
		del self._SysTracAudtNb
		self._SysTracAudtNb = None

	@property
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if type(value) != base_types.auto else self.make_default("TrnsmssnDtTm")

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = None

	@property
	def TtlSttlmAmt(self):
		return self._TtlSttlmAmt

	@TtlSttlmAmt.setter
	def TtlSttlmAmt(self, value):
		self._TtlSttlmAmt = value if type(value) != base_types.auto else self.make_default("TtlSttlmAmt")

	@TtlSttlmAmt.deleter
	def TtlSttlmAmt(self):
		del self._TtlSttlmAmt
		self._TtlSttlmAmt = None

	@property
	def TxDesc(self):
		return self._TxDesc

	@TxDesc.setter
	def TxDesc(self, value):
		self._TxDesc = value if type(value) != base_types.auto else self.make_default("TxDesc")

	@TxDesc.deleter
	def TxDesc(self):
		del self._TxDesc
		self._TxDesc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrSttlmTtls', type=SettlementCategoryTotal3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FI', type=FinancialInstitutionData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndsTrfAmt', type=Amount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrSttlmTtls', type=SettlementCategoryTotal3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrInstn', type=FinancialInstitutionData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSttlmTtls', type=SettlementCategoryTotal3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstn', type=SettlementInstitutionData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmRptTp', type=SettlementReportType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmAmt', type=SettlementCategoryTotal3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
	))

