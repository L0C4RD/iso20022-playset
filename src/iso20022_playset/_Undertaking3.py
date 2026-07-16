# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AutomaticVariation1
from . import CommunicationChannel1
from . import Document9
from . import ExpiryDetails1
from . import ExternalTypeOfParty1Code
from . import GovernanceRules1
from . import ISODate
from . import IssuanceType1Code
from . import Max2000Text
from . import Max35Text
from . import Narrative1
from . import PartyAndType1
from . import PartyIdentification43
from . import PostalAddress12
from . import Presentation1
from . import UnderlyingTradeTransaction1
from . import Undertaking4
from . import UndertakingAmount1
from . import UndertakingIssuanceName1Code
from . import UndertakingType1Choice
from . import YesNoIndicator

class Undertaking3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AddtlPty", "_AdvsgPty", "_Applcnt", "_AutomtcAmtVartn", "_Bnfcry", "_ConfChrgsPyblBy", "_ConfInd", "_ConfPtyTp", "_DlvryChanl", "_DtOfIssnc", "_GovncRulesAndLaw", "_Id", "_IssncTp", "_Issr", "_MltplDmndInd", "_NclsdFile", "_Nm", "_PlcOfIsse", "_PresntnDtls", "_PrtlDmndInd", "_ReqdLclUdrtkg", "_ScndAdvsgPty", "_Tp", "_TrfChrgsPyblBy", "_TrfInd", "_UdrtkgAmt", "_UdrtkgTermsAndConds", "_UndrlygTx", "_XpryDtls"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def AddtlPty(self):
		return self._AddtlPty

	@AddtlPty.setter
	def AddtlPty(self, value):
		self._AddtlPty = value if value is not None else base_types.UninitialisedField(self, 'AddtlPty', PartyAndType1, True)

	@AddtlPty.deleter
	def AddtlPty(self):
		del self._AddtlPty
		self._AddtlPty = base_types.UninitialisedField(self, 'AddtlPty', PartyAndType1, True)

	@property
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if value is not None else base_types.UninitialisedField(self, 'AdvsgPty', PartyIdentification43, False)

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = base_types.UninitialisedField(self, 'AdvsgPty', PartyIdentification43, False)

	@property
	def Applcnt(self):
		return self._Applcnt

	@Applcnt.setter
	def Applcnt(self, value):
		self._Applcnt = value if value is not None else base_types.UninitialisedField(self, 'Applcnt', PartyIdentification43, True)

	@Applcnt.deleter
	def Applcnt(self):
		del self._Applcnt
		self._Applcnt = base_types.UninitialisedField(self, 'Applcnt', PartyIdentification43, True)

	@property
	def AutomtcAmtVartn(self):
		return self._AutomtcAmtVartn

	@AutomtcAmtVartn.setter
	def AutomtcAmtVartn(self, value):
		self._AutomtcAmtVartn = value if value is not None else base_types.UninitialisedField(self, 'AutomtcAmtVartn', AutomaticVariation1, True)

	@AutomtcAmtVartn.deleter
	def AutomtcAmtVartn(self):
		del self._AutomtcAmtVartn
		self._AutomtcAmtVartn = base_types.UninitialisedField(self, 'AutomtcAmtVartn', AutomaticVariation1, True)

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if value is not None else base_types.UninitialisedField(self, 'Bnfcry', PartyIdentification43, True)

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = base_types.UninitialisedField(self, 'Bnfcry', PartyIdentification43, True)

	@property
	def ConfChrgsPyblBy(self):
		return self._ConfChrgsPyblBy

	@ConfChrgsPyblBy.setter
	def ConfChrgsPyblBy(self, value):
		self._ConfChrgsPyblBy = value if value is not None else base_types.UninitialisedField(self, 'ConfChrgsPyblBy', ExternalTypeOfParty1Code, False)

	@ConfChrgsPyblBy.deleter
	def ConfChrgsPyblBy(self):
		del self._ConfChrgsPyblBy
		self._ConfChrgsPyblBy = base_types.UninitialisedField(self, 'ConfChrgsPyblBy', ExternalTypeOfParty1Code, False)

	@property
	def ConfInd(self):
		return self._ConfInd

	@ConfInd.setter
	def ConfInd(self, value):
		self._ConfInd = value if value is not None else base_types.UninitialisedField(self, 'ConfInd', YesNoIndicator, False)

	@ConfInd.deleter
	def ConfInd(self):
		del self._ConfInd
		self._ConfInd = base_types.UninitialisedField(self, 'ConfInd', YesNoIndicator, False)

	@property
	def ConfPtyTp(self):
		return self._ConfPtyTp

	@ConfPtyTp.setter
	def ConfPtyTp(self, value):
		self._ConfPtyTp = value if value is not None else base_types.UninitialisedField(self, 'ConfPtyTp', ExternalTypeOfParty1Code, False)

	@ConfPtyTp.deleter
	def ConfPtyTp(self):
		del self._ConfPtyTp
		self._ConfPtyTp = base_types.UninitialisedField(self, 'ConfPtyTp', ExternalTypeOfParty1Code, False)

	@property
	def DlvryChanl(self):
		return self._DlvryChanl

	@DlvryChanl.setter
	def DlvryChanl(self, value):
		self._DlvryChanl = value if value is not None else base_types.UninitialisedField(self, 'DlvryChanl', CommunicationChannel1, False)

	@DlvryChanl.deleter
	def DlvryChanl(self):
		del self._DlvryChanl
		self._DlvryChanl = base_types.UninitialisedField(self, 'DlvryChanl', CommunicationChannel1, False)

	@property
	def DtOfIssnc(self):
		return self._DtOfIssnc

	@DtOfIssnc.setter
	def DtOfIssnc(self, value):
		self._DtOfIssnc = value if value is not None else base_types.UninitialisedField(self, 'DtOfIssnc', ISODate, False)

	@DtOfIssnc.deleter
	def DtOfIssnc(self):
		del self._DtOfIssnc
		self._DtOfIssnc = base_types.UninitialisedField(self, 'DtOfIssnc', ISODate, False)

	@property
	def GovncRulesAndLaw(self):
		return self._GovncRulesAndLaw

	@GovncRulesAndLaw.setter
	def GovncRulesAndLaw(self, value):
		self._GovncRulesAndLaw = value if value is not None else base_types.UninitialisedField(self, 'GovncRulesAndLaw', GovernanceRules1, False)

	@GovncRulesAndLaw.deleter
	def GovncRulesAndLaw(self):
		del self._GovncRulesAndLaw
		self._GovncRulesAndLaw = base_types.UninitialisedField(self, 'GovncRulesAndLaw', GovernanceRules1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def IssncTp(self):
		return self._IssncTp

	@IssncTp.setter
	def IssncTp(self, value):
		self._IssncTp = value if value is not None else base_types.UninitialisedField(self, 'IssncTp', IssuanceType1Code, False)

	@IssncTp.deleter
	def IssncTp(self):
		del self._IssncTp
		self._IssncTp = base_types.UninitialisedField(self, 'IssncTp', IssuanceType1Code, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification43, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification43, False)

	@property
	def MltplDmndInd(self):
		return self._MltplDmndInd

	@MltplDmndInd.setter
	def MltplDmndInd(self, value):
		self._MltplDmndInd = value if value is not None else base_types.UninitialisedField(self, 'MltplDmndInd', YesNoIndicator, False)

	@MltplDmndInd.deleter
	def MltplDmndInd(self):
		del self._MltplDmndInd
		self._MltplDmndInd = base_types.UninitialisedField(self, 'MltplDmndInd', YesNoIndicator, False)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document9, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', UndertakingIssuanceName1Code, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', UndertakingIssuanceName1Code, False)

	@property
	def PlcOfIsse(self):
		return self._PlcOfIsse

	@PlcOfIsse.setter
	def PlcOfIsse(self, value):
		self._PlcOfIsse = value if value is not None else base_types.UninitialisedField(self, 'PlcOfIsse', PostalAddress12, False)

	@PlcOfIsse.deleter
	def PlcOfIsse(self):
		del self._PlcOfIsse
		self._PlcOfIsse = base_types.UninitialisedField(self, 'PlcOfIsse', PostalAddress12, False)

	@property
	def PresntnDtls(self):
		return self._PresntnDtls

	@PresntnDtls.setter
	def PresntnDtls(self, value):
		self._PresntnDtls = value if value is not None else base_types.UninitialisedField(self, 'PresntnDtls', Presentation1, False)

	@PresntnDtls.deleter
	def PresntnDtls(self):
		del self._PresntnDtls
		self._PresntnDtls = base_types.UninitialisedField(self, 'PresntnDtls', Presentation1, False)

	@property
	def PrtlDmndInd(self):
		return self._PrtlDmndInd

	@PrtlDmndInd.setter
	def PrtlDmndInd(self, value):
		self._PrtlDmndInd = value if value is not None else base_types.UninitialisedField(self, 'PrtlDmndInd', YesNoIndicator, False)

	@PrtlDmndInd.deleter
	def PrtlDmndInd(self):
		del self._PrtlDmndInd
		self._PrtlDmndInd = base_types.UninitialisedField(self, 'PrtlDmndInd', YesNoIndicator, False)

	@property
	def ReqdLclUdrtkg(self):
		return self._ReqdLclUdrtkg

	@ReqdLclUdrtkg.setter
	def ReqdLclUdrtkg(self, value):
		self._ReqdLclUdrtkg = value if value is not None else base_types.UninitialisedField(self, 'ReqdLclUdrtkg', Undertaking4, False)

	@ReqdLclUdrtkg.deleter
	def ReqdLclUdrtkg(self):
		del self._ReqdLclUdrtkg
		self._ReqdLclUdrtkg = base_types.UninitialisedField(self, 'ReqdLclUdrtkg', Undertaking4, False)

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if value is not None else base_types.UninitialisedField(self, 'ScndAdvsgPty', PartyIdentification43, False)

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = base_types.UninitialisedField(self, 'ScndAdvsgPty', PartyIdentification43, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', UndertakingType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', UndertakingType1Choice, False)

	@property
	def TrfChrgsPyblBy(self):
		return self._TrfChrgsPyblBy

	@TrfChrgsPyblBy.setter
	def TrfChrgsPyblBy(self, value):
		self._TrfChrgsPyblBy = value if value is not None else base_types.UninitialisedField(self, 'TrfChrgsPyblBy', ExternalTypeOfParty1Code, False)

	@TrfChrgsPyblBy.deleter
	def TrfChrgsPyblBy(self):
		del self._TrfChrgsPyblBy
		self._TrfChrgsPyblBy = base_types.UninitialisedField(self, 'TrfChrgsPyblBy', ExternalTypeOfParty1Code, False)

	@property
	def TrfInd(self):
		return self._TrfInd

	@TrfInd.setter
	def TrfInd(self, value):
		self._TrfInd = value if value is not None else base_types.UninitialisedField(self, 'TrfInd', YesNoIndicator, False)

	@TrfInd.deleter
	def TrfInd(self):
		del self._TrfInd
		self._TrfInd = base_types.UninitialisedField(self, 'TrfInd', YesNoIndicator, False)

	@property
	def UdrtkgAmt(self):
		return self._UdrtkgAmt

	@UdrtkgAmt.setter
	def UdrtkgAmt(self, value):
		self._UdrtkgAmt = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmt', UndertakingAmount1, False)

	@UdrtkgAmt.deleter
	def UdrtkgAmt(self):
		del self._UdrtkgAmt
		self._UdrtkgAmt = base_types.UninitialisedField(self, 'UdrtkgAmt', UndertakingAmount1, False)

	@property
	def UdrtkgTermsAndConds(self):
		return self._UdrtkgTermsAndConds

	@UdrtkgTermsAndConds.setter
	def UdrtkgTermsAndConds(self, value):
		self._UdrtkgTermsAndConds = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgTermsAndConds', Narrative1, True)

	@UdrtkgTermsAndConds.deleter
	def UdrtkgTermsAndConds(self):
		del self._UdrtkgTermsAndConds
		self._UdrtkgTermsAndConds = base_types.UninitialisedField(self, 'UdrtkgTermsAndConds', Narrative1, True)

	@property
	def UndrlygTx(self):
		return self._UndrlygTx

	@UndrlygTx.setter
	def UndrlygTx(self, value):
		self._UndrlygTx = value if value is not None else base_types.UninitialisedField(self, 'UndrlygTx', UnderlyingTradeTransaction1, True)

	@UndrlygTx.deleter
	def UndrlygTx(self):
		del self._UndrlygTx
		self._UndrlygTx = base_types.UninitialisedField(self, 'UndrlygTx', UnderlyingTradeTransaction1, True)

	@property
	def XpryDtls(self):
		return self._XpryDtls

	@XpryDtls.setter
	def XpryDtls(self, value):
		self._XpryDtls = value if value is not None else base_types.UninitialisedField(self, 'XpryDtls', ExpiryDetails1, False)

	@XpryDtls.deleter
	def XpryDtls(self):
		del self._XpryDtls
		self._XpryDtls = base_types.UninitialisedField(self, 'XpryDtls', ExpiryDetails1, False)

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