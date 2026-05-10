from . import base_types
from ._InvestmentAccountCategory1Choice import InvestmentAccountCategory1Choice
from ._AccountingStatus1Choice import AccountingStatus1Choice
from ._TransactionChannelType1Choice import TransactionChannelType1Choice
from ._AccountUsageType2Choice import AccountUsageType2Choice
from ._AccountType2Choice import AccountType2Choice
from ._DateAndDateTime1Choice import DateAndDateTime1Choice
from ._FiscalYear1Choice import FiscalYear1Choice
from ._YesNoIndicator import YesNoIndicator
from ._Provided1Code import Provided1Code
from ._Collateral1Code import Collateral1Code
from ._ModificationScope46 import ModificationScope46
from ._Max350Text import Max350Text
from ._PositionEffect3Code import PositionEffect3Code
from ._IncomePreference2Code import IncomePreference2Code
from ._Liability1Choice import Liability1Choice
from ._PartyIdentification125Choice import PartyIdentification125Choice
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._LanguageCode import LanguageCode
from ._StatementFrequencyReason2Choice import StatementFrequencyReason2Choice
from ._Number import Number
from ._Reinvestment4 import Reinvestment4
from ._LetterIntent1 import LetterIntent1
from ._Eligible1Code import Eligible1Code
from ._TaxExemptionReason2Choice import TaxExemptionReason2Choice
from ._BlockedStatusReason2Choice import BlockedStatusReason2Choice
from ._TaxWithholdingMethod3Code import TaxWithholdingMethod3Code
from ._AccountStatusUpdateInstruction1 import AccountStatusUpdateInstruction1
from ._ThirdPartyRights2 import ThirdPartyRights2
from ._ModificationScope42 import ModificationScope42
from ._Max35Text import Max35Text
from ._LevelOfControl1Choice import LevelOfControl1Choice
from ._OwnershipType2Choice import OwnershipType2Choice
from ._RoundingParameters1 import RoundingParameters1
from ._TaxReporting3 import TaxReporting3

class InvestmentAccount75(base_types._BaseFieldType):

	__slots__ = ["_Lblty", "_IncmPref", "_Coll", "_ModfdFinInstrmDtls", "_Pldgg", "_ReqrdSgntriesNb", "_RinvstmtDtls", "_ThrdPtyRghts", "_Nm", "_RndgDtls", "_AcmltnRghtRef", "_OpngDt", "_OwnrshTp", "_FrgnStsCertfctn", "_StmtFrqcy", "_ModfdInvstrPrfl", "_Lang", "_AcctSvcr", "_FsclYr", "_RefCcy", "_AcctSgntrDtTm", "_AcctUsgTp", "_TaxXmptn", "_Dsgnt", "_TaxRptg", "_AcctStsUpdInstr", "_TaxWhldgMtd", "_InvstmtAcctCtgy", "_BlckdSts", "_PrcgOrdr", "_AcctgSts", "_ClsgDt", "_LttrInttDtls", "_PwrOfAttnyLvlOfCtrl", "_Tp", "_TxChanlTp", "_NegInd", "_FndFmlyNm"]
	@property
	def AcctSgntrDtTm(self):
		return self._AcctSgntrDtTm

	@AcctSgntrDtTm.setter
	def AcctSgntrDtTm(self, value):
		self._AcctSgntrDtTm = value if type(value) != base_types.auto else self.make_default("AcctSgntrDtTm")

	@AcctSgntrDtTm.deleter
	def AcctSgntrDtTm(self):
		del self._AcctSgntrDtTm
		self._AcctSgntrDtTm = None

	@property
	def AcctStsUpdInstr(self):
		return self._AcctStsUpdInstr

	@AcctStsUpdInstr.setter
	def AcctStsUpdInstr(self, value):
		self._AcctStsUpdInstr = value if type(value) != base_types.auto else self.make_default("AcctStsUpdInstr")

	@AcctStsUpdInstr.deleter
	def AcctStsUpdInstr(self):
		del self._AcctStsUpdInstr
		self._AcctStsUpdInstr = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def AcctUsgTp(self):
		return self._AcctUsgTp

	@AcctUsgTp.setter
	def AcctUsgTp(self, value):
		self._AcctUsgTp = value if type(value) != base_types.auto else self.make_default("AcctUsgTp")

	@AcctUsgTp.deleter
	def AcctUsgTp(self):
		del self._AcctUsgTp
		self._AcctUsgTp = None

	@property
	def AcctgSts(self):
		return self._AcctgSts

	@AcctgSts.setter
	def AcctgSts(self, value):
		self._AcctgSts = value if type(value) != base_types.auto else self.make_default("AcctgSts")

	@AcctgSts.deleter
	def AcctgSts(self):
		del self._AcctgSts
		self._AcctgSts = None

	@property
	def AcmltnRghtRef(self):
		return self._AcmltnRghtRef

	@AcmltnRghtRef.setter
	def AcmltnRghtRef(self, value):
		self._AcmltnRghtRef = value if type(value) != base_types.auto else self.make_default("AcmltnRghtRef")

	@AcmltnRghtRef.deleter
	def AcmltnRghtRef(self):
		del self._AcmltnRghtRef
		self._AcmltnRghtRef = None

	@property
	def BlckdSts(self):
		return self._BlckdSts

	@BlckdSts.setter
	def BlckdSts(self, value):
		self._BlckdSts = value if type(value) != base_types.auto else self.make_default("BlckdSts")

	@BlckdSts.deleter
	def BlckdSts(self):
		del self._BlckdSts
		self._BlckdSts = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if type(value) != base_types.auto else self.make_default("Coll")

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = None

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if type(value) != base_types.auto else self.make_default("Dsgnt")

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = None

	@property
	def FndFmlyNm(self):
		return self._FndFmlyNm

	@FndFmlyNm.setter
	def FndFmlyNm(self, value):
		self._FndFmlyNm = value if type(value) != base_types.auto else self.make_default("FndFmlyNm")

	@FndFmlyNm.deleter
	def FndFmlyNm(self):
		del self._FndFmlyNm
		self._FndFmlyNm = None

	@property
	def FrgnStsCertfctn(self):
		return self._FrgnStsCertfctn

	@FrgnStsCertfctn.setter
	def FrgnStsCertfctn(self, value):
		self._FrgnStsCertfctn = value if type(value) != base_types.auto else self.make_default("FrgnStsCertfctn")

	@FrgnStsCertfctn.deleter
	def FrgnStsCertfctn(self):
		del self._FrgnStsCertfctn
		self._FrgnStsCertfctn = None

	@property
	def FsclYr(self):
		return self._FsclYr

	@FsclYr.setter
	def FsclYr(self, value):
		self._FsclYr = value if type(value) != base_types.auto else self.make_default("FsclYr")

	@FsclYr.deleter
	def FsclYr(self):
		del self._FsclYr
		self._FsclYr = None

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if type(value) != base_types.auto else self.make_default("IncmPref")

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = None

	@property
	def InvstmtAcctCtgy(self):
		return self._InvstmtAcctCtgy

	@InvstmtAcctCtgy.setter
	def InvstmtAcctCtgy(self, value):
		self._InvstmtAcctCtgy = value if type(value) != base_types.auto else self.make_default("InvstmtAcctCtgy")

	@InvstmtAcctCtgy.deleter
	def InvstmtAcctCtgy(self):
		del self._InvstmtAcctCtgy
		self._InvstmtAcctCtgy = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def Lblty(self):
		return self._Lblty

	@Lblty.setter
	def Lblty(self, value):
		self._Lblty = value if type(value) != base_types.auto else self.make_default("Lblty")

	@Lblty.deleter
	def Lblty(self):
		del self._Lblty
		self._Lblty = None

	@property
	def LttrInttDtls(self):
		return self._LttrInttDtls

	@LttrInttDtls.setter
	def LttrInttDtls(self, value):
		self._LttrInttDtls = value if type(value) != base_types.auto else self.make_default("LttrInttDtls")

	@LttrInttDtls.deleter
	def LttrInttDtls(self):
		del self._LttrInttDtls
		self._LttrInttDtls = None

	@property
	def ModfdFinInstrmDtls(self):
		return self._ModfdFinInstrmDtls

	@ModfdFinInstrmDtls.setter
	def ModfdFinInstrmDtls(self, value):
		self._ModfdFinInstrmDtls = value if type(value) != base_types.auto else self.make_default("ModfdFinInstrmDtls")

	@ModfdFinInstrmDtls.deleter
	def ModfdFinInstrmDtls(self):
		del self._ModfdFinInstrmDtls
		self._ModfdFinInstrmDtls = None

	@property
	def ModfdInvstrPrfl(self):
		return self._ModfdInvstrPrfl

	@ModfdInvstrPrfl.setter
	def ModfdInvstrPrfl(self, value):
		self._ModfdInvstrPrfl = value if type(value) != base_types.auto else self.make_default("ModfdInvstrPrfl")

	@ModfdInvstrPrfl.deleter
	def ModfdInvstrPrfl(self):
		del self._ModfdInvstrPrfl
		self._ModfdInvstrPrfl = None

	@property
	def NegInd(self):
		return self._NegInd

	@NegInd.setter
	def NegInd(self, value):
		self._NegInd = value if type(value) != base_types.auto else self.make_default("NegInd")

	@NegInd.deleter
	def NegInd(self):
		del self._NegInd
		self._NegInd = None

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
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if type(value) != base_types.auto else self.make_default("OpngDt")

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = None

	@property
	def OwnrshTp(self):
		return self._OwnrshTp

	@OwnrshTp.setter
	def OwnrshTp(self, value):
		self._OwnrshTp = value if type(value) != base_types.auto else self.make_default("OwnrshTp")

	@OwnrshTp.deleter
	def OwnrshTp(self):
		del self._OwnrshTp
		self._OwnrshTp = None

	@property
	def Pldgg(self):
		return self._Pldgg

	@Pldgg.setter
	def Pldgg(self, value):
		self._Pldgg = value if type(value) != base_types.auto else self.make_default("Pldgg")

	@Pldgg.deleter
	def Pldgg(self):
		del self._Pldgg
		self._Pldgg = None

	@property
	def PrcgOrdr(self):
		return self._PrcgOrdr

	@PrcgOrdr.setter
	def PrcgOrdr(self, value):
		self._PrcgOrdr = value if type(value) != base_types.auto else self.make_default("PrcgOrdr")

	@PrcgOrdr.deleter
	def PrcgOrdr(self):
		del self._PrcgOrdr
		self._PrcgOrdr = None

	@property
	def PwrOfAttnyLvlOfCtrl(self):
		return self._PwrOfAttnyLvlOfCtrl

	@PwrOfAttnyLvlOfCtrl.setter
	def PwrOfAttnyLvlOfCtrl(self, value):
		self._PwrOfAttnyLvlOfCtrl = value if type(value) != base_types.auto else self.make_default("PwrOfAttnyLvlOfCtrl")

	@PwrOfAttnyLvlOfCtrl.deleter
	def PwrOfAttnyLvlOfCtrl(self):
		del self._PwrOfAttnyLvlOfCtrl
		self._PwrOfAttnyLvlOfCtrl = None

	@property
	def RefCcy(self):
		return self._RefCcy

	@RefCcy.setter
	def RefCcy(self, value):
		self._RefCcy = value if type(value) != base_types.auto else self.make_default("RefCcy")

	@RefCcy.deleter
	def RefCcy(self):
		del self._RefCcy
		self._RefCcy = None

	@property
	def ReqrdSgntriesNb(self):
		return self._ReqrdSgntriesNb

	@ReqrdSgntriesNb.setter
	def ReqrdSgntriesNb(self, value):
		self._ReqrdSgntriesNb = value if type(value) != base_types.auto else self.make_default("ReqrdSgntriesNb")

	@ReqrdSgntriesNb.deleter
	def ReqrdSgntriesNb(self):
		del self._ReqrdSgntriesNb
		self._ReqrdSgntriesNb = None

	@property
	def RinvstmtDtls(self):
		return self._RinvstmtDtls

	@RinvstmtDtls.setter
	def RinvstmtDtls(self, value):
		self._RinvstmtDtls = value if type(value) != base_types.auto else self.make_default("RinvstmtDtls")

	@RinvstmtDtls.deleter
	def RinvstmtDtls(self):
		del self._RinvstmtDtls
		self._RinvstmtDtls = None

	@property
	def RndgDtls(self):
		return self._RndgDtls

	@RndgDtls.setter
	def RndgDtls(self, value):
		self._RndgDtls = value if type(value) != base_types.auto else self.make_default("RndgDtls")

	@RndgDtls.deleter
	def RndgDtls(self):
		del self._RndgDtls
		self._RndgDtls = None

	@property
	def StmtFrqcy(self):
		return self._StmtFrqcy

	@StmtFrqcy.setter
	def StmtFrqcy(self, value):
		self._StmtFrqcy = value if type(value) != base_types.auto else self.make_default("StmtFrqcy")

	@StmtFrqcy.deleter
	def StmtFrqcy(self):
		del self._StmtFrqcy
		self._StmtFrqcy = None

	@property
	def TaxRptg(self):
		return self._TaxRptg

	@TaxRptg.setter
	def TaxRptg(self, value):
		self._TaxRptg = value if type(value) != base_types.auto else self.make_default("TaxRptg")

	@TaxRptg.deleter
	def TaxRptg(self):
		del self._TaxRptg
		self._TaxRptg = None

	@property
	def TaxWhldgMtd(self):
		return self._TaxWhldgMtd

	@TaxWhldgMtd.setter
	def TaxWhldgMtd(self, value):
		self._TaxWhldgMtd = value if type(value) != base_types.auto else self.make_default("TaxWhldgMtd")

	@TaxWhldgMtd.deleter
	def TaxWhldgMtd(self):
		del self._TaxWhldgMtd
		self._TaxWhldgMtd = None

	@property
	def TaxXmptn(self):
		return self._TaxXmptn

	@TaxXmptn.setter
	def TaxXmptn(self, value):
		self._TaxXmptn = value if type(value) != base_types.auto else self.make_default("TaxXmptn")

	@TaxXmptn.deleter
	def TaxXmptn(self):
		del self._TaxXmptn
		self._TaxXmptn = None

	@property
	def ThrdPtyRghts(self):
		return self._ThrdPtyRghts

	@ThrdPtyRghts.setter
	def ThrdPtyRghts(self, value):
		self._ThrdPtyRghts = value if type(value) != base_types.auto else self.make_default("ThrdPtyRghts")

	@ThrdPtyRghts.deleter
	def ThrdPtyRghts(self):
		del self._ThrdPtyRghts
		self._ThrdPtyRghts = None

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
	def TxChanlTp(self):
		return self._TxChanlTp

	@TxChanlTp.setter
	def TxChanlTp(self, value):
		self._TxChanlTp = value if type(value) != base_types.auto else self.make_default("TxChanlTp")

	@TxChanlTp.deleter
	def TxChanlTp(self):
		del self._TxChanlTp
		self._TxChanlTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSgntrDtTm', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctStsUpdInstr', type=AccountStatusUpdateInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctUsgTp', type=AccountUsageType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctgSts', type=AccountingStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcmltnRghtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdSts', type=BlockedStatusReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=Collateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndFmlyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrgnStsCertfctn', type=Provided1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclYr', type=FiscalYear1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctCtgy', type=InvestmentAccountCategory1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lblty', type=Liability1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrInttDtls', type=LetterIntent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdFinInstrmDtls', type=ModificationScope42, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdInvstrPrfl', type=ModificationScope46, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NegInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrshTp', type=OwnershipType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pldgg', type=Eligible1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgOrdr', type=PositionEffect3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PwrOfAttnyLvlOfCtrl', type=LevelOfControl1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdSgntriesNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RinvstmtDtls', type=Reinvestment4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RndgDtls', type=RoundingParameters1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtFrqcy', type=StatementFrequencyReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRptg', type=TaxReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxWhldgMtd', type=TaxWithholdingMethod3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxXmptn', type=TaxExemptionReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyRghts', type=ThirdPartyRights2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AccountType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
	))

