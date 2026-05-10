from . import base_types
from ._DrawdownStatus1Choice import DrawdownStatus1Choice
from ._PensionOrder1 import PensionOrder1
from ._Number import Number
from ._TaxReference1 import TaxReference1
from ._PensionSchemeType3Choice import PensionSchemeType3Choice
from ._PensionTransferScope1Choice import PensionTransferScope1Choice
from ._DrawdownType2Choice import DrawdownType2Choice
from ._PensionPolicy1 import PensionPolicy1
from ._LumpSumType1Choice import LumpSumType1Choice
from ._DateAndAmount2 import DateAndAmount2
from ._MoneyPurchaseAnnualAllowance1 import MoneyPurchaseAnnualAllowance1
from ._Max35Text import Max35Text
from ._YesNoIndicator import YesNoIndicator
from ._DecimalNumber import DecimalNumber
from ._AdditionalInformation15 import AdditionalInformation15

class Pension5(base_types._BaseFieldType):

	__slots__ = ["_TaxFreeCshAmt", "_NonSfgrddGrntedBnfts", "_ClntLftmAllwncPrtcn", "_MnyPurchsAnlAllwnc", "_RtrmntAgePrtcn", "_Tp", "_DrwdwnTrchId", "_Shrg", "_LftmAllwncPrtcn", "_TaxFreeCshPrtcn", "_PnsnOrdr", "_NbOfDrwdwnTrnchs", "_BnftCrstllstnEvtOcrd", "_DrwdwnTp", "_ValOfPnsnPlcyOrPlanOrSchme", "_SfgrdBnft", "_Id", "_RtrmntAge", "_DrwdwnSts", "_LumpSumTp", "_NonWrpprTrf", "_RingFncdDrwdwnAssts", "_BlckTrf", "_TaxRef", "_AddtlInf", "_TrfScp", "_EstmtdVal", "_BlckTrfRef"]
	@property
	def TaxFreeCshAmt(self):
		return self._TaxFreeCshAmt

	@TaxFreeCshAmt.setter
	def TaxFreeCshAmt(self, value):
		self._TaxFreeCshAmt = value if type(value) != base_types.auto else self.make_default("TaxFreeCshAmt")

	@TaxFreeCshAmt.deleter
	def TaxFreeCshAmt(self):
		del self._TaxFreeCshAmt
		self._TaxFreeCshAmt = None

	@property
	def NonSfgrddGrntedBnfts(self):
		return self._NonSfgrddGrntedBnfts

	@NonSfgrddGrntedBnfts.setter
	def NonSfgrddGrntedBnfts(self, value):
		self._NonSfgrddGrntedBnfts = value if type(value) != base_types.auto else self.make_default("NonSfgrddGrntedBnfts")

	@NonSfgrddGrntedBnfts.deleter
	def NonSfgrddGrntedBnfts(self):
		del self._NonSfgrddGrntedBnfts
		self._NonSfgrddGrntedBnfts = None

	@property
	def ClntLftmAllwncPrtcn(self):
		return self._ClntLftmAllwncPrtcn

	@ClntLftmAllwncPrtcn.setter
	def ClntLftmAllwncPrtcn(self, value):
		self._ClntLftmAllwncPrtcn = value if type(value) != base_types.auto else self.make_default("ClntLftmAllwncPrtcn")

	@ClntLftmAllwncPrtcn.deleter
	def ClntLftmAllwncPrtcn(self):
		del self._ClntLftmAllwncPrtcn
		self._ClntLftmAllwncPrtcn = None

	@property
	def MnyPurchsAnlAllwnc(self):
		return self._MnyPurchsAnlAllwnc

	@MnyPurchsAnlAllwnc.setter
	def MnyPurchsAnlAllwnc(self, value):
		self._MnyPurchsAnlAllwnc = value if type(value) != base_types.auto else self.make_default("MnyPurchsAnlAllwnc")

	@MnyPurchsAnlAllwnc.deleter
	def MnyPurchsAnlAllwnc(self):
		del self._MnyPurchsAnlAllwnc
		self._MnyPurchsAnlAllwnc = None

	@property
	def RtrmntAgePrtcn(self):
		return self._RtrmntAgePrtcn

	@RtrmntAgePrtcn.setter
	def RtrmntAgePrtcn(self, value):
		self._RtrmntAgePrtcn = value if type(value) != base_types.auto else self.make_default("RtrmntAgePrtcn")

	@RtrmntAgePrtcn.deleter
	def RtrmntAgePrtcn(self):
		del self._RtrmntAgePrtcn
		self._RtrmntAgePrtcn = None

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
	def DrwdwnTrchId(self):
		return self._DrwdwnTrchId

	@DrwdwnTrchId.setter
	def DrwdwnTrchId(self, value):
		self._DrwdwnTrchId = value if type(value) != base_types.auto else self.make_default("DrwdwnTrchId")

	@DrwdwnTrchId.deleter
	def DrwdwnTrchId(self):
		del self._DrwdwnTrchId
		self._DrwdwnTrchId = None

	@property
	def Shrg(self):
		return self._Shrg

	@Shrg.setter
	def Shrg(self, value):
		self._Shrg = value if type(value) != base_types.auto else self.make_default("Shrg")

	@Shrg.deleter
	def Shrg(self):
		del self._Shrg
		self._Shrg = None

	@property
	def LftmAllwncPrtcn(self):
		return self._LftmAllwncPrtcn

	@LftmAllwncPrtcn.setter
	def LftmAllwncPrtcn(self, value):
		self._LftmAllwncPrtcn = value if type(value) != base_types.auto else self.make_default("LftmAllwncPrtcn")

	@LftmAllwncPrtcn.deleter
	def LftmAllwncPrtcn(self):
		del self._LftmAllwncPrtcn
		self._LftmAllwncPrtcn = None

	@property
	def TaxFreeCshPrtcn(self):
		return self._TaxFreeCshPrtcn

	@TaxFreeCshPrtcn.setter
	def TaxFreeCshPrtcn(self, value):
		self._TaxFreeCshPrtcn = value if type(value) != base_types.auto else self.make_default("TaxFreeCshPrtcn")

	@TaxFreeCshPrtcn.deleter
	def TaxFreeCshPrtcn(self):
		del self._TaxFreeCshPrtcn
		self._TaxFreeCshPrtcn = None

	@property
	def PnsnOrdr(self):
		return self._PnsnOrdr

	@PnsnOrdr.setter
	def PnsnOrdr(self, value):
		self._PnsnOrdr = value if type(value) != base_types.auto else self.make_default("PnsnOrdr")

	@PnsnOrdr.deleter
	def PnsnOrdr(self):
		del self._PnsnOrdr
		self._PnsnOrdr = None

	@property
	def NbOfDrwdwnTrnchs(self):
		return self._NbOfDrwdwnTrnchs

	@NbOfDrwdwnTrnchs.setter
	def NbOfDrwdwnTrnchs(self, value):
		self._NbOfDrwdwnTrnchs = value if type(value) != base_types.auto else self.make_default("NbOfDrwdwnTrnchs")

	@NbOfDrwdwnTrnchs.deleter
	def NbOfDrwdwnTrnchs(self):
		del self._NbOfDrwdwnTrnchs
		self._NbOfDrwdwnTrnchs = None

	@property
	def BnftCrstllstnEvtOcrd(self):
		return self._BnftCrstllstnEvtOcrd

	@BnftCrstllstnEvtOcrd.setter
	def BnftCrstllstnEvtOcrd(self, value):
		self._BnftCrstllstnEvtOcrd = value if type(value) != base_types.auto else self.make_default("BnftCrstllstnEvtOcrd")

	@BnftCrstllstnEvtOcrd.deleter
	def BnftCrstllstnEvtOcrd(self):
		del self._BnftCrstllstnEvtOcrd
		self._BnftCrstllstnEvtOcrd = None

	@property
	def DrwdwnTp(self):
		return self._DrwdwnTp

	@DrwdwnTp.setter
	def DrwdwnTp(self, value):
		self._DrwdwnTp = value if type(value) != base_types.auto else self.make_default("DrwdwnTp")

	@DrwdwnTp.deleter
	def DrwdwnTp(self):
		del self._DrwdwnTp
		self._DrwdwnTp = None

	@property
	def ValOfPnsnPlcyOrPlanOrSchme(self):
		return self._ValOfPnsnPlcyOrPlanOrSchme

	@ValOfPnsnPlcyOrPlanOrSchme.setter
	def ValOfPnsnPlcyOrPlanOrSchme(self, value):
		self._ValOfPnsnPlcyOrPlanOrSchme = value if type(value) != base_types.auto else self.make_default("ValOfPnsnPlcyOrPlanOrSchme")

	@ValOfPnsnPlcyOrPlanOrSchme.deleter
	def ValOfPnsnPlcyOrPlanOrSchme(self):
		del self._ValOfPnsnPlcyOrPlanOrSchme
		self._ValOfPnsnPlcyOrPlanOrSchme = None

	@property
	def SfgrdBnft(self):
		return self._SfgrdBnft

	@SfgrdBnft.setter
	def SfgrdBnft(self, value):
		self._SfgrdBnft = value if type(value) != base_types.auto else self.make_default("SfgrdBnft")

	@SfgrdBnft.deleter
	def SfgrdBnft(self):
		del self._SfgrdBnft
		self._SfgrdBnft = None

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
	def RtrmntAge(self):
		return self._RtrmntAge

	@RtrmntAge.setter
	def RtrmntAge(self, value):
		self._RtrmntAge = value if type(value) != base_types.auto else self.make_default("RtrmntAge")

	@RtrmntAge.deleter
	def RtrmntAge(self):
		del self._RtrmntAge
		self._RtrmntAge = None

	@property
	def DrwdwnSts(self):
		return self._DrwdwnSts

	@DrwdwnSts.setter
	def DrwdwnSts(self, value):
		self._DrwdwnSts = value if type(value) != base_types.auto else self.make_default("DrwdwnSts")

	@DrwdwnSts.deleter
	def DrwdwnSts(self):
		del self._DrwdwnSts
		self._DrwdwnSts = None

	@property
	def LumpSumTp(self):
		return self._LumpSumTp

	@LumpSumTp.setter
	def LumpSumTp(self, value):
		self._LumpSumTp = value if type(value) != base_types.auto else self.make_default("LumpSumTp")

	@LumpSumTp.deleter
	def LumpSumTp(self):
		del self._LumpSumTp
		self._LumpSumTp = None

	@property
	def NonWrpprTrf(self):
		return self._NonWrpprTrf

	@NonWrpprTrf.setter
	def NonWrpprTrf(self, value):
		self._NonWrpprTrf = value if type(value) != base_types.auto else self.make_default("NonWrpprTrf")

	@NonWrpprTrf.deleter
	def NonWrpprTrf(self):
		del self._NonWrpprTrf
		self._NonWrpprTrf = None

	@property
	def RingFncdDrwdwnAssts(self):
		return self._RingFncdDrwdwnAssts

	@RingFncdDrwdwnAssts.setter
	def RingFncdDrwdwnAssts(self, value):
		self._RingFncdDrwdwnAssts = value if type(value) != base_types.auto else self.make_default("RingFncdDrwdwnAssts")

	@RingFncdDrwdwnAssts.deleter
	def RingFncdDrwdwnAssts(self):
		del self._RingFncdDrwdwnAssts
		self._RingFncdDrwdwnAssts = None

	@property
	def BlckTrf(self):
		return self._BlckTrf

	@BlckTrf.setter
	def BlckTrf(self, value):
		self._BlckTrf = value if type(value) != base_types.auto else self.make_default("BlckTrf")

	@BlckTrf.deleter
	def BlckTrf(self):
		del self._BlckTrf
		self._BlckTrf = None

	@property
	def TaxRef(self):
		return self._TaxRef

	@TaxRef.setter
	def TaxRef(self, value):
		self._TaxRef = value if type(value) != base_types.auto else self.make_default("TaxRef")

	@TaxRef.deleter
	def TaxRef(self):
		del self._TaxRef
		self._TaxRef = None

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
	def TrfScp(self):
		return self._TrfScp

	@TrfScp.setter
	def TrfScp(self, value):
		self._TrfScp = value if type(value) != base_types.auto else self.make_default("TrfScp")

	@TrfScp.deleter
	def TrfScp(self):
		del self._TrfScp
		self._TrfScp = None

	@property
	def EstmtdVal(self):
		return self._EstmtdVal

	@EstmtdVal.setter
	def EstmtdVal(self, value):
		self._EstmtdVal = value if type(value) != base_types.auto else self.make_default("EstmtdVal")

	@EstmtdVal.deleter
	def EstmtdVal(self):
		del self._EstmtdVal
		self._EstmtdVal = None

	@property
	def BlckTrfRef(self):
		return self._BlckTrfRef

	@BlckTrfRef.setter
	def BlckTrfRef(self, value):
		self._BlckTrfRef = value if type(value) != base_types.auto else self.make_default("BlckTrfRef")

	@BlckTrfRef.deleter
	def BlckTrfRef(self):
		del self._BlckTrfRef
		self._BlckTrfRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxFreeCshAmt', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonSfgrddGrntedBnfts', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntLftmAllwncPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnyPurchsAnlAllwnc', type=MoneyPurchaseAnnualAllowance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrmntAgePrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PensionSchemeType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnTrchId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Shrg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LftmAllwncPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxFreeCshPrtcn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PnsnOrdr', type=PensionOrder1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfDrwdwnTrnchs', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnftCrstllstnEvtOcrd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnTp', type=DrawdownType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValOfPnsnPlcyOrPlanOrSchme', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfgrdBnft', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PensionPolicy1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrmntAge', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrwdwnSts', type=DrawdownStatus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LumpSumTp', type=LumpSumType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonWrpprTrf', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RingFncdDrwdwnAssts', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckTrf', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRef', type=TaxReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfScp', type=PensionTransferScope1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdVal', type=DateAndAmount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckTrfRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

