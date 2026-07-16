# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import DateAndAmount2
from . import DecimalNumber
from . import DrawdownStatus1Choice
from . import DrawdownType2Choice
from . import LumpSumType1Choice
from . import Max35Text
from . import MoneyPurchaseAnnualAllowance1
from . import Number
from . import PensionOrder1
from . import PensionPolicy1
from . import PensionSchemeType3Choice
from . import PensionTransferScope1Choice
from . import TaxReference1
from . import YesNoIndicator

class Pension5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_BlckTrf", "_BlckTrfRef", "_BnftCrstllstnEvtOcrd", "_ClntLftmAllwncPrtcn", "_DrwdwnSts", "_DrwdwnTp", "_DrwdwnTrchId", "_EstmtdVal", "_Id", "_LftmAllwncPrtcn", "_LumpSumTp", "_MnyPurchsAnlAllwnc", "_NbOfDrwdwnTrnchs", "_NonSfgrddGrntedBnfts", "_NonWrpprTrf", "_PnsnOrdr", "_RingFncdDrwdwnAssts", "_RtrmntAge", "_RtrmntAgePrtcn", "_SfgrdBnft", "_Shrg", "_TaxFreeCshAmt", "_TaxFreeCshPrtcn", "_TaxRef", "_Tp", "_TrfScp", "_ValOfPnsnPlcyOrPlanOrSchme"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def BlckTrf(self):
		return self._BlckTrf

	@BlckTrf.setter
	def BlckTrf(self, value):
		self._BlckTrf = value if value is not None else base_types.UninitialisedField(self, 'BlckTrf', YesNoIndicator, False)

	@BlckTrf.deleter
	def BlckTrf(self):
		del self._BlckTrf
		self._BlckTrf = base_types.UninitialisedField(self, 'BlckTrf', YesNoIndicator, False)

	@property
	def BlckTrfRef(self):
		return self._BlckTrfRef

	@BlckTrfRef.setter
	def BlckTrfRef(self, value):
		self._BlckTrfRef = value if value is not None else base_types.UninitialisedField(self, 'BlckTrfRef', Max35Text, False)

	@BlckTrfRef.deleter
	def BlckTrfRef(self):
		del self._BlckTrfRef
		self._BlckTrfRef = base_types.UninitialisedField(self, 'BlckTrfRef', Max35Text, False)

	@property
	def BnftCrstllstnEvtOcrd(self):
		return self._BnftCrstllstnEvtOcrd

	@BnftCrstllstnEvtOcrd.setter
	def BnftCrstllstnEvtOcrd(self, value):
		self._BnftCrstllstnEvtOcrd = value if value is not None else base_types.UninitialisedField(self, 'BnftCrstllstnEvtOcrd', YesNoIndicator, False)

	@BnftCrstllstnEvtOcrd.deleter
	def BnftCrstllstnEvtOcrd(self):
		del self._BnftCrstllstnEvtOcrd
		self._BnftCrstllstnEvtOcrd = base_types.UninitialisedField(self, 'BnftCrstllstnEvtOcrd', YesNoIndicator, False)

	@property
	def ClntLftmAllwncPrtcn(self):
		return self._ClntLftmAllwncPrtcn

	@ClntLftmAllwncPrtcn.setter
	def ClntLftmAllwncPrtcn(self, value):
		self._ClntLftmAllwncPrtcn = value if value is not None else base_types.UninitialisedField(self, 'ClntLftmAllwncPrtcn', YesNoIndicator, False)

	@ClntLftmAllwncPrtcn.deleter
	def ClntLftmAllwncPrtcn(self):
		del self._ClntLftmAllwncPrtcn
		self._ClntLftmAllwncPrtcn = base_types.UninitialisedField(self, 'ClntLftmAllwncPrtcn', YesNoIndicator, False)

	@property
	def DrwdwnSts(self):
		return self._DrwdwnSts

	@DrwdwnSts.setter
	def DrwdwnSts(self, value):
		self._DrwdwnSts = value if value is not None else base_types.UninitialisedField(self, 'DrwdwnSts', DrawdownStatus1Choice, False)

	@DrwdwnSts.deleter
	def DrwdwnSts(self):
		del self._DrwdwnSts
		self._DrwdwnSts = base_types.UninitialisedField(self, 'DrwdwnSts', DrawdownStatus1Choice, False)

	@property
	def DrwdwnTp(self):
		return self._DrwdwnTp

	@DrwdwnTp.setter
	def DrwdwnTp(self, value):
		self._DrwdwnTp = value if value is not None else base_types.UninitialisedField(self, 'DrwdwnTp', DrawdownType2Choice, False)

	@DrwdwnTp.deleter
	def DrwdwnTp(self):
		del self._DrwdwnTp
		self._DrwdwnTp = base_types.UninitialisedField(self, 'DrwdwnTp', DrawdownType2Choice, False)

	@property
	def DrwdwnTrchId(self):
		return self._DrwdwnTrchId

	@DrwdwnTrchId.setter
	def DrwdwnTrchId(self, value):
		self._DrwdwnTrchId = value if value is not None else base_types.UninitialisedField(self, 'DrwdwnTrchId', Max35Text, False)

	@DrwdwnTrchId.deleter
	def DrwdwnTrchId(self):
		del self._DrwdwnTrchId
		self._DrwdwnTrchId = base_types.UninitialisedField(self, 'DrwdwnTrchId', Max35Text, False)

	@property
	def EstmtdVal(self):
		return self._EstmtdVal

	@EstmtdVal.setter
	def EstmtdVal(self, value):
		self._EstmtdVal = value if value is not None else base_types.UninitialisedField(self, 'EstmtdVal', DateAndAmount2, False)

	@EstmtdVal.deleter
	def EstmtdVal(self):
		del self._EstmtdVal
		self._EstmtdVal = base_types.UninitialisedField(self, 'EstmtdVal', DateAndAmount2, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PensionPolicy1, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PensionPolicy1, False)

	@property
	def LftmAllwncPrtcn(self):
		return self._LftmAllwncPrtcn

	@LftmAllwncPrtcn.setter
	def LftmAllwncPrtcn(self, value):
		self._LftmAllwncPrtcn = value if value is not None else base_types.UninitialisedField(self, 'LftmAllwncPrtcn', YesNoIndicator, False)

	@LftmAllwncPrtcn.deleter
	def LftmAllwncPrtcn(self):
		del self._LftmAllwncPrtcn
		self._LftmAllwncPrtcn = base_types.UninitialisedField(self, 'LftmAllwncPrtcn', YesNoIndicator, False)

	@property
	def LumpSumTp(self):
		return self._LumpSumTp

	@LumpSumTp.setter
	def LumpSumTp(self, value):
		self._LumpSumTp = value if value is not None else base_types.UninitialisedField(self, 'LumpSumTp', LumpSumType1Choice, True)

	@LumpSumTp.deleter
	def LumpSumTp(self):
		del self._LumpSumTp
		self._LumpSumTp = base_types.UninitialisedField(self, 'LumpSumTp', LumpSumType1Choice, True)

	@property
	def MnyPurchsAnlAllwnc(self):
		return self._MnyPurchsAnlAllwnc

	@MnyPurchsAnlAllwnc.setter
	def MnyPurchsAnlAllwnc(self, value):
		self._MnyPurchsAnlAllwnc = value if value is not None else base_types.UninitialisedField(self, 'MnyPurchsAnlAllwnc', MoneyPurchaseAnnualAllowance1, False)

	@MnyPurchsAnlAllwnc.deleter
	def MnyPurchsAnlAllwnc(self):
		del self._MnyPurchsAnlAllwnc
		self._MnyPurchsAnlAllwnc = base_types.UninitialisedField(self, 'MnyPurchsAnlAllwnc', MoneyPurchaseAnnualAllowance1, False)

	@property
	def NbOfDrwdwnTrnchs(self):
		return self._NbOfDrwdwnTrnchs

	@NbOfDrwdwnTrnchs.setter
	def NbOfDrwdwnTrnchs(self, value):
		self._NbOfDrwdwnTrnchs = value if value is not None else base_types.UninitialisedField(self, 'NbOfDrwdwnTrnchs', Number, False)

	@NbOfDrwdwnTrnchs.deleter
	def NbOfDrwdwnTrnchs(self):
		del self._NbOfDrwdwnTrnchs
		self._NbOfDrwdwnTrnchs = base_types.UninitialisedField(self, 'NbOfDrwdwnTrnchs', Number, False)

	@property
	def NonSfgrddGrntedBnfts(self):
		return self._NonSfgrddGrntedBnfts

	@NonSfgrddGrntedBnfts.setter
	def NonSfgrddGrntedBnfts(self, value):
		self._NonSfgrddGrntedBnfts = value if value is not None else base_types.UninitialisedField(self, 'NonSfgrddGrntedBnfts', YesNoIndicator, False)

	@NonSfgrddGrntedBnfts.deleter
	def NonSfgrddGrntedBnfts(self):
		del self._NonSfgrddGrntedBnfts
		self._NonSfgrddGrntedBnfts = base_types.UninitialisedField(self, 'NonSfgrddGrntedBnfts', YesNoIndicator, False)

	@property
	def NonWrpprTrf(self):
		return self._NonWrpprTrf

	@NonWrpprTrf.setter
	def NonWrpprTrf(self, value):
		self._NonWrpprTrf = value if value is not None else base_types.UninitialisedField(self, 'NonWrpprTrf', YesNoIndicator, False)

	@NonWrpprTrf.deleter
	def NonWrpprTrf(self):
		del self._NonWrpprTrf
		self._NonWrpprTrf = base_types.UninitialisedField(self, 'NonWrpprTrf', YesNoIndicator, False)

	@property
	def PnsnOrdr(self):
		return self._PnsnOrdr

	@PnsnOrdr.setter
	def PnsnOrdr(self, value):
		self._PnsnOrdr = value if value is not None else base_types.UninitialisedField(self, 'PnsnOrdr', PensionOrder1, True)

	@PnsnOrdr.deleter
	def PnsnOrdr(self):
		del self._PnsnOrdr
		self._PnsnOrdr = base_types.UninitialisedField(self, 'PnsnOrdr', PensionOrder1, True)

	@property
	def RingFncdDrwdwnAssts(self):
		return self._RingFncdDrwdwnAssts

	@RingFncdDrwdwnAssts.setter
	def RingFncdDrwdwnAssts(self, value):
		self._RingFncdDrwdwnAssts = value if value is not None else base_types.UninitialisedField(self, 'RingFncdDrwdwnAssts', YesNoIndicator, False)

	@RingFncdDrwdwnAssts.deleter
	def RingFncdDrwdwnAssts(self):
		del self._RingFncdDrwdwnAssts
		self._RingFncdDrwdwnAssts = base_types.UninitialisedField(self, 'RingFncdDrwdwnAssts', YesNoIndicator, False)

	@property
	def RtrmntAge(self):
		return self._RtrmntAge

	@RtrmntAge.setter
	def RtrmntAge(self, value):
		self._RtrmntAge = value if value is not None else base_types.UninitialisedField(self, 'RtrmntAge', DecimalNumber, False)

	@RtrmntAge.deleter
	def RtrmntAge(self):
		del self._RtrmntAge
		self._RtrmntAge = base_types.UninitialisedField(self, 'RtrmntAge', DecimalNumber, False)

	@property
	def RtrmntAgePrtcn(self):
		return self._RtrmntAgePrtcn

	@RtrmntAgePrtcn.setter
	def RtrmntAgePrtcn(self, value):
		self._RtrmntAgePrtcn = value if value is not None else base_types.UninitialisedField(self, 'RtrmntAgePrtcn', YesNoIndicator, False)

	@RtrmntAgePrtcn.deleter
	def RtrmntAgePrtcn(self):
		del self._RtrmntAgePrtcn
		self._RtrmntAgePrtcn = base_types.UninitialisedField(self, 'RtrmntAgePrtcn', YesNoIndicator, False)

	@property
	def SfgrdBnft(self):
		return self._SfgrdBnft

	@SfgrdBnft.setter
	def SfgrdBnft(self, value):
		self._SfgrdBnft = value if value is not None else base_types.UninitialisedField(self, 'SfgrdBnft', YesNoIndicator, False)

	@SfgrdBnft.deleter
	def SfgrdBnft(self):
		del self._SfgrdBnft
		self._SfgrdBnft = base_types.UninitialisedField(self, 'SfgrdBnft', YesNoIndicator, False)

	@property
	def Shrg(self):
		return self._Shrg

	@Shrg.setter
	def Shrg(self, value):
		self._Shrg = value if value is not None else base_types.UninitialisedField(self, 'Shrg', YesNoIndicator, False)

	@Shrg.deleter
	def Shrg(self):
		del self._Shrg
		self._Shrg = base_types.UninitialisedField(self, 'Shrg', YesNoIndicator, False)

	@property
	def TaxFreeCshAmt(self):
		return self._TaxFreeCshAmt

	@TaxFreeCshAmt.setter
	def TaxFreeCshAmt(self, value):
		self._TaxFreeCshAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxFreeCshAmt', DateAndAmount2, False)

	@TaxFreeCshAmt.deleter
	def TaxFreeCshAmt(self):
		del self._TaxFreeCshAmt
		self._TaxFreeCshAmt = base_types.UninitialisedField(self, 'TaxFreeCshAmt', DateAndAmount2, False)

	@property
	def TaxFreeCshPrtcn(self):
		return self._TaxFreeCshPrtcn

	@TaxFreeCshPrtcn.setter
	def TaxFreeCshPrtcn(self, value):
		self._TaxFreeCshPrtcn = value if value is not None else base_types.UninitialisedField(self, 'TaxFreeCshPrtcn', YesNoIndicator, False)

	@TaxFreeCshPrtcn.deleter
	def TaxFreeCshPrtcn(self):
		del self._TaxFreeCshPrtcn
		self._TaxFreeCshPrtcn = base_types.UninitialisedField(self, 'TaxFreeCshPrtcn', YesNoIndicator, False)

	@property
	def TaxRef(self):
		return self._TaxRef

	@TaxRef.setter
	def TaxRef(self, value):
		self._TaxRef = value if value is not None else base_types.UninitialisedField(self, 'TaxRef', TaxReference1, True)

	@TaxRef.deleter
	def TaxRef(self):
		del self._TaxRef
		self._TaxRef = base_types.UninitialisedField(self, 'TaxRef', TaxReference1, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PensionSchemeType3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PensionSchemeType3Choice, False)

	@property
	def TrfScp(self):
		return self._TrfScp

	@TrfScp.setter
	def TrfScp(self, value):
		self._TrfScp = value if value is not None else base_types.UninitialisedField(self, 'TrfScp', PensionTransferScope1Choice, False)

	@TrfScp.deleter
	def TrfScp(self):
		del self._TrfScp
		self._TrfScp = base_types.UninitialisedField(self, 'TrfScp', PensionTransferScope1Choice, False)

	@property
	def ValOfPnsnPlcyOrPlanOrSchme(self):
		return self._ValOfPnsnPlcyOrPlanOrSchme

	@ValOfPnsnPlcyOrPlanOrSchme.setter
	def ValOfPnsnPlcyOrPlanOrSchme(self, value):
		self._ValOfPnsnPlcyOrPlanOrSchme = value if value is not None else base_types.UninitialisedField(self, 'ValOfPnsnPlcyOrPlanOrSchme', DateAndAmount2, False)

	@ValOfPnsnPlcyOrPlanOrSchme.deleter
	def ValOfPnsnPlcyOrPlanOrSchme(self):
		del self._ValOfPnsnPlcyOrPlanOrSchme
		self._ValOfPnsnPlcyOrPlanOrSchme = base_types.UninitialisedField(self, 'ValOfPnsnPlcyOrPlanOrSchme', DateAndAmount2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BlckTrf', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckTrfRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnftCrstllstnEvtOcrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntLftmAllwncPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnSts', type=DrawdownStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnTp', type=DrawdownType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnTrchId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PensionPolicy1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LftmAllwncPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LumpSumTp', type=LumpSumType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MnyPurchsAnlAllwnc', type=MoneyPurchaseAnnualAllowance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDrwdwnTrnchs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonSfgrddGrntedBnfts', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonWrpprTrf', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnsnOrdr', type=PensionOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RingFncdDrwdwnAssts', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrmntAge', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrmntAgePrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfgrdBnft', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Shrg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxFreeCshAmt', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxFreeCshPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRef', type=TaxReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=PensionSchemeType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfScp', type=PensionTransferScope1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValOfPnsnPlcyOrPlanOrSchme', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
	))