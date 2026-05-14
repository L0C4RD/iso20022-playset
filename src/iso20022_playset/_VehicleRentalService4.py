from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._CarRentalActivity2Code import CarRentalActivity2Code
from ._ContactBusiness2 import ContactBusiness2
from ._CustomerAssigner1Code import CustomerAssigner1Code
from ._DriverInParty4 import DriverInParty4
from ._ISODate import ISODate
from ._ISOTime import ISOTime
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._LocalData20 import LocalData20
from ._LoyaltyProgramme4 import LoyaltyProgramme4
from ._Max105Text import Max105Text
from ._Max10NumericText import Max10NumericText
from ._Max35NumericText import Max35NumericText
from ._Max35Text import Max35Text
from ._Max4NumericText import Max4NumericText
from ._Max70Text import Max70Text
from ._Max99Text import Max99Text
from ._RentalRate3 import RentalRate3
from ._Tax44 import Tax44
from ._TrueFalseIndicator import TrueFalseIndicator
from ._UnitOfMeasure10Code import UnitOfMeasure10Code
from ._VehicleRentalAdditionalAmount1 import VehicleRentalAdditionalAmount1

class VehicleRentalService4(base_types._BaseFieldType):

	__slots__ = ["_AddtlAmt", "_AddtlDrvr", "_Adjstd", "_ChckInDt", "_ChckInTm", "_ChckOutDt", "_ChckOutTm", "_ClssInvcd", "_ClssPrvdd", "_CpnyAdr", "_CpnyBizNm", "_CpnyCtct", "_CpnyId", "_CpnyLclData", "_CpnyLglCorpNm", "_CpnyNm", "_CpnyTp", "_Drtn", "_DstncRate", "_DstncUnit", "_FreeDstnc", "_Insrnc", "_LltyPrgrmm", "_MakeInvcd", "_MakePrvdd", "_MdlInvcd", "_MdlPrvdd", "_NoShow", "_NtlData", "_OdmtrRtr", "_OdmtrStart", "_PckpLctn", "_PmryDrvr", "_PrvtData", "_RegnNbInvcd", "_RegnNbPrvdd", "_RntlAgrmtNb", "_RntlLctn", "_RntlRate", "_RntrCorpIdr", "_RntrCorpIdrAssgnr", "_RntrCorpNm", "_RntrNm", "_RtrLctn", "_SummryCmmdtyId", "_Tax", "_TtlDstnc"]
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
	def AddtlDrvr(self):
		return self._AddtlDrvr

	@AddtlDrvr.setter
	def AddtlDrvr(self, value):
		self._AddtlDrvr = value if type(value) != base_types.auto else self.make_default("AddtlDrvr")

	@AddtlDrvr.deleter
	def AddtlDrvr(self):
		del self._AddtlDrvr
		self._AddtlDrvr = None

	@property
	def Adjstd(self):
		return self._Adjstd

	@Adjstd.setter
	def Adjstd(self, value):
		self._Adjstd = value if type(value) != base_types.auto else self.make_default("Adjstd")

	@Adjstd.deleter
	def Adjstd(self):
		del self._Adjstd
		self._Adjstd = None

	@property
	def ChckInDt(self):
		return self._ChckInDt

	@ChckInDt.setter
	def ChckInDt(self, value):
		self._ChckInDt = value if type(value) != base_types.auto else self.make_default("ChckInDt")

	@ChckInDt.deleter
	def ChckInDt(self):
		del self._ChckInDt
		self._ChckInDt = None

	@property
	def ChckInTm(self):
		return self._ChckInTm

	@ChckInTm.setter
	def ChckInTm(self, value):
		self._ChckInTm = value if type(value) != base_types.auto else self.make_default("ChckInTm")

	@ChckInTm.deleter
	def ChckInTm(self):
		del self._ChckInTm
		self._ChckInTm = None

	@property
	def ChckOutDt(self):
		return self._ChckOutDt

	@ChckOutDt.setter
	def ChckOutDt(self, value):
		self._ChckOutDt = value if type(value) != base_types.auto else self.make_default("ChckOutDt")

	@ChckOutDt.deleter
	def ChckOutDt(self):
		del self._ChckOutDt
		self._ChckOutDt = None

	@property
	def ChckOutTm(self):
		return self._ChckOutTm

	@ChckOutTm.setter
	def ChckOutTm(self, value):
		self._ChckOutTm = value if type(value) != base_types.auto else self.make_default("ChckOutTm")

	@ChckOutTm.deleter
	def ChckOutTm(self):
		del self._ChckOutTm
		self._ChckOutTm = None

	@property
	def ClssInvcd(self):
		return self._ClssInvcd

	@ClssInvcd.setter
	def ClssInvcd(self, value):
		self._ClssInvcd = value if type(value) != base_types.auto else self.make_default("ClssInvcd")

	@ClssInvcd.deleter
	def ClssInvcd(self):
		del self._ClssInvcd
		self._ClssInvcd = None

	@property
	def ClssPrvdd(self):
		return self._ClssPrvdd

	@ClssPrvdd.setter
	def ClssPrvdd(self, value):
		self._ClssPrvdd = value if type(value) != base_types.auto else self.make_default("ClssPrvdd")

	@ClssPrvdd.deleter
	def ClssPrvdd(self):
		del self._ClssPrvdd
		self._ClssPrvdd = None

	@property
	def CpnyAdr(self):
		return self._CpnyAdr

	@CpnyAdr.setter
	def CpnyAdr(self, value):
		self._CpnyAdr = value if type(value) != base_types.auto else self.make_default("CpnyAdr")

	@CpnyAdr.deleter
	def CpnyAdr(self):
		del self._CpnyAdr
		self._CpnyAdr = None

	@property
	def CpnyBizNm(self):
		return self._CpnyBizNm

	@CpnyBizNm.setter
	def CpnyBizNm(self, value):
		self._CpnyBizNm = value if type(value) != base_types.auto else self.make_default("CpnyBizNm")

	@CpnyBizNm.deleter
	def CpnyBizNm(self):
		del self._CpnyBizNm
		self._CpnyBizNm = None

	@property
	def CpnyCtct(self):
		return self._CpnyCtct

	@CpnyCtct.setter
	def CpnyCtct(self, value):
		self._CpnyCtct = value if type(value) != base_types.auto else self.make_default("CpnyCtct")

	@CpnyCtct.deleter
	def CpnyCtct(self):
		del self._CpnyCtct
		self._CpnyCtct = None

	@property
	def CpnyId(self):
		return self._CpnyId

	@CpnyId.setter
	def CpnyId(self, value):
		self._CpnyId = value if type(value) != base_types.auto else self.make_default("CpnyId")

	@CpnyId.deleter
	def CpnyId(self):
		del self._CpnyId
		self._CpnyId = None

	@property
	def CpnyLclData(self):
		return self._CpnyLclData

	@CpnyLclData.setter
	def CpnyLclData(self, value):
		self._CpnyLclData = value if type(value) != base_types.auto else self.make_default("CpnyLclData")

	@CpnyLclData.deleter
	def CpnyLclData(self):
		del self._CpnyLclData
		self._CpnyLclData = None

	@property
	def CpnyLglCorpNm(self):
		return self._CpnyLglCorpNm

	@CpnyLglCorpNm.setter
	def CpnyLglCorpNm(self, value):
		self._CpnyLglCorpNm = value if type(value) != base_types.auto else self.make_default("CpnyLglCorpNm")

	@CpnyLglCorpNm.deleter
	def CpnyLglCorpNm(self):
		del self._CpnyLglCorpNm
		self._CpnyLglCorpNm = None

	@property
	def CpnyNm(self):
		return self._CpnyNm

	@CpnyNm.setter
	def CpnyNm(self, value):
		self._CpnyNm = value if type(value) != base_types.auto else self.make_default("CpnyNm")

	@CpnyNm.deleter
	def CpnyNm(self):
		del self._CpnyNm
		self._CpnyNm = None

	@property
	def CpnyTp(self):
		return self._CpnyTp

	@CpnyTp.setter
	def CpnyTp(self, value):
		self._CpnyTp = value if type(value) != base_types.auto else self.make_default("CpnyTp")

	@CpnyTp.deleter
	def CpnyTp(self):
		del self._CpnyTp
		self._CpnyTp = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def DstncRate(self):
		return self._DstncRate

	@DstncRate.setter
	def DstncRate(self, value):
		self._DstncRate = value if type(value) != base_types.auto else self.make_default("DstncRate")

	@DstncRate.deleter
	def DstncRate(self):
		del self._DstncRate
		self._DstncRate = None

	@property
	def DstncUnit(self):
		return self._DstncUnit

	@DstncUnit.setter
	def DstncUnit(self, value):
		self._DstncUnit = value if type(value) != base_types.auto else self.make_default("DstncUnit")

	@DstncUnit.deleter
	def DstncUnit(self):
		del self._DstncUnit
		self._DstncUnit = None

	@property
	def FreeDstnc(self):
		return self._FreeDstnc

	@FreeDstnc.setter
	def FreeDstnc(self, value):
		self._FreeDstnc = value if type(value) != base_types.auto else self.make_default("FreeDstnc")

	@FreeDstnc.deleter
	def FreeDstnc(self):
		del self._FreeDstnc
		self._FreeDstnc = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != base_types.auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if type(value) != base_types.auto else self.make_default("LltyPrgrmm")

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = None

	@property
	def MakeInvcd(self):
		return self._MakeInvcd

	@MakeInvcd.setter
	def MakeInvcd(self, value):
		self._MakeInvcd = value if type(value) != base_types.auto else self.make_default("MakeInvcd")

	@MakeInvcd.deleter
	def MakeInvcd(self):
		del self._MakeInvcd
		self._MakeInvcd = None

	@property
	def MakePrvdd(self):
		return self._MakePrvdd

	@MakePrvdd.setter
	def MakePrvdd(self, value):
		self._MakePrvdd = value if type(value) != base_types.auto else self.make_default("MakePrvdd")

	@MakePrvdd.deleter
	def MakePrvdd(self):
		del self._MakePrvdd
		self._MakePrvdd = None

	@property
	def MdlInvcd(self):
		return self._MdlInvcd

	@MdlInvcd.setter
	def MdlInvcd(self, value):
		self._MdlInvcd = value if type(value) != base_types.auto else self.make_default("MdlInvcd")

	@MdlInvcd.deleter
	def MdlInvcd(self):
		del self._MdlInvcd
		self._MdlInvcd = None

	@property
	def MdlPrvdd(self):
		return self._MdlPrvdd

	@MdlPrvdd.setter
	def MdlPrvdd(self, value):
		self._MdlPrvdd = value if type(value) != base_types.auto else self.make_default("MdlPrvdd")

	@MdlPrvdd.deleter
	def MdlPrvdd(self):
		del self._MdlPrvdd
		self._MdlPrvdd = None

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if type(value) != base_types.auto else self.make_default("NoShow")

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def OdmtrRtr(self):
		return self._OdmtrRtr

	@OdmtrRtr.setter
	def OdmtrRtr(self, value):
		self._OdmtrRtr = value if type(value) != base_types.auto else self.make_default("OdmtrRtr")

	@OdmtrRtr.deleter
	def OdmtrRtr(self):
		del self._OdmtrRtr
		self._OdmtrRtr = None

	@property
	def OdmtrStart(self):
		return self._OdmtrStart

	@OdmtrStart.setter
	def OdmtrStart(self, value):
		self._OdmtrStart = value if type(value) != base_types.auto else self.make_default("OdmtrStart")

	@OdmtrStart.deleter
	def OdmtrStart(self):
		del self._OdmtrStart
		self._OdmtrStart = None

	@property
	def PckpLctn(self):
		return self._PckpLctn

	@PckpLctn.setter
	def PckpLctn(self, value):
		self._PckpLctn = value if type(value) != base_types.auto else self.make_default("PckpLctn")

	@PckpLctn.deleter
	def PckpLctn(self):
		del self._PckpLctn
		self._PckpLctn = None

	@property
	def PmryDrvr(self):
		return self._PmryDrvr

	@PmryDrvr.setter
	def PmryDrvr(self, value):
		self._PmryDrvr = value if type(value) != base_types.auto else self.make_default("PmryDrvr")

	@PmryDrvr.deleter
	def PmryDrvr(self):
		del self._PmryDrvr
		self._PmryDrvr = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def RegnNbInvcd(self):
		return self._RegnNbInvcd

	@RegnNbInvcd.setter
	def RegnNbInvcd(self, value):
		self._RegnNbInvcd = value if type(value) != base_types.auto else self.make_default("RegnNbInvcd")

	@RegnNbInvcd.deleter
	def RegnNbInvcd(self):
		del self._RegnNbInvcd
		self._RegnNbInvcd = None

	@property
	def RegnNbPrvdd(self):
		return self._RegnNbPrvdd

	@RegnNbPrvdd.setter
	def RegnNbPrvdd(self, value):
		self._RegnNbPrvdd = value if type(value) != base_types.auto else self.make_default("RegnNbPrvdd")

	@RegnNbPrvdd.deleter
	def RegnNbPrvdd(self):
		del self._RegnNbPrvdd
		self._RegnNbPrvdd = None

	@property
	def RntlAgrmtNb(self):
		return self._RntlAgrmtNb

	@RntlAgrmtNb.setter
	def RntlAgrmtNb(self, value):
		self._RntlAgrmtNb = value if type(value) != base_types.auto else self.make_default("RntlAgrmtNb")

	@RntlAgrmtNb.deleter
	def RntlAgrmtNb(self):
		del self._RntlAgrmtNb
		self._RntlAgrmtNb = None

	@property
	def RntlLctn(self):
		return self._RntlLctn

	@RntlLctn.setter
	def RntlLctn(self, value):
		self._RntlLctn = value if type(value) != base_types.auto else self.make_default("RntlLctn")

	@RntlLctn.deleter
	def RntlLctn(self):
		del self._RntlLctn
		self._RntlLctn = None

	@property
	def RntlRate(self):
		return self._RntlRate

	@RntlRate.setter
	def RntlRate(self, value):
		self._RntlRate = value if type(value) != base_types.auto else self.make_default("RntlRate")

	@RntlRate.deleter
	def RntlRate(self):
		del self._RntlRate
		self._RntlRate = None

	@property
	def RntrCorpIdr(self):
		return self._RntrCorpIdr

	@RntrCorpIdr.setter
	def RntrCorpIdr(self, value):
		self._RntrCorpIdr = value if type(value) != base_types.auto else self.make_default("RntrCorpIdr")

	@RntrCorpIdr.deleter
	def RntrCorpIdr(self):
		del self._RntrCorpIdr
		self._RntrCorpIdr = None

	@property
	def RntrCorpIdrAssgnr(self):
		return self._RntrCorpIdrAssgnr

	@RntrCorpIdrAssgnr.setter
	def RntrCorpIdrAssgnr(self, value):
		self._RntrCorpIdrAssgnr = value if type(value) != base_types.auto else self.make_default("RntrCorpIdrAssgnr")

	@RntrCorpIdrAssgnr.deleter
	def RntrCorpIdrAssgnr(self):
		del self._RntrCorpIdrAssgnr
		self._RntrCorpIdrAssgnr = None

	@property
	def RntrCorpNm(self):
		return self._RntrCorpNm

	@RntrCorpNm.setter
	def RntrCorpNm(self, value):
		self._RntrCorpNm = value if type(value) != base_types.auto else self.make_default("RntrCorpNm")

	@RntrCorpNm.deleter
	def RntrCorpNm(self):
		del self._RntrCorpNm
		self._RntrCorpNm = None

	@property
	def RntrNm(self):
		return self._RntrNm

	@RntrNm.setter
	def RntrNm(self, value):
		self._RntrNm = value if type(value) != base_types.auto else self.make_default("RntrNm")

	@RntrNm.deleter
	def RntrNm(self):
		del self._RntrNm
		self._RntrNm = None

	@property
	def RtrLctn(self):
		return self._RtrLctn

	@RtrLctn.setter
	def RtrLctn(self, value):
		self._RtrLctn = value if type(value) != base_types.auto else self.make_default("RtrLctn")

	@RtrLctn.deleter
	def RtrLctn(self):
		del self._RtrLctn
		self._RtrLctn = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != base_types.auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def TtlDstnc(self):
		return self._TtlDstnc

	@TtlDstnc.setter
	def TtlDstnc(self, value):
		self._TtlDstnc = value if type(value) != base_types.auto else self.make_default("TtlDstnc")

	@TtlDstnc.deleter
	def TtlDstnc(self):
		del self._TtlDstnc
		self._TtlDstnc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAmt', type=VehicleRentalAdditionalAmount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlDrvr', type=DriverInParty4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adjstd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckOutDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckOutTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssInvcd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssPrvdd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyBizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyCtct', type=ContactBusiness2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyLclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpnyLglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyTp', type=CarRentalActivity2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstncRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstncUnit', type=UnitOfMeasure10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FreeDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MakeInvcd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MakePrvdd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlInvcd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlPrvdd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OdmtrRtr', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrStart', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PckpLctn', type=Address4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmryDrvr', type=DriverInParty4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnNbInvcd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNbPrvdd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlAgrmtNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlLctn', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlRate', type=RentalRate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RntrCorpIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpIdrAssgnr', type=CustomerAssigner1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrCorpNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntrNm', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrLctn', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
	))

