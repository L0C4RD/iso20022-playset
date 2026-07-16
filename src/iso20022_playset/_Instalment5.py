# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage11
from . import ActiveCurrencyAndAmount
from . import Frequency3Code
from . import GracePeriod1
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import InstalmentAmountDetails1
from . import InstalmentPlan1Code
from . import InterestRateDetails1
from . import Max35Text
from . import Number
from . import PlanOwner1Code

class Instalment5(base_types._BaseFieldType):

	__slots__ = ["_Chrgs", "_DtldChrgs", "_FrstAmt", "_FrstPmtDt", "_GracePrd", "_InstlmtPlan", "_InstlmtPrd", "_IntrstRate", "_LastAmt", "_PlanId", "_PlanNtce", "_PlanOwnr", "_PrdUnit", "_SbsqntAmt", "_SeqNb", "_TtlAmt", "_TtlNbOfPmts"]
	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if value is not None else base_types.UninitialisedField(self, 'Chrgs', ImpliedCurrencyAndAmount, False)

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = base_types.UninitialisedField(self, 'Chrgs', ImpliedCurrencyAndAmount, False)

	@property
	def DtldChrgs(self):
		return self._DtldChrgs

	@DtldChrgs.setter
	def DtldChrgs(self, value):
		self._DtldChrgs = value if value is not None else base_types.UninitialisedField(self, 'DtldChrgs', InstalmentAmountDetails1, True)

	@DtldChrgs.deleter
	def DtldChrgs(self):
		del self._DtldChrgs
		self._DtldChrgs = base_types.UninitialisedField(self, 'DtldChrgs', InstalmentAmountDetails1, True)

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
	def GracePrd(self):
		return self._GracePrd

	@GracePrd.setter
	def GracePrd(self, value):
		self._GracePrd = value if value is not None else base_types.UninitialisedField(self, 'GracePrd', GracePeriod1, True)

	@GracePrd.deleter
	def GracePrd(self):
		del self._GracePrd
		self._GracePrd = base_types.UninitialisedField(self, 'GracePrd', GracePeriod1, True)

	@property
	def InstlmtPlan(self):
		return self._InstlmtPlan

	@InstlmtPlan.setter
	def InstlmtPlan(self, value):
		self._InstlmtPlan = value if value is not None else base_types.UninitialisedField(self, 'InstlmtPlan', InstalmentPlan1Code, True)

	@InstlmtPlan.deleter
	def InstlmtPlan(self):
		del self._InstlmtPlan
		self._InstlmtPlan = base_types.UninitialisedField(self, 'InstlmtPlan', InstalmentPlan1Code, True)

	@property
	def InstlmtPrd(self):
		return self._InstlmtPrd

	@InstlmtPrd.setter
	def InstlmtPrd(self, value):
		self._InstlmtPrd = value if value is not None else base_types.UninitialisedField(self, 'InstlmtPrd', Number, False)

	@InstlmtPrd.deleter
	def InstlmtPrd(self):
		del self._InstlmtPrd
		self._InstlmtPrd = base_types.UninitialisedField(self, 'InstlmtPrd', Number, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', InterestRateDetails1, True)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', InterestRateDetails1, True)

	@property
	def LastAmt(self):
		return self._LastAmt

	@LastAmt.setter
	def LastAmt(self, value):
		self._LastAmt = value if value is not None else base_types.UninitialisedField(self, 'LastAmt', ImpliedCurrencyAndAmount, False)

	@LastAmt.deleter
	def LastAmt(self):
		del self._LastAmt
		self._LastAmt = base_types.UninitialisedField(self, 'LastAmt', ImpliedCurrencyAndAmount, False)

	@property
	def PlanId(self):
		return self._PlanId

	@PlanId.setter
	def PlanId(self, value):
		self._PlanId = value if value is not None else base_types.UninitialisedField(self, 'PlanId', Max35Text, False)

	@PlanId.deleter
	def PlanId(self):
		del self._PlanId
		self._PlanId = base_types.UninitialisedField(self, 'PlanId', Max35Text, False)

	@property
	def PlanNtce(self):
		return self._PlanNtce

	@PlanNtce.setter
	def PlanNtce(self, value):
		self._PlanNtce = value if value is not None else base_types.UninitialisedField(self, 'PlanNtce', ActionMessage11, True)

	@PlanNtce.deleter
	def PlanNtce(self):
		del self._PlanNtce
		self._PlanNtce = base_types.UninitialisedField(self, 'PlanNtce', ActionMessage11, True)

	@property
	def PlanOwnr(self):
		return self._PlanOwnr

	@PlanOwnr.setter
	def PlanOwnr(self, value):
		self._PlanOwnr = value if value is not None else base_types.UninitialisedField(self, 'PlanOwnr', PlanOwner1Code, False)

	@PlanOwnr.deleter
	def PlanOwnr(self):
		del self._PlanOwnr
		self._PlanOwnr = base_types.UninitialisedField(self, 'PlanOwnr', PlanOwner1Code, False)

	@property
	def PrdUnit(self):
		return self._PrdUnit

	@PrdUnit.setter
	def PrdUnit(self, value):
		self._PrdUnit = value if value is not None else base_types.UninitialisedField(self, 'PrdUnit', Frequency3Code, False)

	@PrdUnit.deleter
	def PrdUnit(self):
		del self._PrdUnit
		self._PrdUnit = base_types.UninitialisedField(self, 'PrdUnit', Frequency3Code, False)

	@property
	def SbsqntAmt(self):
		return self._SbsqntAmt

	@SbsqntAmt.setter
	def SbsqntAmt(self, value):
		self._SbsqntAmt = value if value is not None else base_types.UninitialisedField(self, 'SbsqntAmt', ImpliedCurrencyAndAmount, False)

	@SbsqntAmt.deleter
	def SbsqntAmt(self):
		del self._SbsqntAmt
		self._SbsqntAmt = base_types.UninitialisedField(self, 'SbsqntAmt', ImpliedCurrencyAndAmount, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ActiveCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ActiveCurrencyAndAmount, False)

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
		base_types.FieldEntry(name='Chrgs', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldChrgs', type=InstalmentAmountDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrstAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GracePrd', type=GracePeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstlmtPlan', type=InstalmentPlan1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstlmtPrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRateDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LastAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlanNtce', type=ActionMessage11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlanOwnr', type=PlanOwner1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdUnit', type=Frequency3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbsqntAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))