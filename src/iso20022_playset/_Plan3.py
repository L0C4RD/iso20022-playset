# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Frequency18Code
from . import GracePeriodUnitType1Code
from . import ISO3NumericCurrencyCode
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import InstalmentAmountDetails3
from . import InterestRateDetails2
from . import Max256Text
from . import Max35Text
from . import Max3NumericText
from . import Max70Text
from . import Number
from . import PlanOwner1Code
from . import TrueFalseIndicator

class Plan3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AmtDtls", "_Ccy", "_CstmrSelctdGracePrd", "_Dfrrd", "_DfrrdPrds", "_FrstAmt", "_FrstPmtDt", "_GracePrdUnitTp", "_GrdTtlAmt", "_Id", "_IntrstRate", "_NbOfGracePrdUnits", "_NbOfPrds", "_NrmlPmtAmt", "_OthrGracePrdUnitTp", "_OthrOwnr", "_Ownr", "_OwnrNm", "_PmtTp", "_PrdUnit", "_RegnSysId", "_TtlNbOfPmts"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def AmtDtls(self):
		return self._AmtDtls

	@AmtDtls.setter
	def AmtDtls(self, value):
		self._AmtDtls = value if value is not None else base_types.UninitialisedField(self, 'AmtDtls', InstalmentAmountDetails3, True)

	@AmtDtls.deleter
	def AmtDtls(self):
		del self._AmtDtls
		self._AmtDtls = base_types.UninitialisedField(self, 'AmtDtls', InstalmentAmountDetails3, True)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@property
	def CstmrSelctdGracePrd(self):
		return self._CstmrSelctdGracePrd

	@CstmrSelctdGracePrd.setter
	def CstmrSelctdGracePrd(self, value):
		self._CstmrSelctdGracePrd = value if value is not None else base_types.UninitialisedField(self, 'CstmrSelctdGracePrd', TrueFalseIndicator, False)

	@CstmrSelctdGracePrd.deleter
	def CstmrSelctdGracePrd(self):
		del self._CstmrSelctdGracePrd
		self._CstmrSelctdGracePrd = base_types.UninitialisedField(self, 'CstmrSelctdGracePrd', TrueFalseIndicator, False)

	@property
	def Dfrrd(self):
		return self._Dfrrd

	@Dfrrd.setter
	def Dfrrd(self, value):
		self._Dfrrd = value if value is not None else base_types.UninitialisedField(self, 'Dfrrd', TrueFalseIndicator, False)

	@Dfrrd.deleter
	def Dfrrd(self):
		del self._Dfrrd
		self._Dfrrd = base_types.UninitialisedField(self, 'Dfrrd', TrueFalseIndicator, False)

	@property
	def DfrrdPrds(self):
		return self._DfrrdPrds

	@DfrrdPrds.setter
	def DfrrdPrds(self, value):
		self._DfrrdPrds = value if value is not None else base_types.UninitialisedField(self, 'DfrrdPrds', Number, False)

	@DfrrdPrds.deleter
	def DfrrdPrds(self):
		del self._DfrrdPrds
		self._DfrrdPrds = base_types.UninitialisedField(self, 'DfrrdPrds', Number, False)

	@property
	def FrstAmt(self):
		return self._FrstAmt

	@FrstAmt.setter
	def FrstAmt(self, value):
		self._FrstAmt = value if value is not None else base_types.UninitialisedField(self, 'FrstAmt', ImpliedCurrencyAndAmount, False)

	@FrstAmt.deleter
	def FrstAmt(self):
		del self._FrstAmt
		self._FrstAmt = base_types.UninitialisedField(self, 'FrstAmt', ImpliedCurrencyAndAmount, False)

	@property
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'FrstPmtDt', ISODate, False)

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = base_types.UninitialisedField(self, 'FrstPmtDt', ISODate, False)

	@property
	def GracePrdUnitTp(self):
		return self._GracePrdUnitTp

	@GracePrdUnitTp.setter
	def GracePrdUnitTp(self, value):
		self._GracePrdUnitTp = value if value is not None else base_types.UninitialisedField(self, 'GracePrdUnitTp', GracePeriodUnitType1Code, False)

	@GracePrdUnitTp.deleter
	def GracePrdUnitTp(self):
		del self._GracePrdUnitTp
		self._GracePrdUnitTp = base_types.UninitialisedField(self, 'GracePrdUnitTp', GracePeriodUnitType1Code, False)

	@property
	def GrdTtlAmt(self):
		return self._GrdTtlAmt

	@GrdTtlAmt.setter
	def GrdTtlAmt(self, value):
		self._GrdTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'GrdTtlAmt', ImpliedCurrencyAndAmount, False)

	@GrdTtlAmt.deleter
	def GrdTtlAmt(self):
		del self._GrdTtlAmt
		self._GrdTtlAmt = base_types.UninitialisedField(self, 'GrdTtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', InterestRateDetails2, True)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', InterestRateDetails2, True)

	@property
	def NbOfGracePrdUnits(self):
		return self._NbOfGracePrdUnits

	@NbOfGracePrdUnits.setter
	def NbOfGracePrdUnits(self, value):
		self._NbOfGracePrdUnits = value if value is not None else base_types.UninitialisedField(self, 'NbOfGracePrdUnits', Max3NumericText, False)

	@NbOfGracePrdUnits.deleter
	def NbOfGracePrdUnits(self):
		del self._NbOfGracePrdUnits
		self._NbOfGracePrdUnits = base_types.UninitialisedField(self, 'NbOfGracePrdUnits', Max3NumericText, False)

	@property
	def NbOfPrds(self):
		return self._NbOfPrds

	@NbOfPrds.setter
	def NbOfPrds(self, value):
		self._NbOfPrds = value if value is not None else base_types.UninitialisedField(self, 'NbOfPrds', Number, False)

	@NbOfPrds.deleter
	def NbOfPrds(self):
		del self._NbOfPrds
		self._NbOfPrds = base_types.UninitialisedField(self, 'NbOfPrds', Number, False)

	@property
	def NrmlPmtAmt(self):
		return self._NrmlPmtAmt

	@NrmlPmtAmt.setter
	def NrmlPmtAmt(self, value):
		self._NrmlPmtAmt = value if value is not None else base_types.UninitialisedField(self, 'NrmlPmtAmt', ImpliedCurrencyAndAmount, False)

	@NrmlPmtAmt.deleter
	def NrmlPmtAmt(self):
		del self._NrmlPmtAmt
		self._NrmlPmtAmt = base_types.UninitialisedField(self, 'NrmlPmtAmt', ImpliedCurrencyAndAmount, False)

	@property
	def OthrGracePrdUnitTp(self):
		return self._OthrGracePrdUnitTp

	@OthrGracePrdUnitTp.setter
	def OthrGracePrdUnitTp(self, value):
		self._OthrGracePrdUnitTp = value if value is not None else base_types.UninitialisedField(self, 'OthrGracePrdUnitTp', Max35Text, False)

	@OthrGracePrdUnitTp.deleter
	def OthrGracePrdUnitTp(self):
		del self._OthrGracePrdUnitTp
		self._OthrGracePrdUnitTp = base_types.UninitialisedField(self, 'OthrGracePrdUnitTp', Max35Text, False)

	@property
	def OthrOwnr(self):
		return self._OthrOwnr

	@OthrOwnr.setter
	def OthrOwnr(self, value):
		self._OthrOwnr = value if value is not None else base_types.UninitialisedField(self, 'OthrOwnr', Max35Text, False)

	@OthrOwnr.deleter
	def OthrOwnr(self):
		del self._OthrOwnr
		self._OthrOwnr = base_types.UninitialisedField(self, 'OthrOwnr', Max35Text, False)

	@property
	def Ownr(self):
		return self._Ownr

	@Ownr.setter
	def Ownr(self, value):
		self._Ownr = value if value is not None else base_types.UninitialisedField(self, 'Ownr', PlanOwner1Code, False)

	@Ownr.deleter
	def Ownr(self):
		del self._Ownr
		self._Ownr = base_types.UninitialisedField(self, 'Ownr', PlanOwner1Code, False)

	@property
	def OwnrNm(self):
		return self._OwnrNm

	@OwnrNm.setter
	def OwnrNm(self, value):
		self._OwnrNm = value if value is not None else base_types.UninitialisedField(self, 'OwnrNm', Max256Text, False)

	@OwnrNm.deleter
	def OwnrNm(self):
		del self._OwnrNm
		self._OwnrNm = base_types.UninitialisedField(self, 'OwnrNm', Max256Text, False)

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if value is not None else base_types.UninitialisedField(self, 'PmtTp', Max35Text, False)

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = base_types.UninitialisedField(self, 'PmtTp', Max35Text, False)

	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if value is not None else base_types.UninitialisedField(self, 'PrdUnit', Frequency18Code, False)

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = base_types.UninitialisedField(self, 'PrdUnit', Frequency18Code, False)

	@property
	def RegnSysId(self):
		return self._RegnSysId

	@RegnSysId.setter
	def RegnSysId(self, value):
		self._RegnSysId = value if value is not None else base_types.UninitialisedField(self, 'RegnSysId', Max35Text, False)

	@RegnSysId.deleter
	def RegnSysId(self):
		del self._RegnSysId
		self._RegnSysId = base_types.UninitialisedField(self, 'RegnSysId', Max35Text, False)

	@property
	def TtlNbOfPmts(self):
		return self._TtlNbOfPmts

	@TtlNbOfPmts.setter
	def TtlNbOfPmts(self, value):
		self._TtlNbOfPmts = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfPmts', Number, False)

	@TtlNbOfPmts.deleter
	def TtlNbOfPmts(self):
		del self._TtlNbOfPmts
		self._TtlNbOfPmts = base_types.UninitialisedField(self, 'TtlNbOfPmts', Number, False)

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