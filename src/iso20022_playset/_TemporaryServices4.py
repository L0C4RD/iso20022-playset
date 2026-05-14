from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._Amount13 import Amount13
from ._ISODate import ISODate
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._LocalData20 import LocalData20
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Max5NumericText import Max5NumericText
from ._Max70Text import Max70Text
from ._Max99Text import Max99Text
from ._PhoneNumber import PhoneNumber
from ._Tax44 import Tax44
from ._TemporaryServiceChargeRate1 import TemporaryServiceChargeRate1
from ._TrueFalseIndicator import TrueFalseIndicator

class TemporaryServices4(base_types._BaseFieldType):

	__slots__ = ["_ChrgRate", "_CpnyAdr", "_CpnyBizNm", "_CpnyDept", "_CpnyId", "_CpnyLclData", "_CpnyLglCorpNm", "_CpnyNm", "_CpnySprvsr", "_DscntAmt", "_FlatRateInd", "_JobCd", "_JobDesc", "_JobDrtn", "_JobEndDt", "_JobStartDt", "_MiscExpnss", "_MplyeeId", "_MplyeeNm", "_MplyeePrfssnlLvl", "_MplyeePrsnlId", "_NtlData", "_PrvtData", "_SbttlAmt", "_SummryCmmdtyId", "_Tax", "_TmSheet", "_TtlAmt", "_WkEndg"]
	@property
	def ChrgRate(self):
		return self._ChrgRate

	@ChrgRate.setter
	def ChrgRate(self, value):
		self._ChrgRate = value if type(value) != base_types.auto else self.make_default("ChrgRate")

	@ChrgRate.deleter
	def ChrgRate(self):
		del self._ChrgRate
		self._ChrgRate = None

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
	def CpnyDept(self):
		return self._CpnyDept

	@CpnyDept.setter
	def CpnyDept(self, value):
		self._CpnyDept = value if type(value) != base_types.auto else self.make_default("CpnyDept")

	@CpnyDept.deleter
	def CpnyDept(self):
		del self._CpnyDept
		self._CpnyDept = None

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
	def CpnySprvsr(self):
		return self._CpnySprvsr

	@CpnySprvsr.setter
	def CpnySprvsr(self, value):
		self._CpnySprvsr = value if type(value) != base_types.auto else self.make_default("CpnySprvsr")

	@CpnySprvsr.deleter
	def CpnySprvsr(self):
		del self._CpnySprvsr
		self._CpnySprvsr = None

	@property
	def DscntAmt(self):
		return self._DscntAmt

	@DscntAmt.setter
	def DscntAmt(self, value):
		self._DscntAmt = value if type(value) != base_types.auto else self.make_default("DscntAmt")

	@DscntAmt.deleter
	def DscntAmt(self):
		del self._DscntAmt
		self._DscntAmt = None

	@property
	def FlatRateInd(self):
		return self._FlatRateInd

	@FlatRateInd.setter
	def FlatRateInd(self, value):
		self._FlatRateInd = value if type(value) != base_types.auto else self.make_default("FlatRateInd")

	@FlatRateInd.deleter
	def FlatRateInd(self):
		del self._FlatRateInd
		self._FlatRateInd = None

	@property
	def JobCd(self):
		return self._JobCd

	@JobCd.setter
	def JobCd(self, value):
		self._JobCd = value if type(value) != base_types.auto else self.make_default("JobCd")

	@JobCd.deleter
	def JobCd(self):
		del self._JobCd
		self._JobCd = None

	@property
	def JobDesc(self):
		return self._JobDesc

	@JobDesc.setter
	def JobDesc(self, value):
		self._JobDesc = value if type(value) != base_types.auto else self.make_default("JobDesc")

	@JobDesc.deleter
	def JobDesc(self):
		del self._JobDesc
		self._JobDesc = None

	@property
	def JobDrtn(self):
		return self._JobDrtn

	@JobDrtn.setter
	def JobDrtn(self, value):
		self._JobDrtn = value if type(value) != base_types.auto else self.make_default("JobDrtn")

	@JobDrtn.deleter
	def JobDrtn(self):
		del self._JobDrtn
		self._JobDrtn = None

	@property
	def JobEndDt(self):
		return self._JobEndDt

	@JobEndDt.setter
	def JobEndDt(self, value):
		self._JobEndDt = value if type(value) != base_types.auto else self.make_default("JobEndDt")

	@JobEndDt.deleter
	def JobEndDt(self):
		del self._JobEndDt
		self._JobEndDt = None

	@property
	def JobStartDt(self):
		return self._JobStartDt

	@JobStartDt.setter
	def JobStartDt(self, value):
		self._JobStartDt = value if type(value) != base_types.auto else self.make_default("JobStartDt")

	@JobStartDt.deleter
	def JobStartDt(self):
		del self._JobStartDt
		self._JobStartDt = None

	@property
	def MiscExpnss(self):
		return self._MiscExpnss

	@MiscExpnss.setter
	def MiscExpnss(self, value):
		self._MiscExpnss = value if type(value) != base_types.auto else self.make_default("MiscExpnss")

	@MiscExpnss.deleter
	def MiscExpnss(self):
		del self._MiscExpnss
		self._MiscExpnss = None

	@property
	def MplyeeId(self):
		return self._MplyeeId

	@MplyeeId.setter
	def MplyeeId(self, value):
		self._MplyeeId = value if type(value) != base_types.auto else self.make_default("MplyeeId")

	@MplyeeId.deleter
	def MplyeeId(self):
		del self._MplyeeId
		self._MplyeeId = None

	@property
	def MplyeeNm(self):
		return self._MplyeeNm

	@MplyeeNm.setter
	def MplyeeNm(self, value):
		self._MplyeeNm = value if type(value) != base_types.auto else self.make_default("MplyeeNm")

	@MplyeeNm.deleter
	def MplyeeNm(self):
		del self._MplyeeNm
		self._MplyeeNm = None

	@property
	def MplyeePrfssnlLvl(self):
		return self._MplyeePrfssnlLvl

	@MplyeePrfssnlLvl.setter
	def MplyeePrfssnlLvl(self, value):
		self._MplyeePrfssnlLvl = value if type(value) != base_types.auto else self.make_default("MplyeePrfssnlLvl")

	@MplyeePrfssnlLvl.deleter
	def MplyeePrfssnlLvl(self):
		del self._MplyeePrfssnlLvl
		self._MplyeePrfssnlLvl = None

	@property
	def MplyeePrsnlId(self):
		return self._MplyeePrsnlId

	@MplyeePrsnlId.setter
	def MplyeePrsnlId(self, value):
		self._MplyeePrsnlId = value if type(value) != base_types.auto else self.make_default("MplyeePrsnlId")

	@MplyeePrsnlId.deleter
	def MplyeePrsnlId(self):
		del self._MplyeePrsnlId
		self._MplyeePrsnlId = None

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
	def SbttlAmt(self):
		return self._SbttlAmt

	@SbttlAmt.setter
	def SbttlAmt(self, value):
		self._SbttlAmt = value if type(value) != base_types.auto else self.make_default("SbttlAmt")

	@SbttlAmt.deleter
	def SbttlAmt(self):
		del self._SbttlAmt
		self._SbttlAmt = None

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
	def TmSheet(self):
		return self._TmSheet

	@TmSheet.setter
	def TmSheet(self, value):
		self._TmSheet = value if type(value) != base_types.auto else self.make_default("TmSheet")

	@TmSheet.deleter
	def TmSheet(self):
		del self._TmSheet
		self._TmSheet = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def WkEndg(self):
		return self._WkEndg

	@WkEndg.setter
	def WkEndg(self, value):
		self._WkEndg = value if type(value) != base_types.auto else self.make_default("WkEndg")

	@WkEndg.deleter
	def WkEndg(self):
		del self._WkEndg
		self._WkEndg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgRate', type=TemporaryServiceChargeRate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpnyAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyBizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyDept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnyLclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CpnyLglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
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
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbttlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TmSheet', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WkEndg', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

