# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import CarRentalActivity2Code
from . import ContactBusiness2
from . import CustomerAssigner1Code
from . import DriverInParty4
from . import ISODate
from . import ISOTime
from . import ImpliedCurrencyAndAmount
from . import LocalData20
from . import LoyaltyProgramme4
from . import Max105Text
from . import Max10NumericText
from . import Max35NumericText
from . import Max35Text
from . import Max4NumericText
from . import Max70Text
from . import Max99Text
from . import RentalRate3
from . import Tax44
from . import TrueFalseIndicator
from . import UnitOfMeasure10Code
from . import VehicleRentalAdditionalAmount1

class VehicleRentalService4(base_types._BaseFieldType):

	__slots__ = ["_AddtlAmt", "_AddtlDrvr", "_Adjstd", "_ChckInDt", "_ChckInTm", "_ChckOutDt", "_ChckOutTm", "_ClssInvcd", "_ClssPrvdd", "_CpnyAdr", "_CpnyBizNm", "_CpnyCtct", "_CpnyId", "_CpnyLclData", "_CpnyLglCorpNm", "_CpnyNm", "_CpnyTp", "_Drtn", "_DstncRate", "_DstncUnit", "_FreeDstnc", "_Insrnc", "_LltyPrgrmm", "_MakeInvcd", "_MakePrvdd", "_MdlInvcd", "_MdlPrvdd", "_NoShow", "_NtlData", "_OdmtrRtr", "_OdmtrStart", "_PckpLctn", "_PmryDrvr", "_PrvtData", "_RegnNbInvcd", "_RegnNbPrvdd", "_RntlAgrmtNb", "_RntlLctn", "_RntlRate", "_RntrCorpIdr", "_RntrCorpIdrAssgnr", "_RntrCorpNm", "_RntrNm", "_RtrLctn", "_SummryCmmdtyId", "_Tax", "_TtlDstnc"]
	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlAmt', VehicleRentalAdditionalAmount1, True)

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = base_types.UninitialisedField(self, 'AddtlAmt', VehicleRentalAdditionalAmount1, True)

	@property
	def AddtlDrvr(self):
		return self._AddtlDrvr

	@AddtlDrvr.setter
	def AddtlDrvr(self, value):
		self._AddtlDrvr = value if value is not None else base_types.UninitialisedField(self, 'AddtlDrvr', DriverInParty4, True)

	@AddtlDrvr.deleter
	def AddtlDrvr(self):
		del self._AddtlDrvr
		self._AddtlDrvr = base_types.UninitialisedField(self, 'AddtlDrvr', DriverInParty4, True)

	@property
	def Adjstd(self):
		return self._Adjstd

	@Adjstd.setter
	def Adjstd(self, value):
		self._Adjstd = value if value is not None else base_types.UninitialisedField(self, 'Adjstd', TrueFalseIndicator, False)

	@Adjstd.deleter
	def Adjstd(self):
		del self._Adjstd
		self._Adjstd = base_types.UninitialisedField(self, 'Adjstd', TrueFalseIndicator, False)

	@property
	def ChckInDt(self):
		return self._ChckInDt

	@ChckInDt.setter
	def ChckInDt(self, value):
		self._ChckInDt = value if value is not None else base_types.UninitialisedField(self, 'ChckInDt', ISODate, False)

	@ChckInDt.deleter
	def ChckInDt(self):
		del self._ChckInDt
		self._ChckInDt = base_types.UninitialisedField(self, 'ChckInDt', ISODate, False)

	@property
	def ChckInTm(self):
		return self._ChckInTm

	@ChckInTm.setter
	def ChckInTm(self, value):
		self._ChckInTm = value if value is not None else base_types.UninitialisedField(self, 'ChckInTm', ISOTime, False)

	@ChckInTm.deleter
	def ChckInTm(self):
		del self._ChckInTm
		self._ChckInTm = base_types.UninitialisedField(self, 'ChckInTm', ISOTime, False)

	@property
	def ChckOutDt(self):
		return self._ChckOutDt

	@ChckOutDt.setter
	def ChckOutDt(self, value):
		self._ChckOutDt = value if value is not None else base_types.UninitialisedField(self, 'ChckOutDt', ISODate, False)

	@ChckOutDt.deleter
	def ChckOutDt(self):
		del self._ChckOutDt
		self._ChckOutDt = base_types.UninitialisedField(self, 'ChckOutDt', ISODate, False)

	@property
	def ChckOutTm(self):
		return self._ChckOutTm

	@ChckOutTm.setter
	def ChckOutTm(self, value):
		self._ChckOutTm = value if value is not None else base_types.UninitialisedField(self, 'ChckOutTm', ISOTime, False)

	@ChckOutTm.deleter
	def ChckOutTm(self):
		del self._ChckOutTm
		self._ChckOutTm = base_types.UninitialisedField(self, 'ChckOutTm', ISOTime, False)

	@property
	def ClssInvcd(self):
		return self._ClssInvcd

	@ClssInvcd.setter
	def ClssInvcd(self, value):
		self._ClssInvcd = value if value is not None else base_types.UninitialisedField(self, 'ClssInvcd', Max35Text, False)

	@ClssInvcd.deleter
	def ClssInvcd(self):
		del self._ClssInvcd
		self._ClssInvcd = base_types.UninitialisedField(self, 'ClssInvcd', Max35Text, False)

	@property
	def ClssPrvdd(self):
		return self._ClssPrvdd

	@ClssPrvdd.setter
	def ClssPrvdd(self, value):
		self._ClssPrvdd = value if value is not None else base_types.UninitialisedField(self, 'ClssPrvdd', Max35Text, False)

	@ClssPrvdd.deleter
	def ClssPrvdd(self):
		del self._ClssPrvdd
		self._ClssPrvdd = base_types.UninitialisedField(self, 'ClssPrvdd', Max35Text, False)

	@property
	def CpnyAdr(self):
		return self._CpnyAdr

	@CpnyAdr.setter
	def CpnyAdr(self, value):
		self._CpnyAdr = value if value is not None else base_types.UninitialisedField(self, 'CpnyAdr', Address4, False)

	@CpnyAdr.deleter
	def CpnyAdr(self):
		del self._CpnyAdr
		self._CpnyAdr = base_types.UninitialisedField(self, 'CpnyAdr', Address4, False)

	@property
	def CpnyBizNm(self):
		return self._CpnyBizNm

	@CpnyBizNm.setter
	def CpnyBizNm(self, value):
		self._CpnyBizNm = value if value is not None else base_types.UninitialisedField(self, 'CpnyBizNm', Max35Text, False)

	@CpnyBizNm.deleter
	def CpnyBizNm(self):
		del self._CpnyBizNm
		self._CpnyBizNm = base_types.UninitialisedField(self, 'CpnyBizNm', Max35Text, False)

	@property
	def CpnyCtct(self):
		return self._CpnyCtct

	@CpnyCtct.setter
	def CpnyCtct(self, value):
		self._CpnyCtct = value if value is not None else base_types.UninitialisedField(self, 'CpnyCtct', ContactBusiness2, False)

	@CpnyCtct.deleter
	def CpnyCtct(self):
		del self._CpnyCtct
		self._CpnyCtct = base_types.UninitialisedField(self, 'CpnyCtct', ContactBusiness2, False)

	@property
	def CpnyId(self):
		return self._CpnyId

	@CpnyId.setter
	def CpnyId(self, value):
		self._CpnyId = value if value is not None else base_types.UninitialisedField(self, 'CpnyId', Max35Text, False)

	@CpnyId.deleter
	def CpnyId(self):
		del self._CpnyId
		self._CpnyId = base_types.UninitialisedField(self, 'CpnyId', Max35Text, False)

	@property
	def CpnyLclData(self):
		return self._CpnyLclData

	@CpnyLclData.setter
	def CpnyLclData(self, value):
		self._CpnyLclData = value if value is not None else base_types.UninitialisedField(self, 'CpnyLclData', LocalData20, True)

	@CpnyLclData.deleter
	def CpnyLclData(self):
		del self._CpnyLclData
		self._CpnyLclData = base_types.UninitialisedField(self, 'CpnyLclData', LocalData20, True)

	@property
	def CpnyLglCorpNm(self):
		return self._CpnyLglCorpNm

	@CpnyLglCorpNm.setter
	def CpnyLglCorpNm(self, value):
		self._CpnyLglCorpNm = value if value is not None else base_types.UninitialisedField(self, 'CpnyLglCorpNm', Max99Text, False)

	@CpnyLglCorpNm.deleter
	def CpnyLglCorpNm(self):
		del self._CpnyLglCorpNm
		self._CpnyLglCorpNm = base_types.UninitialisedField(self, 'CpnyLglCorpNm', Max99Text, False)

	@property
	def CpnyNm(self):
		return self._CpnyNm

	@CpnyNm.setter
	def CpnyNm(self, value):
		self._CpnyNm = value if value is not None else base_types.UninitialisedField(self, 'CpnyNm', Max70Text, False)

	@CpnyNm.deleter
	def CpnyNm(self):
		del self._CpnyNm
		self._CpnyNm = base_types.UninitialisedField(self, 'CpnyNm', Max70Text, False)

	@property
	def CpnyTp(self):
		return self._CpnyTp

	@CpnyTp.setter
	def CpnyTp(self, value):
		self._CpnyTp = value if value is not None else base_types.UninitialisedField(self, 'CpnyTp', CarRentalActivity2Code, False)

	@CpnyTp.deleter
	def CpnyTp(self):
		del self._CpnyTp
		self._CpnyTp = base_types.UninitialisedField(self, 'CpnyTp', CarRentalActivity2Code, False)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@property
	def DstncRate(self):
		return self._DstncRate

	@DstncRate.setter
	def DstncRate(self, value):
		self._DstncRate = value if value is not None else base_types.UninitialisedField(self, 'DstncRate', ImpliedCurrencyAndAmount, False)

	@DstncRate.deleter
	def DstncRate(self):
		del self._DstncRate
		self._DstncRate = base_types.UninitialisedField(self, 'DstncRate', ImpliedCurrencyAndAmount, False)

	@property
	def DstncUnit(self):
		return self._DstncUnit

	@DstncUnit.setter
	def DstncUnit(self, value):
		self._DstncUnit = value if value is not None else base_types.UninitialisedField(self, 'DstncUnit', UnitOfMeasure10Code, False)

	@DstncUnit.deleter
	def DstncUnit(self):
		del self._DstncUnit
		self._DstncUnit = base_types.UninitialisedField(self, 'DstncUnit', UnitOfMeasure10Code, False)

	@property
	def FreeDstnc(self):
		return self._FreeDstnc

	@FreeDstnc.setter
	def FreeDstnc(self, value):
		self._FreeDstnc = value if value is not None else base_types.UninitialisedField(self, 'FreeDstnc', Max10NumericText, False)

	@FreeDstnc.deleter
	def FreeDstnc(self):
		del self._FreeDstnc
		self._FreeDstnc = base_types.UninitialisedField(self, 'FreeDstnc', Max10NumericText, False)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, True)

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, True)

	@property
	def MakeInvcd(self):
		return self._MakeInvcd

	@MakeInvcd.setter
	def MakeInvcd(self, value):
		self._MakeInvcd = value if value is not None else base_types.UninitialisedField(self, 'MakeInvcd', Max35NumericText, False)

	@MakeInvcd.deleter
	def MakeInvcd(self):
		del self._MakeInvcd
		self._MakeInvcd = base_types.UninitialisedField(self, 'MakeInvcd', Max35NumericText, False)

	@property
	def MakePrvdd(self):
		return self._MakePrvdd

	@MakePrvdd.setter
	def MakePrvdd(self, value):
		self._MakePrvdd = value if value is not None else base_types.UninitialisedField(self, 'MakePrvdd', Max35NumericText, False)

	@MakePrvdd.deleter
	def MakePrvdd(self):
		del self._MakePrvdd
		self._MakePrvdd = base_types.UninitialisedField(self, 'MakePrvdd', Max35NumericText, False)

	@property
	def MdlInvcd(self):
		return self._MdlInvcd

	@MdlInvcd.setter
	def MdlInvcd(self, value):
		self._MdlInvcd = value if value is not None else base_types.UninitialisedField(self, 'MdlInvcd', Max35NumericText, False)

	@MdlInvcd.deleter
	def MdlInvcd(self):
		del self._MdlInvcd
		self._MdlInvcd = base_types.UninitialisedField(self, 'MdlInvcd', Max35NumericText, False)

	@property
	def MdlPrvdd(self):
		return self._MdlPrvdd

	@MdlPrvdd.setter
	def MdlPrvdd(self, value):
		self._MdlPrvdd = value if value is not None else base_types.UninitialisedField(self, 'MdlPrvdd', Max35NumericText, False)

	@MdlPrvdd.deleter
	def MdlPrvdd(self):
		del self._MdlPrvdd
		self._MdlPrvdd = base_types.UninitialisedField(self, 'MdlPrvdd', Max35NumericText, False)

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if value is not None else base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def OdmtrRtr(self):
		return self._OdmtrRtr

	@OdmtrRtr.setter
	def OdmtrRtr(self, value):
		self._OdmtrRtr = value if value is not None else base_types.UninitialisedField(self, 'OdmtrRtr', Max10NumericText, False)

	@OdmtrRtr.deleter
	def OdmtrRtr(self):
		del self._OdmtrRtr
		self._OdmtrRtr = base_types.UninitialisedField(self, 'OdmtrRtr', Max10NumericText, False)

	@property
	def OdmtrStart(self):
		return self._OdmtrStart

	@OdmtrStart.setter
	def OdmtrStart(self, value):
		self._OdmtrStart = value if value is not None else base_types.UninitialisedField(self, 'OdmtrStart', Max10NumericText, False)

	@OdmtrStart.deleter
	def OdmtrStart(self):
		del self._OdmtrStart
		self._OdmtrStart = base_types.UninitialisedField(self, 'OdmtrStart', Max10NumericText, False)

	@property
	def PckpLctn(self):
		return self._PckpLctn

	@PckpLctn.setter
	def PckpLctn(self, value):
		self._PckpLctn = value if value is not None else base_types.UninitialisedField(self, 'PckpLctn', Address4, True)

	@PckpLctn.deleter
	def PckpLctn(self):
		del self._PckpLctn
		self._PckpLctn = base_types.UninitialisedField(self, 'PckpLctn', Address4, True)

	@property
	def PmryDrvr(self):
		return self._PmryDrvr

	@PmryDrvr.setter
	def PmryDrvr(self, value):
		self._PmryDrvr = value if value is not None else base_types.UninitialisedField(self, 'PmryDrvr', DriverInParty4, False)

	@PmryDrvr.deleter
	def PmryDrvr(self):
		del self._PmryDrvr
		self._PmryDrvr = base_types.UninitialisedField(self, 'PmryDrvr', DriverInParty4, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def RegnNbInvcd(self):
		return self._RegnNbInvcd

	@RegnNbInvcd.setter
	def RegnNbInvcd(self, value):
		self._RegnNbInvcd = value if value is not None else base_types.UninitialisedField(self, 'RegnNbInvcd', Max35Text, False)

	@RegnNbInvcd.deleter
	def RegnNbInvcd(self):
		del self._RegnNbInvcd
		self._RegnNbInvcd = base_types.UninitialisedField(self, 'RegnNbInvcd', Max35Text, False)

	@property
	def RegnNbPrvdd(self):
		return self._RegnNbPrvdd

	@RegnNbPrvdd.setter
	def RegnNbPrvdd(self, value):
		self._RegnNbPrvdd = value if value is not None else base_types.UninitialisedField(self, 'RegnNbPrvdd', Max35Text, False)

	@RegnNbPrvdd.deleter
	def RegnNbPrvdd(self):
		del self._RegnNbPrvdd
		self._RegnNbPrvdd = base_types.UninitialisedField(self, 'RegnNbPrvdd', Max35Text, False)

	@property
	def RntlAgrmtNb(self):
		return self._RntlAgrmtNb

	@RntlAgrmtNb.setter
	def RntlAgrmtNb(self, value):
		self._RntlAgrmtNb = value if value is not None else base_types.UninitialisedField(self, 'RntlAgrmtNb', Max35Text, False)

	@RntlAgrmtNb.deleter
	def RntlAgrmtNb(self):
		del self._RntlAgrmtNb
		self._RntlAgrmtNb = base_types.UninitialisedField(self, 'RntlAgrmtNb', Max35Text, False)

	@property
	def RntlLctn(self):
		return self._RntlLctn

	@RntlLctn.setter
	def RntlLctn(self, value):
		self._RntlLctn = value if value is not None else base_types.UninitialisedField(self, 'RntlLctn', Address4, False)

	@RntlLctn.deleter
	def RntlLctn(self):
		del self._RntlLctn
		self._RntlLctn = base_types.UninitialisedField(self, 'RntlLctn', Address4, False)

	@property
	def RntlRate(self):
		return self._RntlRate

	@RntlRate.setter
	def RntlRate(self, value):
		self._RntlRate = value if value is not None else base_types.UninitialisedField(self, 'RntlRate', RentalRate3, True)

	@RntlRate.deleter
	def RntlRate(self):
		del self._RntlRate
		self._RntlRate = base_types.UninitialisedField(self, 'RntlRate', RentalRate3, True)

	@property
	def RntrCorpIdr(self):
		return self._RntrCorpIdr

	@RntrCorpIdr.setter
	def RntrCorpIdr(self, value):
		self._RntrCorpIdr = value if value is not None else base_types.UninitialisedField(self, 'RntrCorpIdr', Max35Text, False)

	@RntrCorpIdr.deleter
	def RntrCorpIdr(self):
		del self._RntrCorpIdr
		self._RntrCorpIdr = base_types.UninitialisedField(self, 'RntrCorpIdr', Max35Text, False)

	@property
	def RntrCorpIdrAssgnr(self):
		return self._RntrCorpIdrAssgnr

	@RntrCorpIdrAssgnr.setter
	def RntrCorpIdrAssgnr(self, value):
		self._RntrCorpIdrAssgnr = value if value is not None else base_types.UninitialisedField(self, 'RntrCorpIdrAssgnr', CustomerAssigner1Code, False)

	@RntrCorpIdrAssgnr.deleter
	def RntrCorpIdrAssgnr(self):
		del self._RntrCorpIdrAssgnr
		self._RntrCorpIdrAssgnr = base_types.UninitialisedField(self, 'RntrCorpIdrAssgnr', CustomerAssigner1Code, False)

	@property
	def RntrCorpNm(self):
		return self._RntrCorpNm

	@RntrCorpNm.setter
	def RntrCorpNm(self, value):
		self._RntrCorpNm = value if value is not None else base_types.UninitialisedField(self, 'RntrCorpNm', Max70Text, False)

	@RntrCorpNm.deleter
	def RntrCorpNm(self):
		del self._RntrCorpNm
		self._RntrCorpNm = base_types.UninitialisedField(self, 'RntrCorpNm', Max70Text, False)

	@property
	def RntrNm(self):
		return self._RntrNm

	@RntrNm.setter
	def RntrNm(self, value):
		self._RntrNm = value if value is not None else base_types.UninitialisedField(self, 'RntrNm', Max105Text, False)

	@RntrNm.deleter
	def RntrNm(self):
		del self._RntrNm
		self._RntrNm = base_types.UninitialisedField(self, 'RntrNm', Max105Text, False)

	@property
	def RtrLctn(self):
		return self._RtrLctn

	@RtrLctn.setter
	def RtrLctn(self, value):
		self._RtrLctn = value if value is not None else base_types.UninitialisedField(self, 'RtrLctn', Address4, False)

	@RtrLctn.deleter
	def RtrLctn(self):
		del self._RtrLctn
		self._RtrLctn = base_types.UninitialisedField(self, 'RtrLctn', Address4, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax44, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax44, True)

	@property
	def TtlDstnc(self):
		return self._TtlDstnc

	@TtlDstnc.setter
	def TtlDstnc(self, value):
		self._TtlDstnc = value if value is not None else base_types.UninitialisedField(self, 'TtlDstnc', Max10NumericText, False)

	@TtlDstnc.deleter
	def TtlDstnc(self):
		del self._TtlDstnc
		self._TtlDstnc = base_types.UninitialisedField(self, 'TtlDstnc', Max10NumericText, False)

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