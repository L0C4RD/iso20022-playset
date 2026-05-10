import base_types
import InterestRateDetails1
import ImpliedCurrencyAndAmount
import ISODate
import Frequency3Code
import InstalmentAmountDetails1
import Max35Text
import InstalmentPlan1Code
import PlanOwner1Code
import GracePeriod1
import Number
import ActiveCurrencyAndAmount
import ActionMessage11

class Instalment5(base_types._BaseFieldType):

	__slots__ = ["_TtlNbOfPmts", "_InstlmtPlan", "_FrstAmt", "_SeqNb", "_Chrgs", "_IntrstRate", "_TtlAmt", "_DtldChrgs", "_LastAmt", "_PlanOwnr", "_SbsqntAmt", "_PlanNtce", "_PlanId", "_GracePrd", "_FrstPmtDt", "_InstlmtPrd", "_PrdUnit"]
	@property
	def TtlNbOfPmts(self):
		return self._TtlNbOfPmts

	@TtlNbOfPmts.setter
	def TtlNbOfPmts(self, value):
		self._TtlNbOfPmts = value if type(value) != auto else self.make_default("TtlNbOfPmts")

	@TtlNbOfPmts.deleter
	def TtlNbOfPmts(self):
		del self._TtlNbOfPmts
		self._TtlNbOfPmts = None

	@property
	def InstlmtPlan(self):
		return self._InstlmtPlan

	@InstlmtPlan.setter
	def InstlmtPlan(self, value):
		self._InstlmtPlan = value if type(value) != auto else self.make_default("InstlmtPlan")

	@InstlmtPlan.deleter
	def InstlmtPlan(self):
		del self._InstlmtPlan
		self._InstlmtPlan = None

	@property
	def FrstAmt(self):
		return self._FrstAmt

	@FrstAmt.setter
	def FrstAmt(self, value):
		self._FrstAmt = value if type(value) != auto else self.make_default("FrstAmt")

	@FrstAmt.deleter
	def FrstAmt(self):
		del self._FrstAmt
		self._FrstAmt = None

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if type(value) != auto else self.make_default("Chrgs")

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def DtldChrgs(self):
		return self._DtldChrgs

	@DtldChrgs.setter
	def DtldChrgs(self, value):
		self._DtldChrgs = value if type(value) != auto else self.make_default("DtldChrgs")

	@DtldChrgs.deleter
	def DtldChrgs(self):
		del self._DtldChrgs
		self._DtldChrgs = None

	@property
	def LastAmt(self):
		return self._LastAmt

	@LastAmt.setter
	def LastAmt(self, value):
		self._LastAmt = value if type(value) != auto else self.make_default("LastAmt")

	@LastAmt.deleter
	def LastAmt(self):
		del self._LastAmt
		self._LastAmt = None

	@property
	def PlanOwnr(self):
		return self._PlanOwnr

	@PlanOwnr.setter
	def PlanOwnr(self, value):
		self._PlanOwnr = value if type(value) != auto else self.make_default("PlanOwnr")

	@PlanOwnr.deleter
	def PlanOwnr(self):
		del self._PlanOwnr
		self._PlanOwnr = None

	@property
	def SbsqntAmt(self):
		return self._SbsqntAmt

	@SbsqntAmt.setter
	def SbsqntAmt(self, value):
		self._SbsqntAmt = value if type(value) != auto else self.make_default("SbsqntAmt")

	@SbsqntAmt.deleter
	def SbsqntAmt(self):
		del self._SbsqntAmt
		self._SbsqntAmt = None

	@property
	def PlanNtce(self):
		return self._PlanNtce

	@PlanNtce.setter
	def PlanNtce(self, value):
		self._PlanNtce = value if type(value) != auto else self.make_default("PlanNtce")

	@PlanNtce.deleter
	def PlanNtce(self):
		del self._PlanNtce
		self._PlanNtce = None

	@property
	def PlanId(self):
		return self._PlanId

	@PlanId.setter
	def PlanId(self, value):
		self._PlanId = value if type(value) != auto else self.make_default("PlanId")

	@PlanId.deleter
	def PlanId(self):
		del self._PlanId
		self._PlanId = None

	@property
	def GracePrd(self):
		return self._GracePrd

	@GracePrd.setter
	def GracePrd(self, value):
		self._GracePrd = value if type(value) != auto else self.make_default("GracePrd")

	@GracePrd.deleter
	def GracePrd(self):
		del self._GracePrd
		self._GracePrd = None

	@property
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if type(value) != auto else self.make_default("FrstPmtDt")

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = None

	@property
	def InstlmtPrd(self):
		return self._InstlmtPrd

	@InstlmtPrd.setter
	def InstlmtPrd(self, value):
		self._InstlmtPrd = value if type(value) != auto else self.make_default("InstlmtPrd")

	@InstlmtPrd.deleter
	def InstlmtPrd(self):
		del self._InstlmtPrd
		self._InstlmtPrd = None

	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if type(value) != auto else self.make_default("PrdUnit")

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlNbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtPlan', type=InstalmentPlan1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrstAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrgs', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRateDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldChrgs', type=InstalmentAmountDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LastAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanOwnr', type=PlanOwner1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbsqntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanNtce', type=ActionMessage11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlanId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GracePrd', type=GracePeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtPrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdUnit', type=Frequency3Code, min=0, max=1, mutex_group=None, array=False),
	))

