# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import AcceptorData3
from . import AccountDetails4
from . import AcquirerData1
from . import AdditionalAmounts5
from . import AdditionalFee4
from . import AdditionalService3
from . import CardData17
from . import CardExchangeRate1
from . import Cardholder23
from . import Context26
from . import CustomerDevice6
from . import DateTime2
from . import DepositDetails4
from . import DestinationData1
from . import DisputeData5
from . import DisputeDocumentation2
from . import FundingService4
from . import IssuerData1
from . import Jurisdiction2
from . import OriginalTransactionCharacteristics2
from . import OriginatorData2
from . import PayeeData1
from . import PayerData1
from . import PointOfInteractionComponent16
from . import ProcessingResult29
from . import ProgrammeMode7
from . import ReceiverData1
from . import Reconciliation5
from . import RiskContext4
from . import SenderData1
from . import SettlementService7
from . import Terminal13
from . import Token5
from . import TransactionAmounts5
from . import TransactionIdentification60
from . import Verification9
from . import Wallet4

class OriginalTransaction4(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_AcctFr", "_AcctTo", "_Acqrr", "_AddtlAmt", "_AddtlFee", "_AddtlSvc", "_Card", "_Cntxt", "_ConvsDtTm", "_Crdhldr", "_CstmrDvc", "_Dcmnttn", "_DpstDtls", "_DsptData", "_Dstn", "_FndsSvcs", "_Issr", "_Jursdctn", "_Orgtr", "_POICmpnt", "_PrcgRslt", "_Prgrmm", "_Pyee", "_Pyer", "_Rcncltn", "_Rcvr", "_Rsk", "_Sndr", "_SpclPrgrmmQlfctn", "_SttlmSvc", "_Termnl", "_Tkn", "_TxAmts", "_TxChrtcs", "_TxId", "_Vrfctn", "_Wllt", "_XchgRate"]
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
	def AcctFr(self):
		return self._AcctFr

	@AcctFr.setter
	def AcctFr(self, value):
		self._AcctFr = value if value is not None else base_types.UninitialisedField(self, 'AcctFr', AccountDetails4, False)

	@AcctFr.deleter
	def AcctFr(self):
		del self._AcctFr
		self._AcctFr = base_types.UninitialisedField(self, 'AcctFr', AccountDetails4, False)

	@property
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if value is not None else base_types.UninitialisedField(self, 'AcctTo', AccountDetails4, False)

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = base_types.UninitialisedField(self, 'AcctTo', AccountDetails4, False)

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
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlAmt', AdditionalAmounts5, True)

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = base_types.UninitialisedField(self, 'AddtlAmt', AdditionalAmounts5, True)

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
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if value is not None else base_types.UninitialisedField(self, 'AddtlSvc', AdditionalService3, True)

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = base_types.UninitialisedField(self, 'AddtlSvc', AdditionalService3, True)

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
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', Context26, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', Context26, False)

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
		self._Crdhldr = value if value is not None else base_types.UninitialisedField(self, 'Crdhldr', Cardholder23, True)

	@Crdhldr.deleter
	def Crdhldr(self):
		del self._Crdhldr
		self._Crdhldr = base_types.UninitialisedField(self, 'Crdhldr', Cardholder23, True)

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
	def Dcmnttn(self):
		return self._Dcmnttn

	@Dcmnttn.setter
	def Dcmnttn(self, value):
		self._Dcmnttn = value if value is not None else base_types.UninitialisedField(self, 'Dcmnttn', DisputeDocumentation2, True)

	@Dcmnttn.deleter
	def Dcmnttn(self):
		del self._Dcmnttn
		self._Dcmnttn = base_types.UninitialisedField(self, 'Dcmnttn', DisputeDocumentation2, True)

	@property
	def DpstDtls(self):
		return self._DpstDtls

	@DpstDtls.setter
	def DpstDtls(self, value):
		self._DpstDtls = value if value is not None else base_types.UninitialisedField(self, 'DpstDtls', DepositDetails4, True)

	@DpstDtls.deleter
	def DpstDtls(self):
		del self._DpstDtls
		self._DpstDtls = base_types.UninitialisedField(self, 'DpstDtls', DepositDetails4, True)

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
	def FndsSvcs(self):
		return self._FndsSvcs

	@FndsSvcs.setter
	def FndsSvcs(self, value):
		self._FndsSvcs = value if value is not None else base_types.UninitialisedField(self, 'FndsSvcs', FundingService4, False)

	@FndsSvcs.deleter
	def FndsSvcs(self):
		del self._FndsSvcs
		self._FndsSvcs = base_types.UninitialisedField(self, 'FndsSvcs', FundingService4, False)

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
	def PrcgRslt(self):
		return self._PrcgRslt

	@PrcgRslt.setter
	def PrcgRslt(self, value):
		self._PrcgRslt = value if value is not None else base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult29, False)

	@PrcgRslt.deleter
	def PrcgRslt(self):
		del self._PrcgRslt
		self._PrcgRslt = base_types.UninitialisedField(self, 'PrcgRslt', ProcessingResult29, False)

	@property
	def Prgrmm(self):
		return self._Prgrmm

	@Prgrmm.setter
	def Prgrmm(self, value):
		self._Prgrmm = value if value is not None else base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode7, False)

	@Prgrmm.deleter
	def Prgrmm(self):
		del self._Prgrmm
		self._Prgrmm = base_types.UninitialisedField(self, 'Prgrmm', ProgrammeMode7, False)

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
	def Rsk(self):
		return self._Rsk

	@Rsk.setter
	def Rsk(self, value):
		self._Rsk = value if value is not None else base_types.UninitialisedField(self, 'Rsk', RiskContext4, True)

	@Rsk.deleter
	def Rsk(self):
		del self._Rsk
		self._Rsk = base_types.UninitialisedField(self, 'Rsk', RiskContext4, True)

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
		self._Termnl = value if value is not None else base_types.UninitialisedField(self, 'Termnl', Terminal13, False)

	@Termnl.deleter
	def Termnl(self):
		del self._Termnl
		self._Termnl = base_types.UninitialisedField(self, 'Termnl', Terminal13, False)

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
	def TxAmts(self):
		return self._TxAmts

	@TxAmts.setter
	def TxAmts(self, value):
		self._TxAmts = value if value is not None else base_types.UninitialisedField(self, 'TxAmts', TransactionAmounts5, False)

	@TxAmts.deleter
	def TxAmts(self):
		del self._TxAmts
		self._TxAmts = base_types.UninitialisedField(self, 'TxAmts', TransactionAmounts5, False)

	@property
	def TxChrtcs(self):
		return self._TxChrtcs

	@TxChrtcs.setter
	def TxChrtcs(self, value):
		self._TxChrtcs = value if value is not None else base_types.UninitialisedField(self, 'TxChrtcs', OriginalTransactionCharacteristics2, False)

	@TxChrtcs.deleter
	def TxChrtcs(self):
		del self._TxChrtcs
		self._TxChrtcs = base_types.UninitialisedField(self, 'TxChrtcs', OriginalTransactionCharacteristics2, False)

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
	def Vrfctn(self):
		return self._Vrfctn

	@Vrfctn.setter
	def Vrfctn(self, value):
		self._Vrfctn = value if value is not None else base_types.UninitialisedField(self, 'Vrfctn', Verification9, True)

	@Vrfctn.deleter
	def Vrfctn(self):
		del self._Vrfctn
		self._Vrfctn = base_types.UninitialisedField(self, 'Vrfctn', Verification9, True)

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

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', CardExchangeRate1, True)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', CardExchangeRate1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptr', type=AcceptorData3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctFr', type=AccountDetails4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTo', type=AccountDetails4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=AcquirerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAmt', type=AdditionalAmounts5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlSvc', type=AdditionalService3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=Context26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDtTm', type=DateTime2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrDvc', type=CustomerDevice6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dcmnttn', type=DisputeDocumentation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DpstDtls', type=DepositDetails4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DsptData', type=DisputeData5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndsSvcs', type=FundingService4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=IssuerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POICmpnt', type=PointOfInteractionComponent16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyee', type=PayeeData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PayerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsk', type=RiskContext4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclPrgrmmQlfctn', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmts', type=TransactionAmounts5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChrtcs', type=OriginalTransactionCharacteristics2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification60, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrfctn', type=Verification9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Wllt', type=Wallet4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=CardExchangeRate1, min=0, max=None, mutex_group=None, array=True),
	))