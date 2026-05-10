import base_types
import AdditionalInformation21
import ProgrammeMode5
import Max70Text
import Jurisdiction2
import ProtectedData2
import PartyIdentification286
import Number
import ClearingBatchData3
import ISODateTime
import Header71
import Reconciliation4
import Max35Binary
import TrueFalseIndicator
import Exact12Text
import Max12NumericText
import SupplementaryData1
import ISO8583ResponseCode
import SettlementService6
import Exact15Text
import Record3
import ContentInformationType41
import ClearingControlTotals3
import AdditionalData2
import ProcessingResult26

class BatchTransferInitiationV03(base_types._BaseFieldType):

	__slots__ = ["_Prgrmm", "_SttlmSvc", "_AgtData", "_ReqAck", "_TrnsmssnDtTm", "_OrgnlBtchId", "_OrgnlRspnCd", "_BtchId", "_NbOfMsgs", "_ClrBtchData", "_SysTracAudtNb", "_Rcncltn", "_Dstn", "_AddtlData", "_ClrCtrlTtls", "_Jursdctn", "_LifeCyclId", "_RtrvlRefNb", "_SctyTrlr", "_Hdr", "_BtchChcksm", "_Rcrd", "_PrcgRslt", "_PrtctdData", "_SplmtryData", "_Orgtr"]
	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if type(value) != auto else self.make_default("Prgrmm")

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = None

	@property
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if type(value) != auto else self.make_default("SttlmSvc")

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = None

	@property
	def AgtData(self):
		return self._AgtData

	@AgtData.setter
	def AgtData(self, value):
		self._AgtData = value if type(value) != auto else self.make_default("AgtData")

	@AgtData.deleter
	def AgtData(self):
		del self._AgtData
		self._AgtData = None

	@property
	def ReqAck(self):
		return self._ReqAck

	@ReqAck.setter
	def ReqAck(self, value):
		self._ReqAck = value if type(value) != auto else self.make_default("ReqAck")

	@ReqAck.deleter
	def ReqAck(self):
		del self._ReqAck
		self._ReqAck = None

	@property
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if type(value) != auto else self.make_default("TrnsmssnDtTm")

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = None

	@property
	def OrgnlBtchId(self):
		return self._OrgnlBtchId

	@OrgnlBtchId.setter
	def OrgnlBtchId(self, value):
		self._OrgnlBtchId = value if type(value) != auto else self.make_default("OrgnlBtchId")

	@OrgnlBtchId.deleter
	def OrgnlBtchId(self):
		del self._OrgnlBtchId
		self._OrgnlBtchId = None

	@property
	def OrgnlRspnCd(self):
		return self._OrgnlRspnCd

	@OrgnlRspnCd.setter
	def OrgnlRspnCd(self, value):
		self._OrgnlRspnCd = value if type(value) != auto else self.make_default("OrgnlRspnCd")

	@OrgnlRspnCd.deleter
	def OrgnlRspnCd(self):
		del self._OrgnlRspnCd
		self._OrgnlRspnCd = None

	@property
	def BtchId(self):
		return self._BtchId

	@BtchId.setter
	def BtchId(self, value):
		self._BtchId = value if type(value) != auto else self.make_default("BtchId")

	@BtchId.deleter
	def BtchId(self):
		del self._BtchId
		self._BtchId = None

	@property
	def NbOfMsgs(self):
		return self._NbOfMsgs

	@NbOfMsgs.setter
	def NbOfMsgs(self, value):
		self._NbOfMsgs = value if type(value) != auto else self.make_default("NbOfMsgs")

	@NbOfMsgs.deleter
	def NbOfMsgs(self):
		del self._NbOfMsgs
		self._NbOfMsgs = None

	@property
	def ClrBtchData(self):
		return self._ClrBtchData

	@ClrBtchData.setter
	def ClrBtchData(self, value):
		self._ClrBtchData = value if type(value) != auto else self.make_default("ClrBtchData")

	@ClrBtchData.deleter
	def ClrBtchData(self):
		del self._ClrBtchData
		self._ClrBtchData = None

	@property
	def SysTracAudtNb(self):
		return self._SysTracAudtNb

	@SysTracAudtNb.setter
	def SysTracAudtNb(self, value):
		self._SysTracAudtNb = value if type(value) != auto else self.make_default("SysTracAudtNb")

	@SysTracAudtNb.deleter
	def SysTracAudtNb(self):
		del self._SysTracAudtNb
		self._SysTracAudtNb = None

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if type(value) != auto else self.make_default("Rcncltn")

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = None

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if type(value) != auto else self.make_default("Dstn")

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def ClrCtrlTtls(self):
		return self._ClrCtrlTtls

	@ClrCtrlTtls.setter
	def ClrCtrlTtls(self, value):
		self._ClrCtrlTtls = value if type(value) != auto else self.make_default("ClrCtrlTtls")

	@ClrCtrlTtls.deleter
	def ClrCtrlTtls(self):
		del self._ClrCtrlTtls
		self._ClrCtrlTtls = None

	@property
	def Jursdctn(self):
		return self._Jursdctn

	@Jursdctn.setter
	def Jursdctn(self, value):
		self._Jursdctn = value if type(value) != auto else self.make_default("Jursdctn")

	@Jursdctn.deleter
	def Jursdctn(self):
		del self._Jursdctn
		self._Jursdctn = None

	@property
	def LifeCyclId(self):
		return self._LifeCyclId

	@LifeCyclId.setter
	def LifeCyclId(self, value):
		self._LifeCyclId = value if type(value) != auto else self.make_default("LifeCyclId")

	@LifeCyclId.deleter
	def LifeCyclId(self):
		del self._LifeCyclId
		self._LifeCyclId = None

	@property
	def RtrvlRefNb(self):
		return self._RtrvlRefNb

	@RtrvlRefNb.setter
	def RtrvlRefNb(self, value):
		self._RtrvlRefNb = value if type(value) != auto else self.make_default("RtrvlRefNb")

	@RtrvlRefNb.deleter
	def RtrvlRefNb(self):
		del self._RtrvlRefNb
		self._RtrvlRefNb = None

	@property
	def SctyTrlr(self):
		return self._SctyTrlr

	@SctyTrlr.setter
	def SctyTrlr(self, value):
		self._SctyTrlr = value if type(value) != auto else self.make_default("SctyTrlr")

	@SctyTrlr.deleter
	def SctyTrlr(self):
		del self._SctyTrlr
		self._SctyTrlr = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def BtchChcksm(self):
		return self._BtchChcksm

	@BtchChcksm.setter
	def BtchChcksm(self, value):
		self._BtchChcksm = value if type(value) != auto else self.make_default("BtchChcksm")

	@BtchChcksm.deleter
	def BtchChcksm(self):
		del self._BtchChcksm
		self._BtchChcksm = None

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

	@property
	def PrcgRslt(self):
		return self._PrcgRslt

	@PrcgRslt.setter
	def PrcgRslt(self, value):
		self._PrcgRslt = value if type(value) != auto else self.make_default("PrcgRslt")

	@PrcgRslt.deleter
	def PrcgRslt(self):
		del self._PrcgRslt
		self._PrcgRslt = None

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if type(value) != auto else self.make_default("PrtctdData")

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtData', type=AdditionalInformation21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqAck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBtchId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfMsgs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrBtchData', type=ClearingBatchData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrCtrlTtls', type=ClearingControlTotals3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchChcksm', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=Record3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
	))

