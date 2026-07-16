# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import AcceptorData3
from . import AcquirerData1
from . import AdditionalFee4
from . import CardData17
from . import Cardholder23
from . import ContentInformationType41
from . import CorrectionIdentification1
from . import CustomerDevice6
from . import DestinationData1
from . import EncryptedData2
from . import Exact12Text
from . import Exact15Text
from . import FileActionScope1Code
from . import FileActionType3Code
from . import Header72
from . import ISO8583MessageReasonCode
from . import ISO8583ResponseCode
from . import ISODate
from . import ISODateTime
from . import IssuerData1
from . import Jurisdiction2
from . import Max1000Text
from . import Max12NumericText
from . import Max140Text
from . import Max256Text
from . import Max35Text
from . import OriginatorData2
from . import OutputFormat7Code
from . import PayeeData1
from . import PayerData1
from . import PointOfInteractionComponent16
from . import ProgrammeMode6
from . import ReceiverData1
from . import Reconciliation5
from . import SenderData1
from . import SettlementService7
from . import Terminal10
from . import Token5
from . import TrueFalseIndicator
from . import Wallet4

class FileActionInitiationV04(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_Acqrr", "_ActnDt", "_AddtlFee", "_AltrnMsgRsn", "_Card", "_Conttn", "_Crdhldr", "_Crrctn", "_CstmrDvc", "_DataRcrd", "_Dstn", "_FileActnScp", "_FileActnTp", "_FileNm", "_FileSctyCd", "_Frmt", "_Hdr", "_Issr", "_Jursdctn", "_LifeCyclId", "_MsgRsn", "_NtlData", "_Orgtr", "_POICmpnt", "_Prgrmm", "_PrtctdData", "_PrvtData", "_Pyee", "_Pyer", "_Rcncltn", "_Rcvr", "_RspnCd", "_RtrvlRefNb", "_SctyTrlr", "_Sndr", "_SttlmSvc", "_SysTracAudtNb", "_Termnl", "_Tkn", "_TrnsmssnDtTm", "_TxDesc", "_Wllt"]
	@property
	def Accptr(self):
		return self._Accptr

	@Accptr.setter
	def Accptr(self, value):
		self._Accptr = value if value is not None else base_types.UninitialisedField(self, 'Accptr', AcceptorData3, False)

	@Accptr.deleter
	def Accptr(self):
		del self._Accptr
		self._Accptr = base_types.UninitialisedField(self, 'Accptr', AcceptorData3, False)

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if value is not None else base_types.UninitialisedField(self, 'Acqrr', AcquirerData1, False)

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = base_types.UninitialisedField(self, 'Acqrr', AcquirerData1, False)

	@property
	def ActnDt(self):
		return self._ActnDt

	@ActnDt.setter
	def ActnDt(self, value):
		self._ActnDt = value if value is not None else base_types.UninitialisedField(self, 'ActnDt', ISODate, False)

	@ActnDt.deleter
	def ActnDt(self):
		del self._ActnDt
		self._ActnDt = base_types.UninitialisedField(self, 'ActnDt', ISODate, False)

	@property
	def AddtlFee(self):
		return self._AddtlFee

	@AddtlFee.setter
	def AddtlFee(self, value):
		self._AddtlFee = value if value is not None else base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee4, True)

	@AddtlFee.deleter
	def AddtlFee(self):
		del self._AddtlFee
		self._AddtlFee = base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee4, True)

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
		self._Card = value if value is not None else base_types.UninitialisedField(self, 'Card', CardData17, False)

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = base_types.UninitialisedField(self, 'Card', CardData17, False)

	@property
	def Conttn(self):
		return self._Conttn

	@Conttn.setter
	def Conttn(self, value):
		self._Conttn = value if value is not None else base_types.UninitialisedField(self, 'Conttn', TrueFalseIndicator, False)

	@Conttn.deleter
	def Conttn(self):
		del self._Conttn
		self._Conttn = base_types.UninitialisedField(self, 'Conttn', TrueFalseIndicator, False)

	@property
	def Crdhldr(self):
		return self._Crdhldr

	@Crdhldr.setter
	def Crdhldr(self, value):
		self._Crdhldr = value if value is not None else base_types.UninitialisedField(self, 'Crdhldr', Cardholder23, False)

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = base_types.UninitialisedField(self, 'Crdhldr', Cardholder23, False)

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if value is not None else base_types.UninitialisedField(self, 'Crrctn', CorrectionIdentification1, False)

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = base_types.UninitialisedField(self, 'Crrctn', CorrectionIdentification1, False)

	@property
	def CstmrDvc(self):
		return self._CstmrDvc

	@CstmrDvc.setter
	def CstmrDvc(self, value):
		self._CstmrDvc = value if value is not None else base_types.UninitialisedField(self, 'CstmrDvc', CustomerDevice6, False)

	@CstmrDvc.deleter
	def CstmrDvc(self):
		del self._CstmrDvc
		self._CstmrDvc = base_types.UninitialisedField(self, 'CstmrDvc', CustomerDevice6, False)

	@property
	def DataRcrd(self):
		return self._DataRcrd

	@DataRcrd.setter
	def DataRcrd(self, value):
		self._DataRcrd = value if value is not None else base_types.UninitialisedField(self, 'DataRcrd', ATICALaxProcessing, False)

	@DataRcrd.deleter
	def DataRcrd(self):
		del self._DataRcrd
		self._DataRcrd = base_types.UninitialisedField(self, 'DataRcrd', ATICALaxProcessing, False)

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if value is not None else base_types.UninitialisedField(self, 'Dstn', DestinationData1, False)

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = base_types.UninitialisedField(self, 'Dstn', DestinationData1, False)

	@property
	def FileActnScp(self):
		return self._FileActnScp

	@FileActnScp.setter
	def FileActnScp(self, value):
		self._FileActnScp = value if value is not None else base_types.UninitialisedField(self, 'FileActnScp', FileActionScope1Code, False)

	@FileActnScp.deleter
	def FileActnScp(self):
		del self._FileActnScp
		self._FileActnScp = base_types.UninitialisedField(self, 'FileActnScp', FileActionScope1Code, False)

	@property
	def FileActnTp(self):
		return self._FileActnTp

	@FileActnTp.setter
	def FileActnTp(self, value):
		self._FileActnTp = value if value is not None else base_types.UninitialisedField(self, 'FileActnTp', FileActionType3Code, False)

	@FileActnTp.deleter
	def FileActnTp(self):
		del self._FileActnTp
		self._FileActnTp = base_types.UninitialisedField(self, 'FileActnTp', FileActionType3Code, False)

	@property
	def FileNm(self):
		return self._FileNm

	@FileNm.setter
	def FileNm(self, value):
		self._FileNm = value if value is not None else base_types.UninitialisedField(self, 'FileNm', Max140Text, False)

	@FileNm.deleter
	def FileNm(self):
		del self._FileNm
		self._FileNm = base_types.UninitialisedField(self, 'FileNm', Max140Text, False)

	@property
	def FileSctyCd(self):
		return self._FileSctyCd

	@FileSctyCd.setter
	def FileSctyCd(self, value):
		self._FileSctyCd = value if value is not None else base_types.UninitialisedField(self, 'FileSctyCd', Max35Text, False)

	@FileSctyCd.deleter
	def FileSctyCd(self):
		del self._FileSctyCd
		self._FileSctyCd = base_types.UninitialisedField(self, 'FileSctyCd', Max35Text, False)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat7Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat7Code, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header72, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header72, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', IssuerData1, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', IssuerData1, False)

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if value is not None else base_types.UninitialisedField(self, 'Orgtr', OriginatorData2, False)

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = base_types.UninitialisedField(self, 'Orgtr', OriginatorData2, False)

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
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode6, False)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode6, False)

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdData', EncryptedData2, True)

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = base_types.UninitialisedField(self, 'PrtctdData', EncryptedData2, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def Pyee(self):
		return self._Pyee

	@Pyee.setter
	def Pyee(self, value):
		self._Pyee = value if value is not None else base_types.UninitialisedField(self, 'Pyee', PayeeData1, False)

	@Pyee.deleter
	def Pyee(self):
		del self._Pyee
		self._Pyee = base_types.UninitialisedField(self, 'Pyee', PayeeData1, False)

	@property
	def Pyer(self):
		return self._Pyer

	@Pyer.setter
	def Pyer(self, value):
		self._Pyer = value if value is not None else base_types.UninitialisedField(self, 'Pyer', PayerData1, False)

	@Pyer.deleter
	def Pyer(self):
		del self._Pyer
		self._Pyer = base_types.UninitialisedField(self, 'Pyer', PayerData1, False)

	@property
	def Rcncltn(self):
		return self._Rcncltn

	@Rcncltn.setter
	def Rcncltn(self, value):
		self._Rcncltn = value if value is not None else base_types.UninitialisedField(self, 'Rcncltn', Reconciliation5, False)

	@Rcncltn.deleter
	def Rcncltn(self):
		del self._Rcncltn
		self._Rcncltn = base_types.UninitialisedField(self, 'Rcncltn', Reconciliation5, False)

	@property
	def Rcvr(self):
		return self._Rcvr

	@Rcvr.setter
	def Rcvr(self, value):
		self._Rcvr = value if value is not None else base_types.UninitialisedField(self, 'Rcvr', ReceiverData1, False)

	@Rcvr.deleter
	def Rcvr(self):
		del self._Rcvr
		self._Rcvr = base_types.UninitialisedField(self, 'Rcvr', ReceiverData1, False)

	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if value is not None else base_types.UninitialisedField(self, 'RspnCd', ISO8583ResponseCode, False)

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = base_types.UninitialisedField(self, 'RspnCd', ISO8583ResponseCode, False)

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
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', SenderData1, False)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', SenderData1, False)

	@property
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if value is not None else base_types.UninitialisedField(self, 'SttlmSvc', SettlementService7, False)

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = base_types.UninitialisedField(self, 'SttlmSvc', SettlementService7, False)

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
	def Termnl(self):
		return self._Termnl

	@Termnl.setter
	def Termnl(self, value):
		self._Termnl = value if value is not None else base_types.UninitialisedField(self, 'Termnl', Terminal10, False)

	@Termnl.deleter
	def Termnl(self):
		del self._Termnl
		self._Termnl = base_types.UninitialisedField(self, 'Termnl', Terminal10, False)

	@property
	def Tkn(self):
		return self._Tkn

	@Tkn.setter
	def Tkn(self, value):
		self._Tkn = value if value is not None else base_types.UninitialisedField(self, 'Tkn', Token5, False)

	@Tkn.deleter
	def Tkn(self):
		del self._Tkn
		self._Tkn = base_types.UninitialisedField(self, 'Tkn', Token5, False)

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
	def Wllt(self):
		return self._Wllt

	@Wllt.setter
	def Wllt(self, value):
		self._Wllt = value if value is not None else base_types.UninitialisedField(self, 'Wllt', Wallet4, False)

	@Wllt.deleter
	def Wllt(self):
		del self._Wllt
		self._Wllt = base_types.UninitialisedField(self, 'Wllt', Wallet4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptr', type=AcceptorData3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=AcquirerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Conttn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crrctn', type=CorrectionIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrDvc', type=CustomerDevice6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DataRcrd', type=ATICALaxProcessing, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileActnScp', type=FileActionScope1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileActnTp', type=FileActionType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FileSctyCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat7Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=IssuerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POICmpnt', type=PointOfInteractionComponent16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pyee', type=PayeeData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PayerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wllt', type=Wallet4, min=0, max=1, mutex_group=None, array=False),
	))