# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._AcceptorData2 import AcceptorData2
from ._AccountBalance4 import AccountBalance4
from ._AccountDetails4 import AccountDetails4
from ._AccountStatementData3 import AccountStatementData3
from ._AcquirerData1 import AcquirerData1
from ._AdditionalAmounts5 import AdditionalAmounts5
from ._AdditionalFee4 import AdditionalFee4
from ._AdditionalService3 import AdditionalService3
from ._BenefitSupportingData1 import BenefitSupportingData1
from ._CardAuthenticationData1 import CardAuthenticationData1
from ._CardData17 import CardData17
from ._Cardholder23 import Cardholder23
from ._ContentInformationType41 import ContentInformationType41
from ._Context27 import Context27
from ._DateTime2 import DateTime2
from ._DestinationData1 import DestinationData1
from ._EncryptedData2 import EncryptedData2
from ._Header72 import Header72
from ._ISO8583ResponseCode import ISO8583ResponseCode
from ._Instalment8 import Instalment8
from ._IssuerData1 import IssuerData1
from ._Jurisdiction2 import Jurisdiction2
from ._Max10KHexBinaryText import Max10KHexBinaryText
from ._OriginatorData2 import OriginatorData2
from ._PayeeData1 import PayeeData1
from ._PayerData1 import PayerData1
from ._ProcessingResult29 import ProcessingResult29
from ._ProgrammeMode6 import ProgrammeMode6
from ._ReceiverData1 import ReceiverData1
from ._Reconciliation5 import Reconciliation5
from ._RiskContext4 import RiskContext4
from ._SenderData1 import SenderData1
from ._SettlementService7 import SettlementService7
from ._StrongCustomerAuthentication2 import StrongCustomerAuthentication2
from ._Terminal12 import Terminal12
from ._Token5 import Token5
from ._TransactionAmounts6 import TransactionAmounts6
from ._TransactionCharacteristics5 import TransactionCharacteristics5
from ._TransactionIdentification60 import TransactionIdentification60
from ._TransactorData1 import TransactorData1
from ._Verification9 import Verification9
from ._Wallet4 import Wallet4

class InquiryVerificationResponseV04(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_AcctBal", "_AcctFr", "_AcctStmtData", "_AcctTo", "_Acqrr", "_AddtlAmt", "_AddtlFee", "_AddtlSvc", "_AuthntcnData", "_Bnfts", "_Card", "_CardPrgrmm", "_Cntxt", "_ConvsDtTm", "_Crdhldr", "_Dstn", "_Hdr", "_ICCRltdData", "_Instlmt", "_Issr", "_Jursdctn", "_NtlData", "_OrgnlRspnCd", "_Orgtr", "_PrcgRslt", "_PrtctdData", "_PrvtData", "_Pyee", "_Pyer", "_Rcncltn", "_Rcvr", "_Rsk", "_SctyTrlr", "_Sndr", "_SpclPrgrmmQlfctn", "_StrngCstmrAuthntcn", "_SttlmSvc", "_Termnl", "_Tkn", "_TxAmts", "_TxChrtcs", "_TxId", "_Txtr", "_Vrfctn", "_Wllt"]
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
	def AcctBal(self):
		return self._AcctBal

	@AcctBal.setter
	def AcctBal(self, value):
		self._AcctBal = value if type(value) != base_types.auto else self.make_default("AcctBal")

	@AcctBal.deleter
	def AcctBal(self):
		del self._AcctBal
		self._AcctBal = None

	@property
	def AcctFr(self):
		return self._AcctFr

	@AcctFr.setter
	def AcctFr(self, value):
		self._AcctFr = value if type(value) != base_types.auto else self.make_default("AcctFr")

	@AcctFr.deleter
	def AcctFr(self):
		del self._AcctFr
		self._AcctFr = None

	@property
	def AcctStmtData(self):
		return self._AcctStmtData

	@AcctStmtData.setter
	def AcctStmtData(self, value):
		self._AcctStmtData = value if type(value) != base_types.auto else self.make_default("AcctStmtData")

	@AcctStmtData.deleter
	def AcctStmtData(self):
		del self._AcctStmtData
		self._AcctStmtData = None

	@property
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if type(value) != base_types.auto else self.make_default("AcctTo")

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = None

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
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if type(value) != base_types.auto else self.make_default("AddtlAmt")

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = None

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
	def AuthntcnData(self):
		return self._AuthntcnData

	@AuthntcnData.setter
	def AuthntcnData(self, value):
		self._AuthntcnData = value if type(value) != base_types.auto else self.make_default("AuthntcnData")

	@AuthntcnData.deleter
	def AuthntcnData(self):
		del self._AuthntcnData
		self._AuthntcnData = None

	@property
	def Bnfts(self):
		return self._Bnfts

	@Bnfts.setter
	def Bnfts(self, value):
		self._Bnfts = value if type(value) != base_types.auto else self.make_default("Bnfts")

	@Bnfts.deleter
	def Bnfts(self):
		del self._Bnfts
		self._Bnfts = None

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
	def CardPrgrmm(self):
		return self._CardPrgrmm

	@CardPrgrmm.setter
	def CardPrgrmm(self, value):
		self._CardPrgrmm = value if type(value) != base_types.auto else self.make_default("CardPrgrmm")

	@CardPrgrmm.deleter
	def CardPrgrmm(self):
		del self._CardPrgrmm
		self._CardPrgrmm = None

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
	def OrgnlRspnCd(self):
		return self._OrgnlRspnCd

	@OrgnlRspnCd.setter
	def OrgnlRspnCd(self, value):
		self._OrgnlRspnCd = value if type(value) != base_types.auto else self.make_default("OrgnlRspnCd")

	@OrgnlRspnCd.deleter
	def OrgnlRspnCd(self):
		del self._OrgnlRspnCd
		self._OrgnlRspnCd = None

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
	def StrngCstmrAuthntcn(self):
		return self._StrngCstmrAuthntcn

	@StrngCstmrAuthntcn.setter
	def StrngCstmrAuthntcn(self, value):
		self._StrngCstmrAuthntcn = value if type(value) != base_types.auto else self.make_default("StrngCstmrAuthntcn")

	@StrngCstmrAuthntcn.deleter
	def StrngCstmrAuthntcn(self):
		del self._StrngCstmrAuthntcn
		self._StrngCstmrAuthntcn = None

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
	def TxAmts(self):
		return self._TxAmts

	@TxAmts.setter
	def TxAmts(self, value):
		self._TxAmts = value if type(value) != base_types.auto else self.make_default("TxAmts")

	@TxAmts.deleter
	def TxAmts(self):
		del self._TxAmts
		self._TxAmts = None

	@property
	def TxChrtcs(self):
		return self._TxChrtcs

	@TxChrtcs.setter
	def TxChrtcs(self, value):
		self._TxChrtcs = value if type(value) != base_types.auto else self.make_default("TxChrtcs")

	@TxChrtcs.deleter
	def TxChrtcs(self):
		del self._TxChrtcs
		self._TxChrtcs = None

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
	def Txtr(self):
		return self._Txtr

	@Txtr.setter
	def Txtr(self, value):
		self._Txtr = value if type(value) != base_types.auto else self.make_default("Txtr")

	@Txtr.deleter
	def Txtr(self):
		del self._Txtr
		self._Txtr = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptr', type=AcceptorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctBal', type=AccountBalance4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctFr', type=AccountDetails4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctStmtData', type=AccountStatementData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctTo', type=AccountDetails4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=AcquirerData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAmt', type=AdditionalAmounts5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlSvc', type=AdditionalService3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthntcnData', type=CardAuthenticationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bnfts', type=BenefitSupportingData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPrgrmm', type=ProgrammeMode6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cntxt', type=Context27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDtTm', type=DateTime2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=DestinationData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header72, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10KHexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instlmt', type=Instalment8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=IssuerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlRspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=OriginatorData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=EncryptedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pyee', type=PayeeData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PayerData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=ReceiverData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsk', type=RiskContext4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=SenderData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclPrgrmmQlfctn', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StrngCstmrAuthntcn', type=StrongCustomerAuthentication2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmts', type=TransactionAmounts6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChrtcs', type=TransactionCharacteristics5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification60, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txtr', type=TransactorData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrfctn', type=Verification9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Wllt', type=Wallet4, min=0, max=1, mutex_group=None, array=False),
	))