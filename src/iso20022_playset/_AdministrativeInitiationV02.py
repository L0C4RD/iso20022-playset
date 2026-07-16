# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData2
from . import AdditionalFee3
from . import AdditionalService2
from . import AdministrativeType1Code
from . import CardData11
from . import Cardholder22
from . import ContentInformationType41
from . import Context19
from . import Customer4
from . import CustomerDevice5
from . import DateTime2
from . import ExchangeRateInformation5
from . import Header71
from . import ISO8583MessageReasonCode
from . import Instalment6
from . import Jurisdiction2
from . import LocalData17
from . import Max1000Text
from . import Max10KHexBinaryText
from . import Max20KText
from . import Max256Text
from . import Max35Text
from . import OriginalTransaction3
from . import PartyIdentification286
from . import PartyIdentification287
from . import PartyIdentification288
from . import PointOfInteractionComponent16
from . import ProcessingResult27
from . import ProgrammeMode4
from . import ProtectedData2
from . import Reconciliation4
from . import RiskContext3
from . import SettlementService5
from . import SpecialProgrammeQualification2
from . import SupplementaryData1
from . import Terminal7
from . import Token2
from . import TransactionIdentification56
from . import Verification6
from . import Wallet3

class AdministrativeInitiationV02(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_Acqrr", "_AddtlData", "_AddtlFee", "_AddtlSvc", "_AdmstvTp", "_AltrnMsgRsn", "_Card", "_Cntxt", "_ConvsDtTm", "_Crdhldr", "_Cstmr", "_CstmrDvc", "_Dstn", "_Hdr", "_ICCRltdData", "_Instlmt", "_Issr", "_Jursdctn", "_LclData", "_MsgRsn", "_OrgnlTx", "_Orgtr", "_OthrAdmstvTp", "_POICmpnt", "_PrcgRslt", "_Prgrmm", "_PrtctdData", "_Pyee", "_Pyer", "_Rcncltn", "_Rcvr", "_Rsk", "_SctyTrlr", "_Sndr", "_SpclPrgrmmQlfctn", "_SplmtryData", "_SttlmSvc", "_Termnl", "_Tkn", "_TxDesc", "_TxId", "_TxtMsg", "_Vrfctn", "_Wllt", "_XchgRate"]
	@property
	def Accptr(self):
		return self._Accptr

	@Accptr.setter
	def Accptr(self, value):
		self._Accptr = value if value is not None else base_types.UninitialisedField(self, 'Accptr', PartyIdentification288, False)

	@Accptr.deleter
	def Accptr(self):
		del self._Accptr
		self._Accptr = base_types.UninitialisedField(self, 'Accptr', PartyIdentification288, False)

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if value is not None else base_types.UninitialisedField(self, 'Acqrr', PartyIdentification286, False)

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = base_types.UninitialisedField(self, 'Acqrr', PartyIdentification286, False)

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
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if value is not None else base_types.UninitialisedField(self, 'AddtlSvc', AdditionalService2, True)

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = base_types.UninitialisedField(self, 'AddtlSvc', AdditionalService2, True)

	@property
	def AdmstvTp(self):
		return self._AdmstvTp

	@AdmstvTp.setter
	def AdmstvTp(self, value):
		self._AdmstvTp = value if value is not None else base_types.UninitialisedField(self, 'AdmstvTp', AdministrativeType1Code, False)

	@AdmstvTp.deleter
	def AdmstvTp(self):
		del self._AdmstvTp
		self._AdmstvTp = base_types.UninitialisedField(self, 'AdmstvTp', AdministrativeType1Code, False)

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
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if value is not None else base_types.UninitialisedField(self, 'Card', CardData11, False)

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = base_types.UninitialisedField(self, 'Card', CardData11, False)

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', Context19, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', Context19, False)

	@property
	def ConvsDtTm(self):
		return self._ConvsDtTm

	@ConvsDtTm.setter
	def ConvsDtTm(self, value):
		self._ConvsDtTm = value if value is not None else base_types.UninitialisedField(self, 'ConvsDtTm', DateTime2, False)

	@ConvsDtTm.deleter
	def ConvsDtTm(self):
		del self._ConvsDtTm
		self._ConvsDtTm = base_types.UninitialisedField(self, 'ConvsDtTm', DateTime2, False)

	@property
	def Crdhldr(self):
		return self._Crdhldr

	@Crdhldr.setter
	def Crdhldr(self, value):
		self._Crdhldr = value if value is not None else base_types.UninitialisedField(self, 'Crdhldr', Cardholder22, False)

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = base_types.UninitialisedField(self, 'Crdhldr', Cardholder22, False)

	@property
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if value is not None else base_types.UninitialisedField(self, 'Cstmr', Customer4, False)

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = base_types.UninitialisedField(self, 'Cstmr', Customer4, False)

	@property
	def CstmrDvc(self):
		return self._CstmrDvc

	@CstmrDvc.setter
	def CstmrDvc(self, value):
		self._CstmrDvc = value if value is not None else base_types.UninitialisedField(self, 'CstmrDvc', CustomerDevice5, False)

	@CstmrDvc.deleter
	def CstmrDvc(self):
		del self._CstmrDvc
		self._CstmrDvc = base_types.UninitialisedField(self, 'CstmrDvc', CustomerDevice5, False)

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
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max10KHexBinaryText, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max10KHexBinaryText, False)

	@property
	def Instlmt(self):
		return self._Instlmt

	@Instlmt.setter
	def Instlmt(self, value):
		self._Instlmt = value if value is not None else base_types.UninitialisedField(self, 'Instlmt', Instalment6, False)

	@Instlmt.deleter
	def Instlmt(self):
		del self._Instlmt
		self._Instlmt = base_types.UninitialisedField(self, 'Instlmt', Instalment6, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification286, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification286, False)

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
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData17, True)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData17, True)

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
	def OrgnlTx(self):
		return self._OrgnlTx

	@OrgnlTx.setter
	def OrgnlTx(self, value):
		self._OrgnlTx = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTx', OriginalTransaction3, True)

	@OrgnlTx.deleter
	def OrgnlTx(self):
		del self._OrgnlTx
		self._OrgnlTx = base_types.UninitialisedField(self, 'OrgnlTx', OriginalTransaction3, True)

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
	def OthrAdmstvTp(self):
		return self._OthrAdmstvTp

	@OthrAdmstvTp.setter
	def OthrAdmstvTp(self, value):
		self._OthrAdmstvTp = value if value is not None else base_types.UninitialisedField(self, 'OthrAdmstvTp', Max35Text, False)

	@OthrAdmstvTp.deleter
	def OthrAdmstvTp(self):
		del self._OthrAdmstvTp
		self._OthrAdmstvTp = base_types.UninitialisedField(self, 'OthrAdmstvTp', Max35Text, False)

	@property
	def POICmpnt(self):
		return self._POICmpnt

	@POICmpnt.setter
	def POICmpnt(self, value):
		self._POICmpnt = value if value is not None else base_types.UninitialisedField(self, 'POICmpnt', PointOfInteractionComponent16, True)

	@POICmpnt.deleter
	def POICmpnt(self):
		del self._POICmpnt
		self._POICmpnt = base_types.UninitialisedField(self, 'POICmpnt', PointOfInteractionComponent16, True)

	@property
	def PrcgRslt(self):
		return self._PrcgRslt

	@PrcgRslt.setter
	def PrcgRslt(self, value):
		self._PrcgRslt = value if value is not None else base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult27, False)

	@PrcgRslt.deleter
	def PrcgRslt(self):
		del self._PrcgRslt
		self._PrcgRslt = base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult27, False)

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode4, False)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode4, False)

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
	def Pyee(self):
		return self._Pyee

	@Pyee.setter
	def Pyee(self, value):
		self._Pyee = value if value is not None else base_types.UninitialisedField(self, 'Pyee', PartyIdentification287, False)

	@Pyee.deleter
	def Pyee(self):
		del self._Pyee
		self._Pyee = base_types.UninitialisedField(self, 'Pyee', PartyIdentification287, False)

	@property
	def Pyer(self):
		return self._Pyer

	@Pyer.setter
	def Pyer(self, value):
		self._Pyer = value if value is not None else base_types.UninitialisedField(self, 'Pyer', PartyIdentification287, False)

	@Pyer.deleter
	def Pyer(self):
		del self._Pyer
		self._Pyer = base_types.UninitialisedField(self, 'Pyer', PartyIdentification287, False)

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
	def Rsk(self):
		return self._Rsk

	@Rsk.setter
	def Rsk(self, value):
		self._Rsk = value if value is not None else base_types.UninitialisedField(self, 'Rsk', RiskContext3, True)

	@Rsk.deleter
	def Rsk(self):
		del self._Rsk
		self._Rsk = base_types.UninitialisedField(self, 'Rsk', RiskContext3, True)

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
	def SpclPrgrmmQlfctn(self):
		return self._SpclPrgrmmQlfctn

	@SpclPrgrmmQlfctn.setter
	def SpclPrgrmmQlfctn(self, value):
		self._SpclPrgrmmQlfctn = value if value is not None else base_types.UninitialisedField(self, 'SpclPrgrmmQlfctn', SpecialProgrammeQualification2, True)

	@SpclPrgrmmQlfctn.deleter
	def SpclPrgrmmQlfctn(self):
		del self._SpclPrgrmmQlfctn
		self._SpclPrgrmmQlfctn = base_types.UninitialisedField(self, 'SpclPrgrmmQlfctn', SpecialProgrammeQualification2, True)

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
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if value is not None else base_types.UninitialisedField(self, 'SttlmSvc', SettlementService5, False)

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = base_types.UninitialisedField(self, 'SttlmSvc', SettlementService5, False)

	@property
	def Termnl(self):
		return self._Termnl

	@Termnl.setter
	def Termnl(self, value):
		self._Termnl = value if value is not None else base_types.UninitialisedField(self, 'Termnl', Terminal7, False)

	@Termnl.deleter
	def Termnl(self):
		del self._Termnl
		self._Termnl = base_types.UninitialisedField(self, 'Termnl', Terminal7, False)

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if value is not None else base_types.UninitialisedField(self, 'Tkn', Token2, False)

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = base_types.UninitialisedField(self, 'Tkn', Token2, False)

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

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentification56, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentification56, False)

	@property
	def TxtMsg(self):
		return self._TxtMsg

	@TxtMsg.setter
	def TxtMsg(self, value):
		self._TxtMsg = value if value is not None else base_types.UninitialisedField(self, 'TxtMsg', Max20KText, False)

	@TxtMsg.deleter
	def TxtMsg(self):
		del self._TxtMsg
		self._TxtMsg = base_types.UninitialisedField(self, 'TxtMsg', Max20KText, False)

	@property
	def Vrfctn(self):
		return self._Vrfctn

	@Vrfctn.setter
	def Vrfctn(self, value):
		self._Vrfctn = value if value is not None else base_types.UninitialisedField(self, 'Vrfctn', Verification6, True)

	@Vrfctn.deleter
	def Vrfctn(self):
		del self._Vrfctn
		self._Vrfctn = base_types.UninitialisedField(self, 'Vrfctn', Verification6, True)

	@property
	def Wllt(self):
		return self._Wllt

	@Wllt.setter
	def Wllt(self, value):
		self._Wllt = value if value is not None else base_types.UninitialisedField(self, 'Wllt', Wallet3, False)

	@Wllt.deleter
	def Wllt(self):
		del self._Wllt
		self._Wllt = base_types.UninitialisedField(self, 'Wllt', Wallet3, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', ExchangeRateInformation5, True)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', ExchangeRateInformation5, True)

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