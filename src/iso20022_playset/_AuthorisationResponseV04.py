# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountBalance3 import AccountBalance3
from ._AccountDetails4 import AccountDetails4
from ._AddendumData7 import AddendumData7
from ._AdditionalAmounts4 import AdditionalAmounts4
from ._AdditionalData2 import AdditionalData2
from ._AdditionalFee3 import AdditionalFee3
from ._AdditionalService2 import AdditionalService2
from ._CardData12 import CardData12
from ._Cardholder22 import Cardholder22
from ._ContentInformationType41 import ContentInformationType41
from ._Context20 import Context20
from ._DateTime2 import DateTime2
from ._Header71 import Header71
from ._Instalment6 import Instalment6
from ._Jurisdiction2 import Jurisdiction2
from ._Max10KHexBinaryText import Max10KHexBinaryText
from ._OriginalDataElements3 import OriginalDataElements3
from ._PartyIdentification285 import PartyIdentification285
from ._PartyIdentification286 import PartyIdentification286
from ._ProcessingResult22 import ProcessingResult22
from ._ProgrammeMode5 import ProgrammeMode5
from ._ProtectedData2 import ProtectedData2
from ._Reconciliation4 import Reconciliation4
from ._RiskContext3 import RiskContext3
from ._SettlementService6 import SettlementService6
from ._SpecialProgrammeQualification2 import SpecialProgrammeQualification2
from ._StrongCustomerAuthentication2 import StrongCustomerAuthentication2
from ._SupplementaryData1 import SupplementaryData1
from ._Terminal8 import Terminal8
from ._Token2 import Token2
from ._TransactionAmounts3 import TransactionAmounts3
from ._TransactionCharacteristics1 import TransactionCharacteristics1
from ._TransactionIdentification57 import TransactionIdentification57
from ._Verification7 import Verification7
from ._Wallet3 import Wallet3

class AuthorisationResponseV04(base_types._BaseFieldType):

	__slots__ = ["_Accptr", "_AcctBal", "_AcctFr", "_AcctTo", "_Acqrr", "_AdddmData", "_AddtlAmt", "_AddtlData", "_AddtlFee", "_AddtlSvc", "_Card", "_Cntxt", "_ConvsDtTm", "_Crdhldr", "_Dstn", "_Hdr", "_ICCRltdData", "_Instlmt", "_Issr", "_Jursdctn", "_OrgnlDataElmts", "_Orgtr", "_PrcgRslt", "_Prgrmm", "_PrtctdData", "_Rcncltn", "_Rcvr", "_Rsk", "_SctyTrlr", "_Sndr", "_SpclPrgrmmQlfctn", "_SplmtryData", "_StrngCstmrAuthntcn", "_SttlmSvc", "_Termnl", "_Tkn", "_TxAmts", "_TxChrtcs", "_TxId", "_Vrfctn", "_Wllt"]
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
	def AdddmData(self):
		return self._AdddmData

	@AdddmData.setter
	def AdddmData(self, value):
		self._AdddmData = value if type(value) != base_types.auto else self.make_default("AdddmData")

	@AdddmData.deleter
	def AdddmData(self):
		del self._AdddmData
		self._AdddmData = None

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
	def OrgnlDataElmts(self):
		return self._OrgnlDataElmts

	@OrgnlDataElmts.setter
	def OrgnlDataElmts(self, value):
		self._OrgnlDataElmts = value if type(value) != base_types.auto else self.make_default("OrgnlDataElmts")

	@OrgnlDataElmts.deleter
	def OrgnlDataElmts(self):
		del self._OrgnlDataElmts
		self._OrgnlDataElmts = None

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
		base_types.FieldEntry(name='Accptr', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctBal', type=AccountBalance3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctFr', type=AccountDetails4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTo', type=AccountDetails4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=PartyIdentification286, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdddmData', type=AddendumData7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAmt', type=AdditionalAmounts4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlSvc', type=AdditionalService2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Card', type=CardData12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=Context20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDtTm', type=DateTime2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdhldr', type=Cardholder22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10KHexBinaryText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instlmt', type=Instalment6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlDataElmts', type=OriginalDataElements3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsk', type=RiskContext3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclPrgrmmQlfctn', type=SpecialProgrammeQualification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StrngCstmrAuthntcn', type=StrongCustomerAuthentication2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tkn', type=Token2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmts', type=TransactionAmounts3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChrtcs', type=TransactionCharacteristics1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrfctn', type=Verification7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Wllt', type=Wallet3, min=0, max=1, mutex_group=None, array=False),
	))