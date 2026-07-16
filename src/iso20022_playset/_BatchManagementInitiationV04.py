# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import BatchManagementType3Code
from . import ContentInformationType41
from . import CorrectionIdentification1
from . import DestinationData1
from . import EncryptedData2
from . import Exact12Text
from . import Exact15Text
from . import Header72
from . import ISO8583ResponseCode
from . import ISODateTime
from . import Jurisdiction2
from . import Max12NumericText
from . import Max15NumericText
from . import Max35Binary
from . import Max70Text
from . import Number
from . import OriginatorData2
from . import ProcessingResult32
from . import ProgrammeMode6
from . import ReceiverData1
from . import Reconciliation5
from . import SenderData1
from . import SettlementService7
from . import TrueFalseIndicator

class BatchManagementInitiationV04(base_types._BaseFieldType):

	__slots__ = ["_BtchChcksm", "_BtchId", "_BtchIdList", "_BtchMgmtTp", "_ChckptId", "_ColltnChcksm", "_ColltnId", "_ColltnIdList", "_ColltnSz", "_Conttn", "_Crrctn", "_Dstn", "_Hdr", "_Jursdctn", "_LifeCyclId", "_MsgSeqNb", "_MsgsBfrAck", "_NbOfBtchsInColltn", "_NbOfMsgs", "_NtlData", "_OrgnlBtchId", "_OrgnlColltnId", "_OrgnlRspnCd", "_Orgtr", "_PostvAck", "_PrcgRslt", "_Prgrmm", "_PrtctdData", "_PrvtData", "_Rcncltn", "_Rcvr", "_ReqAck", "_RmngMsgsInColltn", "_RtrvlRefNb", "_SctyTrlr", "_Sndr", "_SttlmSvc", "_SysTracAudtNb", "_TrnsmssnDtTm"]
	@property
	def BtchChcksm(self):
		return self._BtchChcksm

	@BtchChcksm.setter
	def BtchChcksm(self, value):
		self._BtchChcksm = value if value is not None else base_types.UninitialisedField(self, 'BtchChcksm', Max35Binary, False)

	@BtchChcksm.deleter
	def BtchChcksm(self):
		del self._BtchChcksm
		self._BtchChcksm = base_types.UninitialisedField(self, 'BtchChcksm', Max35Binary, False)

	@property
	def BtchId(self):
		return self._BtchId

	@BtchId.setter
	def BtchId(self, value):
		self._BtchId = value if value is not None else base_types.UninitialisedField(self, 'BtchId', Max70Text, False)

	@BtchId.deleter
	def BtchId(self):
		del self._BtchId
		self._BtchId = base_types.UninitialisedField(self, 'BtchId', Max70Text, False)

	@property
	def BtchIdList(self):
		return self._BtchIdList

	@BtchIdList.setter
	def BtchIdList(self, value):
		self._BtchIdList = value if value is not None else base_types.UninitialisedField(self, 'BtchIdList', Max70Text, True)

	@BtchIdList.deleter
	def BtchIdList(self):
		del self._BtchIdList
		self._BtchIdList = base_types.UninitialisedField(self, 'BtchIdList', Max70Text, True)

	@property
	def BtchMgmtTp(self):
		return self._BtchMgmtTp

	@BtchMgmtTp.setter
	def BtchMgmtTp(self, value):
		self._BtchMgmtTp = value if value is not None else base_types.UninitialisedField(self, 'BtchMgmtTp', BatchManagementType3Code, False)

	@BtchMgmtTp.deleter
	def BtchMgmtTp(self):
		del self._BtchMgmtTp
		self._BtchMgmtTp = base_types.UninitialisedField(self, 'BtchMgmtTp', BatchManagementType3Code, False)

	@property
	def ChckptId(self):
		return self._ChckptId

	@ChckptId.setter
	def ChckptId(self, value):
		self._ChckptId = value if value is not None else base_types.UninitialisedField(self, 'ChckptId', Max70Text, False)

	@ChckptId.deleter
	def ChckptId(self):
		del self._ChckptId
		self._ChckptId = base_types.UninitialisedField(self, 'ChckptId', Max70Text, False)

	@property
	def ColltnChcksm(self):
		return self._ColltnChcksm

	@ColltnChcksm.setter
	def ColltnChcksm(self, value):
		self._ColltnChcksm = value if value is not None else base_types.UninitialisedField(self, 'ColltnChcksm', Max35Binary, False)

	@ColltnChcksm.deleter
	def ColltnChcksm(self):
		del self._ColltnChcksm
		self._ColltnChcksm = base_types.UninitialisedField(self, 'ColltnChcksm', Max35Binary, False)

	@property
	def ColltnId(self):
		return self._ColltnId

	@ColltnId.setter
	def ColltnId(self, value):
		self._ColltnId = value if value is not None else base_types.UninitialisedField(self, 'ColltnId', Max70Text, False)

	@ColltnId.deleter
	def ColltnId(self):
		del self._ColltnId
		self._ColltnId = base_types.UninitialisedField(self, 'ColltnId', Max70Text, False)

	@property
	def ColltnIdList(self):
		return self._ColltnIdList

	@ColltnIdList.setter
	def ColltnIdList(self, value):
		self._ColltnIdList = value if value is not None else base_types.UninitialisedField(self, 'ColltnIdList', Max70Text, True)

	@ColltnIdList.deleter
	def ColltnIdList(self):
		del self._ColltnIdList
		self._ColltnIdList = base_types.UninitialisedField(self, 'ColltnIdList', Max70Text, True)

	@property
	def ColltnSz(self):
		return self._ColltnSz

	@ColltnSz.setter
	def ColltnSz(self, value):
		self._ColltnSz = value if value is not None else base_types.UninitialisedField(self, 'ColltnSz', Number, False)

	@ColltnSz.deleter
	def ColltnSz(self):
		del self._ColltnSz
		self._ColltnSz = base_types.UninitialisedField(self, 'ColltnSz', Number, False)

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
	def MsgSeqNb(self):
		return self._MsgSeqNb

	@MsgSeqNb.setter
	def MsgSeqNb(self, value):
		self._MsgSeqNb = value if value is not None else base_types.UninitialisedField(self, 'MsgSeqNb', Max15NumericText, False)

	@MsgSeqNb.deleter
	def MsgSeqNb(self):
		del self._MsgSeqNb
		self._MsgSeqNb = base_types.UninitialisedField(self, 'MsgSeqNb', Max15NumericText, False)

	@property
	def MsgsBfrAck(self):
		return self._MsgsBfrAck

	@MsgsBfrAck.setter
	def MsgsBfrAck(self, value):
		self._MsgsBfrAck = value if value is not None else base_types.UninitialisedField(self, 'MsgsBfrAck', Number, False)

	@MsgsBfrAck.deleter
	def MsgsBfrAck(self):
		del self._MsgsBfrAck
		self._MsgsBfrAck = base_types.UninitialisedField(self, 'MsgsBfrAck', Number, False)

	@property
	def NbOfBtchsInColltn(self):
		return self._NbOfBtchsInColltn

	@NbOfBtchsInColltn.setter
	def NbOfBtchsInColltn(self, value):
		self._NbOfBtchsInColltn = value if value is not None else base_types.UninitialisedField(self, 'NbOfBtchsInColltn', Number, False)

	@NbOfBtchsInColltn.deleter
	def NbOfBtchsInColltn(self):
		del self._NbOfBtchsInColltn
		self._NbOfBtchsInColltn = base_types.UninitialisedField(self, 'NbOfBtchsInColltn', Number, False)

	@property
	def NbOfMsgs(self):
		return self._NbOfMsgs

	@NbOfMsgs.setter
	def NbOfMsgs(self, value):
		self._NbOfMsgs = value if value is not None else base_types.UninitialisedField(self, 'NbOfMsgs', Number, False)

	@NbOfMsgs.deleter
	def NbOfMsgs(self):
		del self._NbOfMsgs
		self._NbOfMsgs = base_types.UninitialisedField(self, 'NbOfMsgs', Number, False)

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
	def OrgnlBtchId(self):
		return self._OrgnlBtchId

	@OrgnlBtchId.setter
	def OrgnlBtchId(self, value):
		self._OrgnlBtchId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlBtchId', Max70Text, False)

	@OrgnlBtchId.deleter
	def OrgnlBtchId(self):
		del self._OrgnlBtchId
		self._OrgnlBtchId = base_types.UninitialisedField(self, 'OrgnlBtchId', Max70Text, False)

	@property
	def OrgnlColltnId(self):
		return self._OrgnlColltnId

	@OrgnlColltnId.setter
	def OrgnlColltnId(self, value):
		self._OrgnlColltnId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlColltnId', Max70Text, False)

	@OrgnlColltnId.deleter
	def OrgnlColltnId(self):
		del self._OrgnlColltnId
		self._OrgnlColltnId = base_types.UninitialisedField(self, 'OrgnlColltnId', Max70Text, False)

	@property
	def OrgnlRspnCd(self):
		return self._OrgnlRspnCd

	@OrgnlRspnCd.setter
	def OrgnlRspnCd(self, value):
		self._OrgnlRspnCd = value if value is not None else base_types.UninitialisedField(self, 'OrgnlRspnCd', ISO8583ResponseCode, False)

	@OrgnlRspnCd.deleter
	def OrgnlRspnCd(self):
		del self._OrgnlRspnCd
		self._OrgnlRspnCd = base_types.UninitialisedField(self, 'OrgnlRspnCd', ISO8583ResponseCode, False)

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
	def PostvAck(self):
		return self._PostvAck

	@PostvAck.setter
	def PostvAck(self, value):
		self._PostvAck = value if value is not None else base_types.UninitialisedField(self, 'PostvAck', TrueFalseIndicator, False)

	@PostvAck.deleter
	def PostvAck(self):
		del self._PostvAck
		self._PostvAck = base_types.UninitialisedField(self, 'PostvAck', TrueFalseIndicator, False)

	@property
	def PrcgRslt(self):
		return self._PrcgRslt

	@PrcgRslt.setter
	def PrcgRslt(self, value):
		self._PrcgRslt = value if value is not None else base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult32, False)

	@PrcgRslt.deleter
	def PrcgRslt(self):
		del self._PrcgRslt
		self._PrcgRslt = base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult32, False)

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode6, True)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode6, True)

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
	def ReqAck(self):
		return self._ReqAck

	@ReqAck.setter
	def ReqAck(self, value):
		self._ReqAck = value if value is not None else base_types.UninitialisedField(self, 'ReqAck', TrueFalseIndicator, False)

	@ReqAck.deleter
	def ReqAck(self):
		del self._ReqAck
		self._ReqAck = base_types.UninitialisedField(self, 'ReqAck', TrueFalseIndicator, False)

	@property
	def RmngMsgsInColltn(self):
		return self._RmngMsgsInColltn

	@RmngMsgsInColltn.setter
	def RmngMsgsInColltn(self, value):
		self._RmngMsgsInColltn = value if value is not None else base_types.UninitialisedField(self, 'RmngMsgsInColltn', Number, False)

	@RmngMsgsInColltn.deleter
	def RmngMsgsInColltn(self):
		del self._RmngMsgsInColltn
		self._RmngMsgsInColltn = base_types.UninitialisedField(self, 'RmngMsgsInColltn', Number, False)

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
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if value is not None else base_types.UninitialisedField(self, 'TrnsmssnDtTm', ISODateTime, False)

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = base_types.UninitialisedField(self, 'TrnsmssnDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchChcksm', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchIdList', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BtchMgmtTp', type=BatchManagementType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckptId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ColltnChcksm', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ColltnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ColltnIdList', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ColltnSz', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Conttn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crrctn', type=CorrectionIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgSeqNb', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgsBfrAck', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfBtchsInColltn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfMsgs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlBtchId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlColltnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlRspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PostvAck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqAck', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngMsgsInColltn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))