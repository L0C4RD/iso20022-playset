from . import base_types
from ._AutomaticVariation1 import AutomaticVariation1
from ._CommunicationChannel1 import CommunicationChannel1
from ._Document9 import Document9
from ._ExpiryDetails1 import ExpiryDetails1
from ._ExternalTypeOfParty1Code import ExternalTypeOfParty1Code
from ._GovernanceRules1 import GovernanceRules1
from ._ISODate import ISODate
from ._IssuanceType1Code import IssuanceType1Code
from ._Max2000Text import Max2000Text
from ._Max35Text import Max35Text
from ._Narrative1 import Narrative1
from ._PartyAndType1 import PartyAndType1
from ._PartyIdentification43 import PartyIdentification43
from ._PostalAddress12 import PostalAddress12
from ._Presentation1 import Presentation1
from ._UnderlyingTradeTransaction1 import UnderlyingTradeTransaction1
from ._Undertaking4 import Undertaking4
from ._UndertakingAmount1 import UndertakingAmount1
from ._UndertakingIssuanceName1Code import UndertakingIssuanceName1Code
from ._UndertakingType1Choice import UndertakingType1Choice
from ._YesNoIndicator import YesNoIndicator

class Undertaking3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AddtlPty", "_AdvsgPty", "_Applcnt", "_AutomtcAmtVartn", "_Bnfcry", "_ConfChrgsPyblBy", "_ConfInd", "_ConfPtyTp", "_DlvryChanl", "_DtOfIssnc", "_GovncRulesAndLaw", "_Id", "_IssncTp", "_Issr", "_MltplDmndInd", "_NclsdFile", "_Nm", "_PlcOfIsse", "_PresntnDtls", "_PrtlDmndInd", "_ReqdLclUdrtkg", "_ScndAdvsgPty", "_Tp", "_TrfChrgsPyblBy", "_TrfInd", "_UdrtkgAmt", "_UdrtkgTermsAndConds", "_UndrlygTx", "_XpryDtls"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AddtlPty(self):
		return self._AddtlPty

	@AddtlPty.setter
	def AddtlPty(self, value):
		self._AddtlPty = value if type(value) != base_types.auto else self.make_default("AddtlPty")

	@AddtlPty.deleter
	def AddtlPty(self):
		del self._AddtlPty
		self._AddtlPty = None

	@property
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if type(value) != base_types.auto else self.make_default("AdvsgPty")

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = None

	@property
	def Applcnt(self):
		return self._Applcnt

	@Applcnt.setter
	def Applcnt(self, value):
		self._Applcnt = value if type(value) != base_types.auto else self.make_default("Applcnt")

	@Applcnt.deleter
	def Applcnt(self):
		del self._Applcnt
		self._Applcnt = None

	@property
	def AutomtcAmtVartn(self):
		return self._AutomtcAmtVartn

	@AutomtcAmtVartn.setter
	def AutomtcAmtVartn(self, value):
		self._AutomtcAmtVartn = value if type(value) != base_types.auto else self.make_default("AutomtcAmtVartn")

	@AutomtcAmtVartn.deleter
	def AutomtcAmtVartn(self):
		del self._AutomtcAmtVartn
		self._AutomtcAmtVartn = None

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if type(value) != base_types.auto else self.make_default("Bnfcry")

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = None

	@property
	def ConfChrgsPyblBy(self):
		return self._ConfChrgsPyblBy

	@ConfChrgsPyblBy.setter
	def ConfChrgsPyblBy(self, value):
		self._ConfChrgsPyblBy = value if type(value) != base_types.auto else self.make_default("ConfChrgsPyblBy")

	@ConfChrgsPyblBy.deleter
	def ConfChrgsPyblBy(self):
		del self._ConfChrgsPyblBy
		self._ConfChrgsPyblBy = None

	@property
	def ConfInd(self):
		return self._ConfInd

	@ConfInd.setter
	def ConfInd(self, value):
		self._ConfInd = value if type(value) != base_types.auto else self.make_default("ConfInd")

	@ConfInd.deleter
	def ConfInd(self):
		del self._ConfInd
		self._ConfInd = None

	@property
	def ConfPtyTp(self):
		return self._ConfPtyTp

	@ConfPtyTp.setter
	def ConfPtyTp(self, value):
		self._ConfPtyTp = value if type(value) != base_types.auto else self.make_default("ConfPtyTp")

	@ConfPtyTp.deleter
	def ConfPtyTp(self):
		del self._ConfPtyTp
		self._ConfPtyTp = None

	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if type(value) != base_types.auto else self.make_default("DlvryChanl")

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = None

	@property
	def DtOfIssnc(self):
		return self._DtOfIssnc

	@DtOfIssnc.setter
	def DtOfIssnc(self, value):
		self._DtOfIssnc = value if type(value) != base_types.auto else self.make_default("DtOfIssnc")

	@DtOfIssnc.deleter
	def DtOfIssnc(self):
		del self._DtOfIssnc
		self._DtOfIssnc = None

	@property
	def GovncRulesAndLaw(self):
		return self._GovncRulesAndLaw

	@GovncRulesAndLaw.setter
	def GovncRulesAndLaw(self, value):
		self._GovncRulesAndLaw = value if type(value) != base_types.auto else self.make_default("GovncRulesAndLaw")

	@GovncRulesAndLaw.deleter
	def GovncRulesAndLaw(self):
		del self._GovncRulesAndLaw
		self._GovncRulesAndLaw = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def IssncTp(self):
		return self._IssncTp

	@IssncTp.setter
	def IssncTp(self, value):
		self._IssncTp = value if type(value) != base_types.auto else self.make_default("IssncTp")

	@IssncTp.deleter
	def IssncTp(self):
		del self._IssncTp
		self._IssncTp = None

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
	def MltplDmndInd(self):
		return self._MltplDmndInd

	@MltplDmndInd.setter
	def MltplDmndInd(self, value):
		self._MltplDmndInd = value if type(value) != base_types.auto else self.make_default("MltplDmndInd")

	@MltplDmndInd.deleter
	def MltplDmndInd(self):
		del self._MltplDmndInd
		self._MltplDmndInd = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != base_types.auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def PlcOfIsse(self):
		return self._PlcOfIsse

	@PlcOfIsse.setter
	def PlcOfIsse(self, value):
		self._PlcOfIsse = value if type(value) != base_types.auto else self.make_default("PlcOfIsse")

	@PlcOfIsse.deleter
	def PlcOfIsse(self):
		del self._PlcOfIsse
		self._PlcOfIsse = None

	@property
	def PresntnDtls(self):
		return self._PresntnDtls

	@PresntnDtls.setter
	def PresntnDtls(self, value):
		self._PresntnDtls = value if type(value) != base_types.auto else self.make_default("PresntnDtls")

	@PresntnDtls.deleter
	def PresntnDtls(self):
		del self._PresntnDtls
		self._PresntnDtls = None

	@property
	def PrtlDmndInd(self):
		return self._PrtlDmndInd

	@PrtlDmndInd.setter
	def PrtlDmndInd(self, value):
		self._PrtlDmndInd = value if type(value) != base_types.auto else self.make_default("PrtlDmndInd")

	@PrtlDmndInd.deleter
	def PrtlDmndInd(self):
		del self._PrtlDmndInd
		self._PrtlDmndInd = None

	@property
	def ReqdLclUdrtkg(self):
		return self._ReqdLclUdrtkg

	@ReqdLclUdrtkg.setter
	def ReqdLclUdrtkg(self, value):
		self._ReqdLclUdrtkg = value if type(value) != base_types.auto else self.make_default("ReqdLclUdrtkg")

	@ReqdLclUdrtkg.deleter
	def ReqdLclUdrtkg(self):
		del self._ReqdLclUdrtkg
		self._ReqdLclUdrtkg = None

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if type(value) != base_types.auto else self.make_default("ScndAdvsgPty")

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TrfChrgsPyblBy(self):
		return self._TrfChrgsPyblBy

	@TrfChrgsPyblBy.setter
	def TrfChrgsPyblBy(self, value):
		self._TrfChrgsPyblBy = value if type(value) != base_types.auto else self.make_default("TrfChrgsPyblBy")

	@TrfChrgsPyblBy.deleter
	def TrfChrgsPyblBy(self):
		del self._TrfChrgsPyblBy
		self._TrfChrgsPyblBy = None

	@property
	def TrfInd(self):
		return self._TrfInd

	@TrfInd.setter
	def TrfInd(self, value):
		self._TrfInd = value if type(value) != base_types.auto else self.make_default("TrfInd")

	@TrfInd.deleter
	def TrfInd(self):
		del self._TrfInd
		self._TrfInd = None

	@property
	def UdrtkgAmt(self):
		return self._UdrtkgAmt

	@UdrtkgAmt.setter
	def UdrtkgAmt(self, value):
		self._UdrtkgAmt = value if type(value) != base_types.auto else self.make_default("UdrtkgAmt")

	@UdrtkgAmt.deleter
	def UdrtkgAmt(self):
		del self._UdrtkgAmt
		self._UdrtkgAmt = None

	@property
	def UdrtkgTermsAndConds(self):
		return self._UdrtkgTermsAndConds

	@UdrtkgTermsAndConds.setter
	def UdrtkgTermsAndConds(self, value):
		self._UdrtkgTermsAndConds = value if type(value) != base_types.auto else self.make_default("UdrtkgTermsAndConds")

	@UdrtkgTermsAndConds.deleter
	def UdrtkgTermsAndConds(self):
		del self._UdrtkgTermsAndConds
		self._UdrtkgTermsAndConds = None

	@property
	def UndrlygTx(self):
		return self._UndrlygTx

	@UndrlygTx.setter
	def UndrlygTx(self, value):
		self._UndrlygTx = value if type(value) != base_types.auto else self.make_default("UndrlygTx")

	@UndrlygTx.deleter
	def UndrlygTx(self):
		del self._UndrlygTx
		self._UndrlygTx = None

	@property
	def XpryDtls(self):
		return self._XpryDtls

	@XpryDtls.setter
	def XpryDtls(self, value):
		self._XpryDtls = value if type(value) != base_types.auto else self.make_default("XpryDtls")

	@XpryDtls.deleter
	def XpryDtls(self):
		del self._XpryDtls
		self._XpryDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlPty', type=PartyAndType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Applcnt', type=PartyIdentification43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AutomtcAmtVartn', type=AutomaticVariation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification43, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfPtyTp', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfIssnc', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovncRulesAndLaw', type=GovernanceRules1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncTp', type=IssuanceType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MltplDmndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=UndertakingIssuanceName1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfIsse', type=PostalAddress12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntnDtls', type=Presentation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlDmndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdLclUdrtkg', type=Undertaking4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=UndertakingType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmt', type=UndertakingAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgTermsAndConds', type=Narrative1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygTx', type=UnderlyingTradeTransaction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryDtls', type=ExpiryDetails1, min=1, max=1, mutex_group=None, array=False),
	))

