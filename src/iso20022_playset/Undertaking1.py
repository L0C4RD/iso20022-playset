from . import base_types
from .Max35Text import Max35Text
from .YesNoIndicator import YesNoIndicator
from .UndertakingName1Code import UndertakingName1Code
from .CommunicationChannel1 import CommunicationChannel1
from .UnderlyingTradeTransaction1 import UnderlyingTradeTransaction1
from .Max350Text import Max350Text
from .UndertakingAmount1 import UndertakingAmount1
from .PartyIdentification43 import PartyIdentification43
from .Max2000Text import Max2000Text
from .GovernanceRules1 import GovernanceRules1
from .PartyAndType1 import PartyAndType1
from .UndertakingWording1 import UndertakingWording1
from .ExternalTypeOfParty1Code import ExternalTypeOfParty1Code
from .AutomaticVariation1 import AutomaticVariation1
from .UndertakingType1Choice import UndertakingType1Choice
from .Presentation4 import Presentation4
from .CashAccount28 import CashAccount28
from .Document9 import Document9
from .Undertaking2 import Undertaking2
from .ExpiryDetails2 import ExpiryDetails2

class Undertaking1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_ConfChrgsPyblBy", "_PresntnDtls", "_Purp", "_TrfInd", "_ScndAdvsgPty", "_Nm", "_ConfInd", "_PrtlDmndInd", "_AddtlApplInf", "_Oblgr", "_OblgrSttlmAcct", "_XpryDtls", "_Cnfrmr", "_ApplcntRefNb", "_AddtlPty", "_CntrUdrtkg", "_Issr", "_MltplDmndInd", "_OblgrChrgAcct", "_NclsdFile", "_TrfChrgsPyblBy", "_UdrtkgWrdg", "_GovncRulesAndLaw", "_AutomtcAmtVartn", "_AdvsgPty", "_DlvryChanl", "_Bnfcry", "_CntrUdrtkgInd", "_UdrtkgAmt", "_OblgrLbltyAcct", "_Applcnt", "_UndrlygTx"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def ConfChrgsPyblBy(self):
		return self._ConfChrgsPyblBy

	@ConfChrgsPyblBy.setter
	def ConfChrgsPyblBy(self, value):
		self._ConfChrgsPyblBy = value if type(value) != auto else self.make_default("ConfChrgsPyblBy")

	@ConfChrgsPyblBy.deleter
	def ConfChrgsPyblBy(self):
		del self._ConfChrgsPyblBy
		self._ConfChrgsPyblBy = None

	@property
	def PresntnDtls(self):
		return self._PresntnDtls

	@PresntnDtls.setter
	def PresntnDtls(self, value):
		self._PresntnDtls = value if type(value) != auto else self.make_default("PresntnDtls")

	@PresntnDtls.deleter
	def PresntnDtls(self):
		del self._PresntnDtls
		self._PresntnDtls = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def TrfInd(self):
		return self._TrfInd

	@TrfInd.setter
	def TrfInd(self, value):
		self._TrfInd = value if type(value) != auto else self.make_default("TrfInd")

	@TrfInd.deleter
	def TrfInd(self):
		del self._TrfInd
		self._TrfInd = None

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if type(value) != auto else self.make_default("ScndAdvsgPty")

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def ConfInd(self):
		return self._ConfInd

	@ConfInd.setter
	def ConfInd(self, value):
		self._ConfInd = value if type(value) != auto else self.make_default("ConfInd")

	@ConfInd.deleter
	def ConfInd(self):
		del self._ConfInd
		self._ConfInd = None

	@property
	def PrtlDmndInd(self):
		return self._PrtlDmndInd

	@PrtlDmndInd.setter
	def PrtlDmndInd(self, value):
		self._PrtlDmndInd = value if type(value) != auto else self.make_default("PrtlDmndInd")

	@PrtlDmndInd.deleter
	def PrtlDmndInd(self):
		del self._PrtlDmndInd
		self._PrtlDmndInd = None

	@property
	def AddtlApplInf(self):
		return self._AddtlApplInf

	@AddtlApplInf.setter
	def AddtlApplInf(self, value):
		self._AddtlApplInf = value if type(value) != auto else self.make_default("AddtlApplInf")

	@AddtlApplInf.deleter
	def AddtlApplInf(self):
		del self._AddtlApplInf
		self._AddtlApplInf = None

	@property
	def Oblgr(self):
		return self._Oblgr

	@Oblgr.setter
	def Oblgr(self, value):
		self._Oblgr = value if type(value) != auto else self.make_default("Oblgr")

	@Oblgr.deleter
	def Oblgr(self):
		del self._Oblgr
		self._Oblgr = None

	@property
	def OblgrSttlmAcct(self):
		return self._OblgrSttlmAcct

	@OblgrSttlmAcct.setter
	def OblgrSttlmAcct(self, value):
		self._OblgrSttlmAcct = value if type(value) != auto else self.make_default("OblgrSttlmAcct")

	@OblgrSttlmAcct.deleter
	def OblgrSttlmAcct(self):
		del self._OblgrSttlmAcct
		self._OblgrSttlmAcct = None

	@property
	def XpryDtls(self):
		return self._XpryDtls

	@XpryDtls.setter
	def XpryDtls(self, value):
		self._XpryDtls = value if type(value) != auto else self.make_default("XpryDtls")

	@XpryDtls.deleter
	def XpryDtls(self):
		del self._XpryDtls
		self._XpryDtls = None

	@property
	def Cnfrmr(self):
		return self._Cnfrmr

	@Cnfrmr.setter
	def Cnfrmr(self, value):
		self._Cnfrmr = value if type(value) != auto else self.make_default("Cnfrmr")

	@Cnfrmr.deleter
	def Cnfrmr(self):
		del self._Cnfrmr
		self._Cnfrmr = None

	@property
	def ApplcntRefNb(self):
		return self._ApplcntRefNb

	@ApplcntRefNb.setter
	def ApplcntRefNb(self, value):
		self._ApplcntRefNb = value if type(value) != auto else self.make_default("ApplcntRefNb")

	@ApplcntRefNb.deleter
	def ApplcntRefNb(self):
		del self._ApplcntRefNb
		self._ApplcntRefNb = None

	@property
	def AddtlPty(self):
		return self._AddtlPty

	@AddtlPty.setter
	def AddtlPty(self, value):
		self._AddtlPty = value if type(value) != auto else self.make_default("AddtlPty")

	@AddtlPty.deleter
	def AddtlPty(self):
		del self._AddtlPty
		self._AddtlPty = None

	@property
	def CntrUdrtkg(self):
		return self._CntrUdrtkg

	@CntrUdrtkg.setter
	def CntrUdrtkg(self, value):
		self._CntrUdrtkg = value if type(value) != auto else self.make_default("CntrUdrtkg")

	@CntrUdrtkg.deleter
	def CntrUdrtkg(self):
		del self._CntrUdrtkg
		self._CntrUdrtkg = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def MltplDmndInd(self):
		return self._MltplDmndInd

	@MltplDmndInd.setter
	def MltplDmndInd(self, value):
		self._MltplDmndInd = value if type(value) != auto else self.make_default("MltplDmndInd")

	@MltplDmndInd.deleter
	def MltplDmndInd(self):
		del self._MltplDmndInd
		self._MltplDmndInd = None

	@property
	def OblgrChrgAcct(self):
		return self._OblgrChrgAcct

	@OblgrChrgAcct.setter
	def OblgrChrgAcct(self, value):
		self._OblgrChrgAcct = value if type(value) != auto else self.make_default("OblgrChrgAcct")

	@OblgrChrgAcct.deleter
	def OblgrChrgAcct(self):
		del self._OblgrChrgAcct
		self._OblgrChrgAcct = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def TrfChrgsPyblBy(self):
		return self._TrfChrgsPyblBy

	@TrfChrgsPyblBy.setter
	def TrfChrgsPyblBy(self, value):
		self._TrfChrgsPyblBy = value if type(value) != auto else self.make_default("TrfChrgsPyblBy")

	@TrfChrgsPyblBy.deleter
	def TrfChrgsPyblBy(self):
		del self._TrfChrgsPyblBy
		self._TrfChrgsPyblBy = None

	@property
	def UdrtkgWrdg(self):
		return self._UdrtkgWrdg

	@UdrtkgWrdg.setter
	def UdrtkgWrdg(self, value):
		self._UdrtkgWrdg = value if type(value) != auto else self.make_default("UdrtkgWrdg")

	@UdrtkgWrdg.deleter
	def UdrtkgWrdg(self):
		del self._UdrtkgWrdg
		self._UdrtkgWrdg = None

	@property
	def GovncRulesAndLaw(self):
		return self._GovncRulesAndLaw

	@GovncRulesAndLaw.setter
	def GovncRulesAndLaw(self, value):
		self._GovncRulesAndLaw = value if type(value) != auto else self.make_default("GovncRulesAndLaw")

	@GovncRulesAndLaw.deleter
	def GovncRulesAndLaw(self):
		del self._GovncRulesAndLaw
		self._GovncRulesAndLaw = None

	@property
	def AutomtcAmtVartn(self):
		return self._AutomtcAmtVartn

	@AutomtcAmtVartn.setter
	def AutomtcAmtVartn(self, value):
		self._AutomtcAmtVartn = value if type(value) != auto else self.make_default("AutomtcAmtVartn")

	@AutomtcAmtVartn.deleter
	def AutomtcAmtVartn(self):
		del self._AutomtcAmtVartn
		self._AutomtcAmtVartn = None

	@property
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if type(value) != auto else self.make_default("AdvsgPty")

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = None

	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if type(value) != auto else self.make_default("DlvryChanl")

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = None

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if type(value) != auto else self.make_default("Bnfcry")

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = None

	@property
	def CntrUdrtkgInd(self):
		return self._CntrUdrtkgInd

	@CntrUdrtkgInd.setter
	def CntrUdrtkgInd(self, value):
		self._CntrUdrtkgInd = value if type(value) != auto else self.make_default("CntrUdrtkgInd")

	@CntrUdrtkgInd.deleter
	def CntrUdrtkgInd(self):
		del self._CntrUdrtkgInd
		self._CntrUdrtkgInd = None

	@property
	def UdrtkgAmt(self):
		return self._UdrtkgAmt

	@UdrtkgAmt.setter
	def UdrtkgAmt(self, value):
		self._UdrtkgAmt = value if type(value) != auto else self.make_default("UdrtkgAmt")

	@UdrtkgAmt.deleter
	def UdrtkgAmt(self):
		del self._UdrtkgAmt
		self._UdrtkgAmt = None

	@property
	def OblgrLbltyAcct(self):
		return self._OblgrLbltyAcct

	@OblgrLbltyAcct.setter
	def OblgrLbltyAcct(self, value):
		self._OblgrLbltyAcct = value if type(value) != auto else self.make_default("OblgrLbltyAcct")

	@OblgrLbltyAcct.deleter
	def OblgrLbltyAcct(self):
		del self._OblgrLbltyAcct
		self._OblgrLbltyAcct = None

	@property
	def Applcnt(self):
		return self._Applcnt

	@Applcnt.setter
	def Applcnt(self, value):
		self._Applcnt = value if type(value) != auto else self.make_default("Applcnt")

	@Applcnt.deleter
	def Applcnt(self):
		del self._Applcnt
		self._Applcnt = None

	@property
	def UndrlygTx(self):
		return self._UndrlygTx

	@UndrlygTx.setter
	def UndrlygTx(self, value):
		self._UndrlygTx = value if type(value) != auto else self.make_default("UndrlygTx")

	@UndrlygTx.deleter
	def UndrlygTx(self):
		del self._UndrlygTx
		self._UndrlygTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=UndertakingType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntnDtls', type=Presentation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=UndertakingName1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlDmndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlApplInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oblgr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrSttlmAcct', type=CashAccount28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtls', type=ExpiryDetails2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnfrmr', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplcntRefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPty', type=PartyAndType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CntrUdrtkg', type=Undertaking2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MltplDmndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrChrgAcct', type=CashAccount28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgWrdg', type=UndertakingWording1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovncRulesAndLaw', type=GovernanceRules1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutomtcAmtVartn', type=AutomaticVariation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification43, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CntrUdrtkgInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmt', type=UndertakingAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrLbltyAcct', type=CashAccount28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Applcnt', type=PartyIdentification43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygTx', type=UnderlyingTradeTransaction1, min=0, max=None, mutex_group=None, array=True),
	))

