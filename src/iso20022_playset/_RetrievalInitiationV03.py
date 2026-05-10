from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .DisputeData4 import DisputeData4
from .RetrievalFulfilmentInstructions3 import RetrievalFulfilmentInstructions3
from .SpecialProgrammeQualification2 import SpecialProgrammeQualification2
from .Header71 import Header71
from .ProtectedData2 import ProtectedData2
from .AdditionalFee3 import AdditionalFee3
from .OriginalTransaction3 import OriginalTransaction3
from .TransactionIdentification54 import TransactionIdentification54
from .Terminal8 import Terminal8
from .Token2 import Token2
from .DateTime2 import DateTime2
from .AdditionalData2 import AdditionalData2
from .PartyIdentification287 import PartyIdentification287
from .CardData13 import CardData13
from .PartyIdentification285 import PartyIdentification285
from .ProcessingResult25 import ProcessingResult25
from .Jurisdiction2 import Jurisdiction2
from .Wallet3 import Wallet3
from .Reconciliation4 import Reconciliation4
from .SettlementService6 import SettlementService6
from .ContentInformationType41 import ContentInformationType41
from .ProgrammeMode5 import ProgrammeMode5
from .Context24 import Context24
from .TransactionCharacteristics3 import TransactionCharacteristics3
from .PartyIdentification286 import PartyIdentification286

class RetrievalInitiationV03(base_types._BaseFieldType):

	__slots__ = ["_SctyTrlr", "_Pyee", "_RtrvlFlfmtInstrs", "_TxChrtcs", "_RtrvlFlfmtDstn", "_ConvsDtTm", "_Issr", "_Rcncltn", "_AddtlFee", "_Tkn", "_Termnl", "_Hdr", "_Orgtr", "_Prgrmm", "_TxId", "_Wllt", "_DsptData", "_PrtctdData", "_SplmtryData", "_OrgnlTx", "_Pyer", "_Accptr", "_Card", "_Acqrr", "_AddtlData", "_Rcvr", "_Cntxt", "_Sndr", "_SpclPrgrmmQlfctn", "_Dstn", "_Jursdctn", "_PrcgRslt", "_SttlmSvc"]
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
	def RtrvlFlfmtInstrs(self):
		return self._RtrvlFlfmtInstrs

	@RtrvlFlfmtInstrs.setter
	def RtrvlFlfmtInstrs(self, value):
		self._RtrvlFlfmtInstrs = value if type(value) != base_types.auto else self.make_default("RtrvlFlfmtInstrs")

	@RtrvlFlfmtInstrs.deleter
	def RtrvlFlfmtInstrs(self):
		del self._RtrvlFlfmtInstrs
		self._RtrvlFlfmtInstrs = None

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
	def RtrvlFlfmtDstn(self):
		return self._RtrvlFlfmtDstn

	@RtrvlFlfmtDstn.setter
	def RtrvlFlfmtDstn(self, value):
		self._RtrvlFlfmtDstn = value if type(value) != base_types.auto else self.make_default("RtrvlFlfmtDstn")

	@RtrvlFlfmtDstn.deleter
	def RtrvlFlfmtDstn(self):
		del self._RtrvlFlfmtDstn
		self._RtrvlFlfmtDstn = None

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
	def DsptData(self):
		return self._DsptData

	@DsptData.setter
	def DsptData(self, value):
		self._DsptData = value if type(value) != base_types.auto else self.make_default("DsptData")

	@DsptData.deleter
	def DsptData(self):
		del self._DsptData
		self._DsptData = None

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
	def SttlmSvc(self):
		return self._SttlmSvc

	@SttlmSvc.setter
	def SttlmSvc(self, value):
		self._SttlmSvc = value if type(value) != base_types.auto else self.make_default("SttlmSvc")

	@SttlmSvc.deleter
	def SttlmSvc(self):
		del self._SttlmSvc
		self._SttlmSvc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyTrlr', type=ContentInformationType41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyee', type=PartyIdentification287, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlFlfmtInstrs', type=RetrievalFulfilmentInstructions3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxChrtcs', type=TransactionCharacteristics3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlFlfmtDstn', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDtTm', type=DateTime2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcncltn', type=Reconciliation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tkn', type=Token2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termnl', type=Terminal8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header71, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgrmm', type=ProgrammeMode5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification54, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wllt', type=Wallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DsptData', type=DisputeData4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTx', type=OriginalTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pyer', type=PartyIdentification287, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Accptr', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=CardData13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=PartyIdentification286, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rcvr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=Context24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpclPrgrmmQlfctn', type=SpecialProgrammeQualification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dstn', type=PartyIdentification286, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Jursdctn', type=Jurisdiction2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgRslt', type=ProcessingResult25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSvc', type=SettlementService6, min=0, max=1, mutex_group=None, array=False),
	))

