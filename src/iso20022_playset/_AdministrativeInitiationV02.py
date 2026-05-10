from . import base_types
from ._Context19 import Context19
from ._OriginalTransaction3 import OriginalTransaction3
from ._Max256Text import Max256Text
from ._AdministrativeType1Code import AdministrativeType1Code
from ._PartyIdentification286 import PartyIdentification286
from ._SupplementaryData1 import SupplementaryData1
from ._ContentInformationType41 import ContentInformationType41
from ._CustomerDevice5 import CustomerDevice5
from ._Max20KText import Max20KText
from ._Terminal7 import Terminal7
from ._AdditionalFee3 import AdditionalFee3
from ._Reconciliation4 import Reconciliation4
from ._Customer4 import Customer4
from ._RiskContext3 import RiskContext3
from ._Max1000Text import Max1000Text
from ._PartyIdentification288 import PartyIdentification288
from ._PartyIdentification287 import PartyIdentification287
from ._AdditionalService2 import AdditionalService2
from ._PointOfInteractionComponent16 import PointOfInteractionComponent16
from ._DateTime2 import DateTime2
from ._Verification6 import Verification6
from ._Header71 import Header71
from ._SettlementService5 import SettlementService5
from ._ProcessingResult27 import ProcessingResult27
from ._AdditionalData2 import AdditionalData2
from ._CardData11 import CardData11
from ._Jurisdiction2 import Jurisdiction2
from ._Cardholder22 import Cardholder22
from ._ISO8583MessageReasonCode import ISO8583MessageReasonCode
from ._ExchangeRateInformation5 import ExchangeRateInformation5
from ._ProgrammeMode4 import ProgrammeMode4
from ._LocalData17 import LocalData17
from ._ProtectedData2 import ProtectedData2
from ._Wallet3 import Wallet3
from ._Instalment6 import Instalment6
from ._Max10KHexBinaryText import Max10KHexBinaryText
from ._Max35Text import Max35Text
from ._TransactionIdentification56 import TransactionIdentification56
from ._SpecialProgrammeQualification2 import SpecialProgrammeQualification2
from ._Token2 import Token2

class AdministrativeInitiationV02(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_MsgRsn", "_Termnl", "_Sndr", "_AddtlData", "_AddtlFee", "_Pyee", "_LclData", "_TxtMsg", "_Vrfctn", "_Rcncltn", "_ConvsDtTm", "_Crdhldr", "_POICmpnt", "_Cstmr", "_Pyer", "_CstmrDvc", "_Rsk", "_PrcgRslt", "_Orgtr", "_Card", "_XchgRate", "_OthrAdmstvTp", "_Acqrr", "_Dstn", "_ICCRltdData", "_OrgnlTx", "_Instlmt", "_Prgrmm", "_Issr", "_Jursdctn", "_TxId", "_AdmstvTp", "_Hdr", "_Tkn", "_SctyTrlr", "_AltrnMsgRsn", "_Rcvr", "_Cntxt", "_SttlmSvc", "_PrtctdData", "_TxDesc", "_AddtlSvc", "_SpclPrgrmmQlfctn", "_Wllt", "_SplmtryData"]
	@property
	def Accptr(self):
		return self._Accptr

	@Accptr.setter
	def Accptr(self, value):
		self._Accptr = value if type(value) != base_types.auto else self.make_default("Accptr")

	@Accptr.deleter
	def Accptr(self):
		del self._Accptr
		self._Accptr = None

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if type(value) != base_types.auto else self.make_default("Acqrr")

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

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
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if type(value) != base_types.auto else self.make_default("AddtlSvc")

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = None

	@property
	def AdmstvTp(self):
		return self._AdmstvTp

	@AdmstvTp.setter
	def AdmstvTp(self, value):
		self._AdmstvTp = value if type(value) != base_types.auto else self.make_default("AdmstvTp")

	@AdmstvTp.deleter
	def AdmstvTp(self):
		del self._AdmstvTp
		self._AdmstvTp = None

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
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != base_types.auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != base_types.auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	@property
	def ConvsDtTm(self):
		return self._ConvsDtTm

	@ConvsDtTm.setter
	def ConvsDtTm(self, value):
		self._ConvsDtTm = value if type(value) != base_types.auto else self.make_default("ConvsDtTm")

	@ConvsDtTm.deleter
	def ConvsDtTm(self):
		del self._ConvsDtTm
		self._ConvsDtTm = None

	@property
	def Crdhldr(self):
		return self._Crdhldr

	@Crdhldr.setter
	def Crdhldr(self, value):
		self._Crdhldr = value if type(value) != base_types.auto else self.make_default("Crdhldr")

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = None

	@property
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if type(value) != base_types.auto else self.make_default("Cstmr")

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = None

	@property
	def CstmrDvc(self):
		return self._CstmrDvc

	@CstmrDvc.setter
	def CstmrDvc(self, value):
		self._CstmrDvc = value if type(value) != base_types.auto else self.make_default("CstmrDvc")

	@CstmrDvc.deleter
	def CstmrDvc(self):
		del self._CstmrDvc
		self._CstmrDvc = None

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
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != base_types.auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def Instlmt(self):
		return self._Instlmt

	@Instlmt.setter
	def Instlmt(self, value):
		self._Instlmt = value if type(value) != base_types.auto else self.make_default("Instlmt")

	@Instlmt.deleter
	def Instlmt(self):
		del self._Instlmt
		self._Instlmt = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if type(value) != base_types.auto else self.make_default("LclData")

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = None

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
	def OrgnlTx(self):
		return self._OrgnlTx

	@OrgnlTx.setter
	def OrgnlTx(self, value):
		self._OrgnlTx = value if type(value) != base_types.auto else self.make_default("OrgnlTx")

	@OrgnlTx.deleter
	def OrgnlTx(self):
		del self._OrgnlTx
		self._OrgnlTx = None

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
	def OthrAdmstvTp(self):
		return self._OthrAdmstvTp

	@OthrAdmstvTp.setter
	def OthrAdmstvTp(self, value):
		self._OthrAdmstvTp = value if type(value) != base_types.auto else self.make_default("OthrAdmstvTp")

	@OthrAdmstvTp.deleter
	def OthrAdmstvTp(self):
		del self._OthrAdmstvTp
		self._OthrAdmstvTp = None

	@property
	def POICmpnt(self):
		return self._POICmpnt

	@POICmpnt.setter
	def POICmpnt(self, value):
		self._POICmpnt = value if type(value) != base_types.auto else self.make_default("POICmpnt")

	@POICmpnt.deleter
	def POICmpnt(self):
		del self._POICmpnt
		self._POICmpnt = None

	@property
	def PrcgRslt(self):
		return self._PrcgRslt

	@PrcgRslt.setter
	def PrcgRslt(self, value):
		self._PrcgRslt = value if type(value) != base_types.auto else self.make_default("PrcgRslt")

	@PrcgRslt.deleter
	def PrcgRslt(self):
		del self._PrcgRslt
		self._PrcgRslt = None

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
	def Pyee(self):
		return self._Pyee

	@Pyee.setter
	def Pyee(self, value):
		self._Pyee = value if type(value) != base_types.auto else self.make_default("Pyee")

	@Pyee.deleter
	def Pyee(self):
		del self._Pyee
		self._Pyee = None

	@property
	def Pyer(self):
		return self._Pyer

	@Pyer.setter
	def Pyer(self, value):
		self._Pyer = value if type(value) != base_types.auto else self.make_default("Pyer")

	@Pyer.deleter
	def Pyer(self):
		del self._Pyer
		self._Pyer = None

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
	def Rsk(self):
		return self._Rsk

	@Rsk.setter
	def Rsk(self, value):
		self._Rsk = value if type(value) != base_types.auto else self.make_default("Rsk")

	@Rsk.deleter
	def Rsk(self):
		del self._Rsk
		self._Rsk = None

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
	def SpclPrgrmmQlfctn(self):
		return self._SpclPrgrmmQlfctn

	@SpclPrgrmmQlfctn.setter
	def SpclPrgrmmQlfctn(self, value):
		self._SpclPrgrmmQlfctn = value if type(value) != base_types.auto else self.make_default("SpclPrgrmmQlfctn")

	@SpclPrgrmmQlfctn.deleter
	def SpclPrgrmmQlfctn(self):
		del self._SpclPrgrmmQlfctn
		self._SpclPrgrmmQlfctn = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

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
	def Termnl(self):
		return self._Termnl

	@Termnl.setter
	def Termnl(self, value):
		self._Termnl = value if type(value) != base_types.auto else self.make_default("Termnl")

	@Termnl.deleter
	def Termnl(self):
		del self._Termnl
		self._Termnl = None

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if type(value) != base_types.auto else self.make_default("Tkn")

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = None

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

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def TxtMsg(self):
		return self._TxtMsg

	@TxtMsg.setter
	def TxtMsg(self, value):
		self._TxtMsg = value if type(value) != base_types.auto else self.make_default("TxtMsg")

	@TxtMsg.deleter
	def TxtMsg(self):
		del self._TxtMsg
		self._TxtMsg = None

	@property
	def Vrfctn(self):
		return self._Vrfctn

	@Vrfctn.setter
	def Vrfctn(self, value):
		self._Vrfctn = value if type(value) != base_types.auto else self.make_default("Vrfctn")

	@Vrfctn.deleter
	def Vrfctn(self):
		del self._Vrfctn
		self._Vrfctn = None

	@property
	def Wllt(self):
		return self._Wllt

	@Wllt.setter
	def Wllt(self, value):
		self._Wllt = value if type(value) != base_types.auto else self.make_default("Wllt")

	@Wllt.deleter
	def Wllt(self):
		del self._Wllt
		self._Wllt = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptr', type=PartyIdentification288, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=PartyIdentification286, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlSvc', type=AdditionalService2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdmstvTp', type=AdministrativeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=Context19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDtTm', type=DateTime2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cstmr', type=Customer4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrDvc', type=CustomerDevice5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10KHexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instlmt', type=Instalment6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTx', type=OriginalTransaction3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAdmstvTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POICmpnt', type=PointOfInteractionComponent16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pyee', type=PartyIdentification287, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PartyIdentification287, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsk', type=RiskContext3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclPrgrmmQlfctn', type=SpecialProgrammeQualification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification56, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxtMsg', type=Max20KText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrfctn', type=Verification6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Wllt', type=Wallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=ExchangeRateInformation5, min=0, max=None, mutex_group=None, array=True),
	))

