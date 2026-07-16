# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Amount12
from . import Amount13
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max256Text
from . import Max35Text
from . import Max5NumericText
from . import Max70Text
from . import PartyIdentification285
from . import PhoneNumber
from . import Tax41
from . import TrueFalseIndicator

class TemporaryServices3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Chrg", "_CpnyDept", "_CpnyId", "_CpnyNm", "_CpnySprvsr", "_DscntAmt", "_FlatRateInd", "_JobCd", "_JobDesc", "_JobDrtn", "_JobEndDt", "_JobStartDt", "_MiscExpnss", "_MplyeeId", "_MplyeeNm", "_MplyeePrfssnlLvl", "_MplyeePrsnlId", "_SbttlAmt", "_SummryCmmdtyId", "_Tax", "_TmSheet", "_WkEndg"]
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
	def Chrg(self):
		return self._Chrg

	@Chrg.setter
	def Chrg(self, value):
		self._Chrg = value if value is not None else base_types.UninitialisedField(self, 'Chrg', Amount12, True)

	@Chrg.deleter
	def Chrg(self):
		del self._Chrg
		self._Chrg = base_types.UninitialisedField(self, 'Chrg', Amount12, True)

	@property
	def CpnyDept(self):
		return self._CpnyDept

	@CpnyDept.setter
	def CpnyDept(self, value):
		self._CpnyDept = value if value is not None else base_types.UninitialisedField(self, 'CpnyDept', Max70Text, False)

	@CpnyDept.deleter
	def CpnyDept(self):
		del self._CpnyDept
		self._CpnyDept = base_types.UninitialisedField(self, 'CpnyDept', Max70Text, False)

	@property
	def CpnyId(self):
		return self._CpnyId

	@CpnyId.setter
	def CpnyId(self, value):
		self._CpnyId = value if value is not None else base_types.UninitialisedField(self, 'CpnyId', PartyIdentification285, False)

	@CpnyId.deleter
	def CpnyId(self):
		del self._CpnyId
		self._CpnyId = base_types.UninitialisedField(self, 'CpnyId', PartyIdentification285, False)

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
	def CpnySprvsr(self):
		return self._CpnySprvsr

	@CpnySprvsr.setter
	def CpnySprvsr(self, value):
		self._CpnySprvsr = value if value is not None else base_types.UninitialisedField(self, 'CpnySprvsr', Max70Text, False)

	@CpnySprvsr.deleter
	def CpnySprvsr(self):
		del self._CpnySprvsr
		self._CpnySprvsr = base_types.UninitialisedField(self, 'CpnySprvsr', Max70Text, False)

	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if value is not None else base_types.UninitialisedField(self, 'DscntAmt', ImpliedCurrencyAndAmount, False)

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = base_types.UninitialisedField(self, 'DscntAmt', ImpliedCurrencyAndAmount, False)

	@property
	def FlatRateInd(self):
		return self._FlatRateInd

	@FlatRateInd.setter
	def FlatRateInd(self, value):
		self._FlatRateInd = value if value is not None else base_types.UninitialisedField(self, 'FlatRateInd', TrueFalseIndicator, False)

	@FlatRateInd.deleter
	def FlatRateInd(self):
		del self._FlatRateInd
		self._FlatRateInd = base_types.UninitialisedField(self, 'FlatRateInd', TrueFalseIndicator, False)

	@property
	def JobCd(self):
		return self._JobCd

	@JobCd.setter
	def JobCd(self, value):
		self._JobCd = value if value is not None else base_types.UninitialisedField(self, 'JobCd', Max35Text, False)

	@JobCd.deleter
	def JobCd(self):
		del self._JobCd
		self._JobCd = base_types.UninitialisedField(self, 'JobCd', Max35Text, False)

	@property
	def JobDesc(self):
		return self._JobDesc

	@JobDesc.setter
	def JobDesc(self, value):
		self._JobDesc = value if value is not None else base_types.UninitialisedField(self, 'JobDesc', Max256Text, False)

	@JobDesc.deleter
	def JobDesc(self):
		del self._JobDesc
		self._JobDesc = base_types.UninitialisedField(self, 'JobDesc', Max256Text, False)

	@property
	def JobDrtn(self):
		return self._JobDrtn

	@JobDrtn.setter
	def JobDrtn(self, value):
		self._JobDrtn = value if value is not None else base_types.UninitialisedField(self, 'JobDrtn', Max5NumericText, False)

	@JobDrtn.deleter
	def JobDrtn(self):
		del self._JobDrtn
		self._JobDrtn = base_types.UninitialisedField(self, 'JobDrtn', Max5NumericText, False)

	@property
	def JobEndDt(self):
		return self._JobEndDt

	@JobEndDt.setter
	def JobEndDt(self, value):
		self._JobEndDt = value if value is not None else base_types.UninitialisedField(self, 'JobEndDt', ISODate, False)

	@JobEndDt.deleter
	def JobEndDt(self):
		del self._JobEndDt
		self._JobEndDt = base_types.UninitialisedField(self, 'JobEndDt', ISODate, False)

	@property
	def JobStartDt(self):
		return self._JobStartDt

	@JobStartDt.setter
	def JobStartDt(self, value):
		self._JobStartDt = value if value is not None else base_types.UninitialisedField(self, 'JobStartDt', ISODate, False)

	@JobStartDt.deleter
	def JobStartDt(self):
		del self._JobStartDt
		self._JobStartDt = base_types.UninitialisedField(self, 'JobStartDt', ISODate, False)

	@property
	def MiscExpnss(self):
		return self._MiscExpnss

	@MiscExpnss.setter
	def MiscExpnss(self, value):
		self._MiscExpnss = value if value is not None else base_types.UninitialisedField(self, 'MiscExpnss', Amount13, True)

	@MiscExpnss.deleter
	def MiscExpnss(self):
		del self._MiscExpnss
		self._MiscExpnss = base_types.UninitialisedField(self, 'MiscExpnss', Amount13, True)

	@property
	def MplyeeId(self):
		return self._MplyeeId

	@MplyeeId.setter
	def MplyeeId(self, value):
		self._MplyeeId = value if value is not None else base_types.UninitialisedField(self, 'MplyeeId', PhoneNumber, False)

	@MplyeeId.deleter
	def MplyeeId(self):
		del self._MplyeeId
		self._MplyeeId = base_types.UninitialisedField(self, 'MplyeeId', PhoneNumber, False)

	@property
	def MplyeeNm(self):
		return self._MplyeeNm

	@MplyeeNm.setter
	def MplyeeNm(self, value):
		self._MplyeeNm = value if value is not None else base_types.UninitialisedField(self, 'MplyeeNm', Max70Text, False)

	@MplyeeNm.deleter
	def MplyeeNm(self):
		del self._MplyeeNm
		self._MplyeeNm = base_types.UninitialisedField(self, 'MplyeeNm', Max70Text, False)

	@property
	def MplyeePrfssnlLvl(self):
		return self._MplyeePrfssnlLvl

	@MplyeePrfssnlLvl.setter
	def MplyeePrfssnlLvl(self, value):
		self._MplyeePrfssnlLvl = value if value is not None else base_types.UninitialisedField(self, 'MplyeePrfssnlLvl', Max35Text, False)

	@MplyeePrfssnlLvl.deleter
	def MplyeePrfssnlLvl(self):
		del self._MplyeePrfssnlLvl
		self._MplyeePrfssnlLvl = base_types.UninitialisedField(self, 'MplyeePrfssnlLvl', Max35Text, False)

	@property
	def MplyeePrsnlId(self):
		return self._MplyeePrsnlId

	@MplyeePrsnlId.setter
	def MplyeePrsnlId(self, value):
		self._MplyeePrsnlId = value if value is not None else base_types.UninitialisedField(self, 'MplyeePrsnlId', Max35Text, False)

	@MplyeePrsnlId.deleter
	def MplyeePrsnlId(self):
		del self._MplyeePrsnlId
		self._MplyeePrsnlId = base_types.UninitialisedField(self, 'MplyeePrsnlId', Max35Text, False)

	@property
	def SbttlAmt(self):
		return self._SbttlAmt

	@SbttlAmt.setter
	def SbttlAmt(self, value):
		self._SbttlAmt = value if value is not None else base_types.UninitialisedField(self, 'SbttlAmt', ImpliedCurrencyAndAmount, False)

	@SbttlAmt.deleter
	def SbttlAmt(self):
		del self._SbttlAmt
		self._SbttlAmt = base_types.UninitialisedField(self, 'SbttlAmt', ImpliedCurrencyAndAmount, False)

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
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@property
	def TmSheet(self):
		return self._TmSheet

	@TmSheet.setter
	def TmSheet(self, value):
		self._TmSheet = value if value is not None else base_types.UninitialisedField(self, 'TmSheet', Max35Text, False)

	@TmSheet.deleter
	def TmSheet(self):
		del self._TmSheet
		self._TmSheet = base_types.UninitialisedField(self, 'TmSheet', Max35Text, False)

	@property
	def WkEndg(self):
		return self._WkEndg

	@WkEndg.setter
	def WkEndg(self, value):
		self._WkEndg = value if value is not None else base_types.UninitialisedField(self, 'WkEndg', ISODate, False)

	@WkEndg.deleter
	def WkEndg(self):
		del self._WkEndg
		self._WkEndg = base_types.UninitialisedField(self, 'WkEndg', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Chrg', type=Amount12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpnyDept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnySprvsr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlatRateInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobDesc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobDrtn', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobStartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MiscExpnss', type=Amount13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MplyeeId', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyeeNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyeePrfssnlLvl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MplyeePrsnlId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbttlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TmSheet', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WkEndg', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))