from . import base_types
from ._ISODate import ISODate
from ._TrueFalseIndicator import TrueFalseIndicator
from ._InterestRateDetails2 import InterestRateDetails2
from ._InstalmentAmountDetails3 import InstalmentAmountDetails3
from ._PlanOwner1Code import PlanOwner1Code
from ._Number import Number
from ._AdditionalData1 import AdditionalData1
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._Max3NumericText import Max3NumericText
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._GracePeriodUnitType1Code import GracePeriodUnitType1Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Frequency18Code import Frequency18Code

class Plan3(base_types._BaseFieldType):

	__slots__ = ["_NbOfGracePrdUnits", "_GracePrdUnitTp", "_Ownr", "_FrstPmtDt", "_GrdTtlAmt", "_CstmrSelctdGracePrd", "_AddtlData", "_OthrOwnr", "_OwnrNm", "_OthrGracePrdUnitTp", "_AmtDtls", "_FrstAmt", "_Ccy", "_NbOfPrds", "_RegnSysId", "_IntrstRate", "_NrmlPmtAmt", "_Id", "_DfrrdPrds", "_TtlNbOfPmts", "_PrdUnit", "_PmtTp", "_Dfrrd"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if type(value) != base_types.auto else self.make_default("AmtDtls")

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CstmrSelctdGracePrd(self):
		return self._CstmrSelctdGracePrd

	@CstmrSelctdGracePrd.setter
	def CstmrSelctdGracePrd(self, value):
		self._CstmrSelctdGracePrd = value if type(value) != base_types.auto else self.make_default("CstmrSelctdGracePrd")

	@CstmrSelctdGracePrd.deleter
	def CstmrSelctdGracePrd(self):
		del self._CstmrSelctdGracePrd
		self._CstmrSelctdGracePrd = None

	@property
	def Dfrrd(self):
		return self._Dfrrd

	@Dfrrd.setter
	def Dfrrd(self, value):
		self._Dfrrd = value if type(value) != base_types.auto else self.make_default("Dfrrd")

	@Dfrrd.deleter
	def Dfrrd(self):
		del self._Dfrrd
		self._Dfrrd = None

	@property
	def DfrrdPrds(self):
		return self._DfrrdPrds

	@DfrrdPrds.setter
	def DfrrdPrds(self, value):
		self._DfrrdPrds = value if type(value) != base_types.auto else self.make_default("DfrrdPrds")

	@DfrrdPrds.deleter
	def DfrrdPrds(self):
		del self._DfrrdPrds
		self._DfrrdPrds = None

	@property
	def FrstAmt(self):
		return self._FrstAmt

	@FrstAmt.setter
	def FrstAmt(self, value):
		self._FrstAmt = value if type(value) != base_types.auto else self.make_default("FrstAmt")

	@FrstAmt.deleter
	def FrstAmt(self):
		del self._FrstAmt
		self._FrstAmt = None

	@property
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if type(value) != base_types.auto else self.make_default("FrstPmtDt")

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = None

	@property
	def GracePrdUnitTp(self):
		return self._GracePrdUnitTp

	@GracePrdUnitTp.setter
	def GracePrdUnitTp(self, value):
		self._GracePrdUnitTp = value if type(value) != base_types.auto else self.make_default("GracePrdUnitTp")

	@GracePrdUnitTp.deleter
	def GracePrdUnitTp(self):
		del self._GracePrdUnitTp
		self._GracePrdUnitTp = None

	@property
	def GrdTtlAmt(self):
		return self._GrdTtlAmt

	@GrdTtlAmt.setter
	def GrdTtlAmt(self, value):
		self._GrdTtlAmt = value if type(value) != base_types.auto else self.make_default("GrdTtlAmt")

	@GrdTtlAmt.deleter
	def GrdTtlAmt(self):
		del self._GrdTtlAmt
		self._GrdTtlAmt = None

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
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def NbOfGracePrdUnits(self):
		return self._NbOfGracePrdUnits

	@NbOfGracePrdUnits.setter
	def NbOfGracePrdUnits(self, value):
		self._NbOfGracePrdUnits = value if type(value) != base_types.auto else self.make_default("NbOfGracePrdUnits")

	@NbOfGracePrdUnits.deleter
	def NbOfGracePrdUnits(self):
		del self._NbOfGracePrdUnits
		self._NbOfGracePrdUnits = None

	@property
	def NbOfPrds(self):
		return self._NbOfPrds

	@NbOfPrds.setter
	def NbOfPrds(self, value):
		self._NbOfPrds = value if type(value) != base_types.auto else self.make_default("NbOfPrds")

	@NbOfPrds.deleter
	def NbOfPrds(self):
		del self._NbOfPrds
		self._NbOfPrds = None

	@property
	def NrmlPmtAmt(self):
		return self._NrmlPmtAmt

	@NrmlPmtAmt.setter
	def NrmlPmtAmt(self, value):
		self._NrmlPmtAmt = value if type(value) != base_types.auto else self.make_default("NrmlPmtAmt")

	@NrmlPmtAmt.deleter
	def NrmlPmtAmt(self):
		del self._NrmlPmtAmt
		self._NrmlPmtAmt = None

	@property
	def OthrGracePrdUnitTp(self):
		return self._OthrGracePrdUnitTp

	@OthrGracePrdUnitTp.setter
	def OthrGracePrdUnitTp(self, value):
		self._OthrGracePrdUnitTp = value if type(value) != base_types.auto else self.make_default("OthrGracePrdUnitTp")

	@OthrGracePrdUnitTp.deleter
	def OthrGracePrdUnitTp(self):
		del self._OthrGracePrdUnitTp
		self._OthrGracePrdUnitTp = None

	@property
	def OthrOwnr(self):
		return self._OthrOwnr

	@OthrOwnr.setter
	def OthrOwnr(self, value):
		self._OthrOwnr = value if type(value) != base_types.auto else self.make_default("OthrOwnr")

	@OthrOwnr.deleter
	def OthrOwnr(self):
		del self._OthrOwnr
		self._OthrOwnr = None

	@property
	def Ownr(self):
		return self._Ownr

	@Ownr.setter
	def Ownr(self, value):
		self._Ownr = value if type(value) != base_types.auto else self.make_default("Ownr")

	@Ownr.deleter
	def Ownr(self):
		del self._Ownr
		self._Ownr = None

	@property
	def OwnrNm(self):
		return self._OwnrNm

	@OwnrNm.setter
	def OwnrNm(self, value):
		self._OwnrNm = value if type(value) != base_types.auto else self.make_default("OwnrNm")

	@OwnrNm.deleter
	def OwnrNm(self):
		del self._OwnrNm
		self._OwnrNm = None

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if type(value) != base_types.auto else self.make_default("PmtTp")

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = None

	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if type(value) != base_types.auto else self.make_default("PrdUnit")

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = None

	@property
	def RegnSysId(self):
		return self._RegnSysId

	@RegnSysId.setter
	def RegnSysId(self, value):
		self._RegnSysId = value if type(value) != base_types.auto else self.make_default("RegnSysId")

	@RegnSysId.deleter
	def RegnSysId(self):
		del self._RegnSysId
		self._RegnSysId = None

	@property
	def TtlNbOfPmts(self):
		return self._TtlNbOfPmts

	@TtlNbOfPmts.setter
	def TtlNbOfPmts(self, value):
		self._TtlNbOfPmts = value if type(value) != base_types.auto else self.make_default("TtlNbOfPmts")

	@TtlNbOfPmts.deleter
	def TtlNbOfPmts(self):
		del self._TtlNbOfPmts
		self._TtlNbOfPmts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtDtls', type=InstalmentAmountDetails3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrSelctdGracePrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dfrrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdPrds', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GracePrdUnitTp', type=GracePeriodUnitType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrdTtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRateDetails2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfGracePrdUnits', type=Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfPrds', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrmlPmtAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrGracePrdUnitTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrOwnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ownr', type=PlanOwner1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrNm', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdUnit', type=Frequency18Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnSysId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

