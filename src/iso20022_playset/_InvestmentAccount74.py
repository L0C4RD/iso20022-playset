# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountStatus2
from . import AccountType2Choice
from . import AccountUsageType2Choice
from . import AccountingStatus1Choice
from . import ActiveCurrencyCode
from . import BlockedStatusReason2Choice
from . import Collateral1Code
from . import DateAndDateTime1Choice
from . import Eligible1Code
from . import FinancialInstrument87
from . import FiscalYear1Choice
from . import IncomePreference2Code
from . import InvestmentAccountCategory1Choice
from . import InvestorProfile2
from . import LanguageCode
from . import LetterIntent1
from . import LevelOfControl1Choice
from . import Liability1Choice
from . import Max350Text
from . import Max35Text
from . import Number
from . import OwnershipType2Choice
from . import PartyIdentification125Choice
from . import PositionEffect3Code
from . import Provided1Code
from . import Reinvestment4
from . import RoundingParameters1
from . import StatementFrequencyReason2Choice
from . import TaxExemptionReason2Choice
from . import TaxReporting3
from . import TaxWithholdingMethod3Code
from . import ThirdPartyRights2
from . import TransactionChannelType1Choice
from . import YesNoIndicator

class InvestmentAccount74(base_types._BaseFieldType):

	__slots__ = ["_AcctSgntrDtTm", "_AcctSts", "_AcctSvcr", "_AcctUsgTp", "_AcctgSts", "_AcmltnRghtRef", "_BlckdSts", "_ClsgDt", "_Coll", "_Dsgnt", "_FinInstrmDtls", "_FndFmlyNm", "_FrgnStsCertfctn", "_FsclYr", "_Id", "_IncmPref", "_InvstmtAcctCtgy", "_InvstrPrfl", "_Lang", "_Lblty", "_LttrInttDtls", "_NegInd", "_Nm", "_OpngDt", "_OwnrshTp", "_Pldgg", "_PrcgOrdr", "_PwrOfAttnyLvlOfCtrl", "_RefCcy", "_ReqrdSgntriesNb", "_RinvstmtDtls", "_RndgDtls", "_StmtFrqcy", "_StsDt", "_TaxRptg", "_TaxWhldgMtd", "_TaxXmptn", "_ThrdPtyRghts", "_Tp", "_TxChanlTp"]
	@property
	def AcctSgntrDtTm(self):
		return self._AcctSgntrDtTm

	@AcctSgntrDtTm.setter
	def AcctSgntrDtTm(self, value):
		self._AcctSgntrDtTm = value if value is not None else base_types.UninitialisedField(self, 'AcctSgntrDtTm', DateAndDateTime1Choice, False)

	@AcctSgntrDtTm.deleter
	def AcctSgntrDtTm(self):
		del self._AcctSgntrDtTm
		self._AcctSgntrDtTm = base_types.UninitialisedField(self, 'AcctSgntrDtTm', DateAndDateTime1Choice, False)

	@property
	def AcctSts(self):
		return self._AcctSts

	@AcctSts.setter
	def AcctSts(self, value):
		self._AcctSts = value if value is not None else base_types.UninitialisedField(self, 'AcctSts', AccountStatus2, False)

	@AcctSts.deleter
	def AcctSts(self):
		del self._AcctSts
		self._AcctSts = base_types.UninitialisedField(self, 'AcctSts', AccountStatus2, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification125Choice, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification125Choice, False)

	@property
	def AcctUsgTp(self):
		return self._AcctUsgTp

	@AcctUsgTp.setter
	def AcctUsgTp(self, value):
		self._AcctUsgTp = value if value is not None else base_types.UninitialisedField(self, 'AcctUsgTp', AccountUsageType2Choice, False)

	@AcctUsgTp.deleter
	def AcctUsgTp(self):
		del self._AcctUsgTp
		self._AcctUsgTp = base_types.UninitialisedField(self, 'AcctUsgTp', AccountUsageType2Choice, False)

	@property
	def AcctgSts(self):
		return self._AcctgSts

	@AcctgSts.setter
	def AcctgSts(self, value):
		self._AcctgSts = value if value is not None else base_types.UninitialisedField(self, 'AcctgSts', AccountingStatus1Choice, False)

	@AcctgSts.deleter
	def AcctgSts(self):
		del self._AcctgSts
		self._AcctgSts = base_types.UninitialisedField(self, 'AcctgSts', AccountingStatus1Choice, False)

	@property
	def AcmltnRghtRef(self):
		return self._AcmltnRghtRef

	@AcmltnRghtRef.setter
	def AcmltnRghtRef(self, value):
		self._AcmltnRghtRef = value if value is not None else base_types.UninitialisedField(self, 'AcmltnRghtRef', Max35Text, False)

	@AcmltnRghtRef.deleter
	def AcmltnRghtRef(self):
		del self._AcmltnRghtRef
		self._AcmltnRghtRef = base_types.UninitialisedField(self, 'AcmltnRghtRef', Max35Text, False)

	@property
	def BlckdSts(self):
		return self._BlckdSts

	@BlckdSts.setter
	def BlckdSts(self, value):
		self._BlckdSts = value if value is not None else base_types.UninitialisedField(self, 'BlckdSts', BlockedStatusReason2Choice, False)

	@BlckdSts.deleter
	def BlckdSts(self):
		del self._BlckdSts
		self._BlckdSts = base_types.UninitialisedField(self, 'BlckdSts', BlockedStatusReason2Choice, False)

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', DateAndDateTime1Choice, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', DateAndDateTime1Choice, False)

	@property
	def Coll(self):
		return self._Coll

	@Coll.setter
	def Coll(self, value):
		self._Coll = value if value is not None else base_types.UninitialisedField(self, 'Coll', Collateral1Code, False)

	@Coll.deleter
	def Coll(self):
		del self._Coll
		self._Coll = base_types.UninitialisedField(self, 'Coll', Collateral1Code, False)

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if value is not None else base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument87, True)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument87, True)

	@property
	def FndFmlyNm(self):
		return self._FndFmlyNm

	@FndFmlyNm.setter
	def FndFmlyNm(self, value):
		self._FndFmlyNm = value if value is not None else base_types.UninitialisedField(self, 'FndFmlyNm', Max350Text, False)

	@FndFmlyNm.deleter
	def FndFmlyNm(self):
		del self._FndFmlyNm
		self._FndFmlyNm = base_types.UninitialisedField(self, 'FndFmlyNm', Max350Text, False)

	@property
	def FrgnStsCertfctn(self):
		return self._FrgnStsCertfctn

	@FrgnStsCertfctn.setter
	def FrgnStsCertfctn(self, value):
		self._FrgnStsCertfctn = value if value is not None else base_types.UninitialisedField(self, 'FrgnStsCertfctn', Provided1Code, False)

	@FrgnStsCertfctn.deleter
	def FrgnStsCertfctn(self):
		del self._FrgnStsCertfctn
		self._FrgnStsCertfctn = base_types.UninitialisedField(self, 'FrgnStsCertfctn', Provided1Code, False)

	@property
	def FsclYr(self):
		return self._FsclYr

	@FsclYr.setter
	def FsclYr(self, value):
		self._FsclYr = value if value is not None else base_types.UninitialisedField(self, 'FsclYr', FiscalYear1Choice, False)

	@FsclYr.deleter
	def FsclYr(self):
		del self._FsclYr
		self._FsclYr = base_types.UninitialisedField(self, 'FsclYr', FiscalYear1Choice, False)

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
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if value is not None else base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = base_types.UninitialisedField(self, 'IncmPref', IncomePreference2Code, False)

	@property
	def InvstmtAcctCtgy(self):
		return self._InvstmtAcctCtgy

	@InvstmtAcctCtgy.setter
	def InvstmtAcctCtgy(self, value):
		self._InvstmtAcctCtgy = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctCtgy', InvestmentAccountCategory1Choice, False)

	@InvstmtAcctCtgy.deleter
	def InvstmtAcctCtgy(self):
		del self._InvstmtAcctCtgy
		self._InvstmtAcctCtgy = base_types.UninitialisedField(self, 'InvstmtAcctCtgy', InvestmentAccountCategory1Choice, False)

	@property
	def InvstrPrfl(self):
		return self._InvstrPrfl

	@InvstrPrfl.setter
	def InvstrPrfl(self, value):
		self._InvstrPrfl = value if value is not None else base_types.UninitialisedField(self, 'InvstrPrfl', InvestorProfile2, True)

	@InvstrPrfl.deleter
	def InvstrPrfl(self):
		del self._InvstrPrfl
		self._InvstrPrfl = base_types.UninitialisedField(self, 'InvstrPrfl', InvestorProfile2, True)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@property
	def Lblty(self):
		return self._Lblty

	@Lblty.setter
	def Lblty(self, value):
		self._Lblty = value if value is not None else base_types.UninitialisedField(self, 'Lblty', Liability1Choice, False)

	@Lblty.deleter
	def Lblty(self):
		del self._Lblty
		self._Lblty = base_types.UninitialisedField(self, 'Lblty', Liability1Choice, False)

	@property
	def LttrInttDtls(self):
		return self._LttrInttDtls

	@LttrInttDtls.setter
	def LttrInttDtls(self, value):
		self._LttrInttDtls = value if value is not None else base_types.UninitialisedField(self, 'LttrInttDtls', LetterIntent1, False)

	@LttrInttDtls.deleter
	def LttrInttDtls(self):
		del self._LttrInttDtls
		self._LttrInttDtls = base_types.UninitialisedField(self, 'LttrInttDtls', LetterIntent1, False)

	@property
	def NegInd(self):
		return self._NegInd

	@NegInd.setter
	def NegInd(self, value):
		self._NegInd = value if value is not None else base_types.UninitialisedField(self, 'NegInd', YesNoIndicator, False)

	@NegInd.deleter
	def NegInd(self):
		del self._NegInd
		self._NegInd = base_types.UninitialisedField(self, 'NegInd', YesNoIndicator, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if value is not None else base_types.UninitialisedField(self, 'OpngDt', DateAndDateTime1Choice, False)

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = base_types.UninitialisedField(self, 'OpngDt', DateAndDateTime1Choice, False)

	@property
	def OwnrshTp(self):
		return self._OwnrshTp

	@OwnrshTp.setter
	def OwnrshTp(self, value):
		self._OwnrshTp = value if value is not None else base_types.UninitialisedField(self, 'OwnrshTp', OwnershipType2Choice, False)

	@OwnrshTp.deleter
	def OwnrshTp(self):
		del self._OwnrshTp
		self._OwnrshTp = base_types.UninitialisedField(self, 'OwnrshTp', OwnershipType2Choice, False)

	@property
	def Pldgg(self):
		return self._Pldgg

	@Pldgg.setter
	def Pldgg(self, value):
		self._Pldgg = value if value is not None else base_types.UninitialisedField(self, 'Pldgg', Eligible1Code, False)

	@Pldgg.deleter
	def Pldgg(self):
		del self._Pldgg
		self._Pldgg = base_types.UninitialisedField(self, 'Pldgg', Eligible1Code, False)

	@property
	def PrcgOrdr(self):
		return self._PrcgOrdr

	@PrcgOrdr.setter
	def PrcgOrdr(self, value):
		self._PrcgOrdr = value if value is not None else base_types.UninitialisedField(self, 'PrcgOrdr', PositionEffect3Code, False)

	@PrcgOrdr.deleter
	def PrcgOrdr(self):
		del self._PrcgOrdr
		self._PrcgOrdr = base_types.UninitialisedField(self, 'PrcgOrdr', PositionEffect3Code, False)

	@property
	def PwrOfAttnyLvlOfCtrl(self):
		return self._PwrOfAttnyLvlOfCtrl

	@PwrOfAttnyLvlOfCtrl.setter
	def PwrOfAttnyLvlOfCtrl(self, value):
		self._PwrOfAttnyLvlOfCtrl = value if value is not None else base_types.UninitialisedField(self, 'PwrOfAttnyLvlOfCtrl', LevelOfControl1Choice, False)

	@PwrOfAttnyLvlOfCtrl.deleter
	def PwrOfAttnyLvlOfCtrl(self):
		del self._PwrOfAttnyLvlOfCtrl
		self._PwrOfAttnyLvlOfCtrl = base_types.UninitialisedField(self, 'PwrOfAttnyLvlOfCtrl', LevelOfControl1Choice, False)

	@property
	def RefCcy(self):
		return self._RefCcy

	@RefCcy.setter
	def RefCcy(self, value):
		self._RefCcy = value if value is not None else base_types.UninitialisedField(self, 'RefCcy', ActiveCurrencyCode, False)

	@RefCcy.deleter
	def RefCcy(self):
		del self._RefCcy
		self._RefCcy = base_types.UninitialisedField(self, 'RefCcy', ActiveCurrencyCode, False)

	@property
	def ReqrdSgntriesNb(self):
		return self._ReqrdSgntriesNb

	@ReqrdSgntriesNb.setter
	def ReqrdSgntriesNb(self, value):
		self._ReqrdSgntriesNb = value if value is not None else base_types.UninitialisedField(self, 'ReqrdSgntriesNb', Number, False)

	@ReqrdSgntriesNb.deleter
	def ReqrdSgntriesNb(self):
		del self._ReqrdSgntriesNb
		self._ReqrdSgntriesNb = base_types.UninitialisedField(self, 'ReqrdSgntriesNb', Number, False)

	@property
	def RinvstmtDtls(self):
		return self._RinvstmtDtls

	@RinvstmtDtls.setter
	def RinvstmtDtls(self, value):
		self._RinvstmtDtls = value if value is not None else base_types.UninitialisedField(self, 'RinvstmtDtls', Reinvestment4, True)

	@RinvstmtDtls.deleter
	def RinvstmtDtls(self):
		del self._RinvstmtDtls
		self._RinvstmtDtls = base_types.UninitialisedField(self, 'RinvstmtDtls', Reinvestment4, True)

	@property
	def RndgDtls(self):
		return self._RndgDtls

	@RndgDtls.setter
	def RndgDtls(self, value):
		self._RndgDtls = value if value is not None else base_types.UninitialisedField(self, 'RndgDtls', RoundingParameters1, False)

	@RndgDtls.deleter
	def RndgDtls(self):
		del self._RndgDtls
		self._RndgDtls = base_types.UninitialisedField(self, 'RndgDtls', RoundingParameters1, False)

	@property
	def StmtFrqcy(self):
		return self._StmtFrqcy

	@StmtFrqcy.setter
	def StmtFrqcy(self, value):
		self._StmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'StmtFrqcy', StatementFrequencyReason2Choice, False)

	@StmtFrqcy.deleter
	def StmtFrqcy(self):
		del self._StmtFrqcy
		self._StmtFrqcy = base_types.UninitialisedField(self, 'StmtFrqcy', StatementFrequencyReason2Choice, False)

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if value is not None else base_types.UninitialisedField(self, 'StsDt', DateAndDateTime1Choice, False)

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = base_types.UninitialisedField(self, 'StsDt', DateAndDateTime1Choice, False)

	@property
	def TaxRptg(self):
		return self._TaxRptg

	@TaxRptg.setter
	def TaxRptg(self, value):
		self._TaxRptg = value if value is not None else base_types.UninitialisedField(self, 'TaxRptg', TaxReporting3, True)

	@TaxRptg.deleter
	def TaxRptg(self):
		del self._TaxRptg
		self._TaxRptg = base_types.UninitialisedField(self, 'TaxRptg', TaxReporting3, True)

	@property
	def TaxWhldgMtd(self):
		return self._TaxWhldgMtd

	@TaxWhldgMtd.setter
	def TaxWhldgMtd(self, value):
		self._TaxWhldgMtd = value if value is not None else base_types.UninitialisedField(self, 'TaxWhldgMtd', TaxWithholdingMethod3Code, False)

	@TaxWhldgMtd.deleter
	def TaxWhldgMtd(self):
		del self._TaxWhldgMtd
		self._TaxWhldgMtd = base_types.UninitialisedField(self, 'TaxWhldgMtd', TaxWithholdingMethod3Code, False)

	@property
	def TaxXmptn(self):
		return self._TaxXmptn

	@TaxXmptn.setter
	def TaxXmptn(self, value):
		self._TaxXmptn = value if value is not None else base_types.UninitialisedField(self, 'TaxXmptn', TaxExemptionReason2Choice, False)

	@TaxXmptn.deleter
	def TaxXmptn(self):
		del self._TaxXmptn
		self._TaxXmptn = base_types.UninitialisedField(self, 'TaxXmptn', TaxExemptionReason2Choice, False)

	@property
	def ThrdPtyRghts(self):
		return self._ThrdPtyRghts

	@ThrdPtyRghts.setter
	def ThrdPtyRghts(self, value):
		self._ThrdPtyRghts = value if value is not None else base_types.UninitialisedField(self, 'ThrdPtyRghts', ThirdPartyRights2, False)

	@ThrdPtyRghts.deleter
	def ThrdPtyRghts(self):
		del self._ThrdPtyRghts
		self._ThrdPtyRghts = base_types.UninitialisedField(self, 'ThrdPtyRghts', ThirdPartyRights2, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', AccountType2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', AccountType2Choice, False)

	@property
	def TxChanlTp(self):
		return self._TxChanlTp

	@TxChanlTp.setter
	def TxChanlTp(self, value):
		self._TxChanlTp = value if value is not None else base_types.UninitialisedField(self, 'TxChanlTp', TransactionChannelType1Choice, False)

	@TxChanlTp.deleter
	def TxChanlTp(self):
		del self._TxChanlTp
		self._TxChanlTp = base_types.UninitialisedField(self, 'TxChanlTp', TransactionChannelType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSgntrDtTm', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSts', type=AccountStatus2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctUsgTp', type=AccountUsageType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctgSts', type=AccountingStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcmltnRghtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdSts', type=BlockedStatusReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Coll', type=Collateral1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument87, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FndFmlyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrgnStsCertfctn', type=Provided1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FsclYr', type=FiscalYear1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctCtgy', type=InvestmentAccountCategory1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrPrfl', type=InvestorProfile2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lblty', type=Liability1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrInttDtls', type=LetterIntent1, min=0, max=1, mutex_group=None, array=False),
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
		base_types.FieldEntry(name='StsDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRptg', type=TaxReporting3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxWhldgMtd', type=TaxWithholdingMethod3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxXmptn', type=TaxExemptionReason2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdPtyRghts', type=ThirdPartyRights2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AccountType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
	))