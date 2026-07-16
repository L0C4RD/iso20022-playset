# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AutomaticVariation1
from . import CashAccount28
from . import CommunicationChannel1
from . import Document9
from . import ExpiryDetails2
from . import ExternalTypeOfParty1Code
from . import GovernanceRules1
from . import Max2000Text
from . import Max350Text
from . import Max35Text
from . import PartyAndType1
from . import PartyIdentification43
from . import Presentation4
from . import UnderlyingTradeTransaction1
from . import Undertaking2
from . import UndertakingAmount1
from . import UndertakingName1Code
from . import UndertakingType1Choice
from . import UndertakingWording1
from . import YesNoIndicator

class Undertaking1(base_types._BaseFieldType):

	__slots__ = ["_AddtlApplInf", "_AddtlPty", "_AdvsgPty", "_Applcnt", "_ApplcntRefNb", "_AutomtcAmtVartn", "_Bnfcry", "_Cnfrmr", "_CntrUdrtkg", "_CntrUdrtkgInd", "_ConfChrgsPyblBy", "_ConfInd", "_DlvryChanl", "_GovncRulesAndLaw", "_Issr", "_MltplDmndInd", "_NclsdFile", "_Nm", "_Oblgr", "_OblgrChrgAcct", "_OblgrLbltyAcct", "_OblgrSttlmAcct", "_PresntnDtls", "_PrtlDmndInd", "_Purp", "_ScndAdvsgPty", "_Tp", "_TrfChrgsPyblBy", "_TrfInd", "_UdrtkgAmt", "_UdrtkgWrdg", "_UndrlygTx", "_XpryDtls"]
	@property
	def AddtlApplInf(self):
		return self._AddtlApplInf

	@AddtlApplInf.setter
	def AddtlApplInf(self, value):
		self._AddtlApplInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlApplInf', Max2000Text, True)

	@AddtlApplInf.deleter
	def AddtlApplInf(self):
		del self._AddtlApplInf
		self._AddtlApplInf = base_types.UninitialisedField(self, 'AddtlApplInf', Max2000Text, True)

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
	def ApplcntRefNb(self):
		return self._ApplcntRefNb

	@ApplcntRefNb.setter
	def ApplcntRefNb(self, value):
		self._ApplcntRefNb = value if value is not None else base_types.UninitialisedField(self, 'ApplcntRefNb', Max35Text, False)

	@ApplcntRefNb.deleter
	def ApplcntRefNb(self):
		del self._ApplcntRefNb
		self._ApplcntRefNb = base_types.UninitialisedField(self, 'ApplcntRefNb', Max35Text, False)

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
	def Cnfrmr(self):
		return self._Cnfrmr

	@Cnfrmr.setter
	def Cnfrmr(self, value):
		self._Cnfrmr = value if value is not None else base_types.UninitialisedField(self, 'Cnfrmr', PartyIdentification43, False)

	@Cnfrmr.deleter
	def Cnfrmr(self):
		del self._Cnfrmr
		self._Cnfrmr = base_types.UninitialisedField(self, 'Cnfrmr', PartyIdentification43, False)

	@property
	def CntrUdrtkg(self):
		return self._CntrUdrtkg

	@CntrUdrtkg.setter
	def CntrUdrtkg(self, value):
		self._CntrUdrtkg = value if value is not None else base_types.UninitialisedField(self, 'CntrUdrtkg', Undertaking2, False)

	@CntrUdrtkg.deleter
	def CntrUdrtkg(self):
		del self._CntrUdrtkg
		self._CntrUdrtkg = base_types.UninitialisedField(self, 'CntrUdrtkg', Undertaking2, False)

	@property
	def CntrUdrtkgInd(self):
		return self._CntrUdrtkgInd

	@CntrUdrtkgInd.setter
	def CntrUdrtkgInd(self, value):
		self._CntrUdrtkgInd = value if value is not None else base_types.UninitialisedField(self, 'CntrUdrtkgInd', YesNoIndicator, False)

	@CntrUdrtkgInd.deleter
	def CntrUdrtkgInd(self):
		del self._CntrUdrtkgInd
		self._CntrUdrtkgInd = base_types.UninitialisedField(self, 'CntrUdrtkgInd', YesNoIndicator, False)

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
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', UndertakingName1Code, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', UndertakingName1Code, False)

	@property
	def Oblgr(self):
		return self._Oblgr

	@Oblgr.setter
	def Oblgr(self, value):
		self._Oblgr = value if value is not None else base_types.UninitialisedField(self, 'Oblgr', PartyIdentification43, False)

	@Oblgr.deleter
	def Oblgr(self):
		del self._Oblgr
		self._Oblgr = base_types.UninitialisedField(self, 'Oblgr', PartyIdentification43, False)

	@property
	def OblgrChrgAcct(self):
		return self._OblgrChrgAcct

	@OblgrChrgAcct.setter
	def OblgrChrgAcct(self, value):
		self._OblgrChrgAcct = value if value is not None else base_types.UninitialisedField(self, 'OblgrChrgAcct', CashAccount28, False)

	@OblgrChrgAcct.deleter
	def OblgrChrgAcct(self):
		del self._OblgrChrgAcct
		self._OblgrChrgAcct = base_types.UninitialisedField(self, 'OblgrChrgAcct', CashAccount28, False)

	@property
	def OblgrLbltyAcct(self):
		return self._OblgrLbltyAcct

	@OblgrLbltyAcct.setter
	def OblgrLbltyAcct(self, value):
		self._OblgrLbltyAcct = value if value is not None else base_types.UninitialisedField(self, 'OblgrLbltyAcct', CashAccount28, False)

	@OblgrLbltyAcct.deleter
	def OblgrLbltyAcct(self):
		del self._OblgrLbltyAcct
		self._OblgrLbltyAcct = base_types.UninitialisedField(self, 'OblgrLbltyAcct', CashAccount28, False)

	@property
	def OblgrSttlmAcct(self):
		return self._OblgrSttlmAcct

	@OblgrSttlmAcct.setter
	def OblgrSttlmAcct(self, value):
		self._OblgrSttlmAcct = value if value is not None else base_types.UninitialisedField(self, 'OblgrSttlmAcct', CashAccount28, False)

	@OblgrSttlmAcct.deleter
	def OblgrSttlmAcct(self):
		del self._OblgrSttlmAcct
		self._OblgrSttlmAcct = base_types.UninitialisedField(self, 'OblgrSttlmAcct', CashAccount28, False)

	@property
	def PresntnDtls(self):
		return self._PresntnDtls

	@PresntnDtls.setter
	def PresntnDtls(self, value):
		self._PresntnDtls = value if value is not None else base_types.UninitialisedField(self, 'PresntnDtls', Presentation4, False)

	@PresntnDtls.deleter
	def PresntnDtls(self):
		del self._PresntnDtls
		self._PresntnDtls = base_types.UninitialisedField(self, 'PresntnDtls', Presentation4, False)

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
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Max350Text, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Max350Text, False)

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
	def UdrtkgWrdg(self):
		return self._UdrtkgWrdg

	@UdrtkgWrdg.setter
	def UdrtkgWrdg(self, value):
		self._UdrtkgWrdg = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgWrdg', UndertakingWording1, False)

	@UdrtkgWrdg.deleter
	def UdrtkgWrdg(self):
		del self._UdrtkgWrdg
		self._UdrtkgWrdg = base_types.UninitialisedField(self, 'UdrtkgWrdg', UndertakingWording1, False)

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
		self._XpryDtls = value if value is not None else base_types.UninitialisedField(self, 'XpryDtls', ExpiryDetails2, False)

	@XpryDtls.deleter
	def XpryDtls(self):
		del self._XpryDtls
		self._XpryDtls = base_types.UninitialisedField(self, 'XpryDtls', ExpiryDetails2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlApplInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlPty', type=PartyAndType1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Applcnt', type=PartyIdentification43, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplcntRefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutomtcAmtVartn', type=AutomaticVariation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification43, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cnfrmr', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrUdrtkg', type=Undertaking2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrUdrtkgInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryChanl', type=CommunicationChannel1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovncRulesAndLaw', type=GovernanceRules1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MltplDmndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=UndertakingName1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrChrgAcct', type=CashAccount28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrLbltyAcct', type=CashAccount28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgrSttlmAcct', type=CashAccount28, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntnDtls', type=Presentation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlDmndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=UndertakingType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfChrgsPyblBy', type=ExternalTypeOfParty1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmt', type=UndertakingAmount1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgWrdg', type=UndertakingWording1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTx', type=UnderlyingTradeTransaction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryDtls', type=ExpiryDetails2, min=1, max=1, mutex_group=None, array=False),
	))