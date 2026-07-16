# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import AcceptorData2
from . import AcquirerData1
from . import AdditionalFee4
from . import CardData17
from . import ContentInformationType41
from . import Context30
from . import DateTime2
from . import DestinationData1
from . import DisputeData5
from . import EncryptedData2
from . import Header72
from . import ISO8583ResponseCode
from . import IssuerData1
from . import Jurisdiction2
from . import OriginatorData2
from . import PayeeData1
from . import PayerData1
from . import ProcessingResult30
from . import ProgrammeMode6
from . import ReceiverData1
from . import Reconciliation5
from . import SenderData1
from . import SettlementService7
from . import Terminal12
from . import Token5
from . import TransactionCharacteristics6
from . import TransactionIdentification60
from . import TransactorData1
from . import Wallet4

class RetrievalFulfilmentResponseV04(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_Acqrr", "_AddtlFee", "_Card", "_Cntxt", "_ConvsDtTm", "_DsptData", "_Dstn", "_Hdr", "_Issr", "_Jursdctn", "_NtlData", "_OrgnlRspnCd", "_Orgtr", "_PrcgRslt", "_Prgrmm", "_PrtctdData", "_PrvtData", "_Pyee", "_Pyer", "_Rcncltn", "_Rcvr", "_RtrvlFlfmtInstrs", "_SctyTrlr", "_Sndr", "_SpclPrgrmmQlfctn", "_SttlmSvc", "_Termnl", "_Tkn", "_TxChrtcs", "_TxId", "_Txtr", "_Wllt"]
	@property
	def Accptr(self):
		return self._Accptr

	@Accptr.setter
	def Accptr(self, value):
		self._Accptr = value if value is not None else base_types.UninitialisedField(self, 'Accptr', AcceptorData2, False)

	@Accptr.deleter
	def Accptr(self):
		del self._Accptr
		self._Accptr = base_types.UninitialisedField(self, 'Accptr', AcceptorData2, False)

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
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', Context30, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', Context30, False)

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
	def DsptData(self):
		return self._DsptData

	@DsptData.setter
	def DsptData(self, value):
		self._DsptData = value if value is not None else base_types.UninitialisedField(self, 'DsptData', DisputeData5, True)

	@DsptData.deleter
	def DsptData(self):
		del self._DsptData
		self._DsptData = base_types.UninitialisedField(self, 'DsptData', DisputeData5, True)

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
	def PrcgRslt(self):
		return self._PrcgRslt

	@PrcgRslt.setter
	def PrcgRslt(self, value):
		self._PrcgRslt = value if value is not None else base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult30, False)

	@PrcgRslt.deleter
	def PrcgRslt(self):
		del self._PrcgRslt
		self._PrcgRslt = base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult30, False)

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
	def RtrvlFlfmtInstrs(self):
		return self._RtrvlFlfmtInstrs

	@RtrvlFlfmtInstrs.setter
	def RtrvlFlfmtInstrs(self, value):
		self._RtrvlFlfmtInstrs = value if value is not None else base_types.UninitialisedField(self, 'RtrvlFlfmtInstrs', ATICALaxProcessing, True)

	@RtrvlFlfmtInstrs.deleter
	def RtrvlFlfmtInstrs(self):
		del self._RtrvlFlfmtInstrs
		self._RtrvlFlfmtInstrs = base_types.UninitialisedField(self, 'RtrvlFlfmtInstrs', ATICALaxProcessing, True)

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
	def SpclPrgrmmQlfctn(self):
		return self._SpclPrgrmmQlfctn

	@SpclPrgrmmQlfctn.setter
	def SpclPrgrmmQlfctn(self, value):
		self._SpclPrgrmmQlfctn = value if value is not None else base_types.UninitialisedField(self, 'SpclPrgrmmQlfctn', ATICALaxProcessing, True)

	@SpclPrgrmmQlfctn.deleter
	def SpclPrgrmmQlfctn(self):
		del self._SpclPrgrmmQlfctn
		self._SpclPrgrmmQlfctn = base_types.UninitialisedField(self, 'SpclPrgrmmQlfctn', ATICALaxProcessing, True)

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
	def Termnl(self):
		return self._Termnl

	@Termnl.setter
	def Termnl(self, value):
		self._Termnl = value if value is not None else base_types.UninitialisedField(self, 'Termnl', Terminal12, False)

	@Termnl.deleter
	def Termnl(self):
		del self._Termnl
		self._Termnl = base_types.UninitialisedField(self, 'Termnl', Terminal12, False)

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
	def TxChrtcs(self):
		return self._TxChrtcs

	@TxChrtcs.setter
	def TxChrtcs(self, value):
		self._TxChrtcs = value if value is not None else base_types.UninitialisedField(self, 'TxChrtcs', TransactionCharacteristics6, False)

	@TxChrtcs.deleter
	def TxChrtcs(self):
		del self._TxChrtcs
		self._TxChrtcs = base_types.UninitialisedField(self, 'TxChrtcs', TransactionCharacteristics6, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentification60, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentification60, False)

	@property
	def Txtr(self):
		return self._Txtr

	@Txtr.setter
	def Txtr(self, value):
		self._Txtr = value if value is not None else base_types.UninitialisedField(self, 'Txtr', TransactorData1, False)

	@Txtr.deleter
	def Txtr(self):
		del self._Txtr
		self._Txtr = base_types.UninitialisedField(self, 'Txtr', TransactorData1, False)

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
		base_types.FieldEntry(name='Accptr', type=AcceptorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=AcquirerData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=Context30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDtTm', type=DateTime2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptData', type=DisputeData5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=IssuerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlRspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pyee', type=PayeeData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PayerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlFlfmtInstrs', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclPrgrmmQlfctn', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChrtcs', type=TransactionCharacteristics6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification60, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txtr', type=TransactorData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wllt', type=Wallet4, min=0, max=1, mutex_group=None, array=False),
	))