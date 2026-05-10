from . import base_types
from ._CompareDecimalNumber3 import CompareDecimalNumber3
from ._ComparePercentageRate3 import ComparePercentageRate3
from ._CompareInterestComputationMethod3 import CompareInterestComputationMethod3
from ._CompareNumber5 import CompareNumber5
from ._CompareRateBasis3 import CompareRateBasis3
from ._CompareBenchmarkCurveName3 import CompareBenchmarkCurveName3
from ._CompareAmountAndDirection1 import CompareAmountAndDirection1
from ._CompareNumber6 import CompareNumber6

class CompareInterestRate1(base_types._BaseFieldType):

	__slots__ = ["_DayCntBsis", "_FltgIntrstRatePmtFrqcyUnit", "_FltgIntrstRefRate", "_FxdIntrstRate", "_FltgIntrstRateTermUnit", "_BsisPtSprd", "_FltgIntrstRateTermVal", "_FltgIntrstRateRstFrqcyVal", "_FltgIntrstRatePmtFrqcyVal", "_MrgnLnAmt", "_FltgIntrstRateRstFrqcyUnit"]
	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if type(value) != base_types.auto else self.make_default("DayCntBsis")

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = None

	@property
	def FltgIntrstRatePmtFrqcyUnit(self):
		return self._FltgIntrstRatePmtFrqcyUnit

	@FltgIntrstRatePmtFrqcyUnit.setter
	def FltgIntrstRatePmtFrqcyUnit(self, value):
		self._FltgIntrstRatePmtFrqcyUnit = value if type(value) != base_types.auto else self.make_default("FltgIntrstRatePmtFrqcyUnit")

	@FltgIntrstRatePmtFrqcyUnit.deleter
	def FltgIntrstRatePmtFrqcyUnit(self):
		del self._FltgIntrstRatePmtFrqcyUnit
		self._FltgIntrstRatePmtFrqcyUnit = None

	@property
	def FltgIntrstRefRate(self):
		return self._FltgIntrstRefRate

	@FltgIntrstRefRate.setter
	def FltgIntrstRefRate(self, value):
		self._FltgIntrstRefRate = value if type(value) != base_types.auto else self.make_default("FltgIntrstRefRate")

	@FltgIntrstRefRate.deleter
	def FltgIntrstRefRate(self):
		del self._FltgIntrstRefRate
		self._FltgIntrstRefRate = None

	@property
	def FxdIntrstRate(self):
		return self._FxdIntrstRate

	@FxdIntrstRate.setter
	def FxdIntrstRate(self, value):
		self._FxdIntrstRate = value if type(value) != base_types.auto else self.make_default("FxdIntrstRate")

	@FxdIntrstRate.deleter
	def FxdIntrstRate(self):
		del self._FxdIntrstRate
		self._FxdIntrstRate = None

	@property
	def FltgIntrstRateTermUnit(self):
		return self._FltgIntrstRateTermUnit

	@FltgIntrstRateTermUnit.setter
	def FltgIntrstRateTermUnit(self, value):
		self._FltgIntrstRateTermUnit = value if type(value) != base_types.auto else self.make_default("FltgIntrstRateTermUnit")

	@FltgIntrstRateTermUnit.deleter
	def FltgIntrstRateTermUnit(self):
		del self._FltgIntrstRateTermUnit
		self._FltgIntrstRateTermUnit = None

	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if type(value) != base_types.auto else self.make_default("BsisPtSprd")

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = None

	@property
	def FltgIntrstRateTermVal(self):
		return self._FltgIntrstRateTermVal

	@FltgIntrstRateTermVal.setter
	def FltgIntrstRateTermVal(self, value):
		self._FltgIntrstRateTermVal = value if type(value) != base_types.auto else self.make_default("FltgIntrstRateTermVal")

	@FltgIntrstRateTermVal.deleter
	def FltgIntrstRateTermVal(self):
		del self._FltgIntrstRateTermVal
		self._FltgIntrstRateTermVal = None

	@property
	def FltgIntrstRateRstFrqcyVal(self):
		return self._FltgIntrstRateRstFrqcyVal

	@FltgIntrstRateRstFrqcyVal.setter
	def FltgIntrstRateRstFrqcyVal(self, value):
		self._FltgIntrstRateRstFrqcyVal = value if type(value) != base_types.auto else self.make_default("FltgIntrstRateRstFrqcyVal")

	@FltgIntrstRateRstFrqcyVal.deleter
	def FltgIntrstRateRstFrqcyVal(self):
		del self._FltgIntrstRateRstFrqcyVal
		self._FltgIntrstRateRstFrqcyVal = None

	@property
	def FltgIntrstRatePmtFrqcyVal(self):
		return self._FltgIntrstRatePmtFrqcyVal

	@FltgIntrstRatePmtFrqcyVal.setter
	def FltgIntrstRatePmtFrqcyVal(self, value):
		self._FltgIntrstRatePmtFrqcyVal = value if type(value) != base_types.auto else self.make_default("FltgIntrstRatePmtFrqcyVal")

	@FltgIntrstRatePmtFrqcyVal.deleter
	def FltgIntrstRatePmtFrqcyVal(self):
		del self._FltgIntrstRatePmtFrqcyVal
		self._FltgIntrstRatePmtFrqcyVal = None

	@property
	def MrgnLnAmt(self):
		return self._MrgnLnAmt

	@MrgnLnAmt.setter
	def MrgnLnAmt(self, value):
		self._MrgnLnAmt = value if type(value) != base_types.auto else self.make_default("MrgnLnAmt")

	@MrgnLnAmt.deleter
	def MrgnLnAmt(self):
		del self._MrgnLnAmt
		self._MrgnLnAmt = None

	@property
	def FltgIntrstRateRstFrqcyUnit(self):
		return self._FltgIntrstRateRstFrqcyUnit

	@FltgIntrstRateRstFrqcyUnit.setter
	def FltgIntrstRateRstFrqcyUnit(self, value):
		self._FltgIntrstRateRstFrqcyUnit = value if type(value) != base_types.auto else self.make_default("FltgIntrstRateRstFrqcyUnit")

	@FltgIntrstRateRstFrqcyUnit.deleter
	def FltgIntrstRateRstFrqcyUnit(self):
		del self._FltgIntrstRateRstFrqcyUnit
		self._FltgIntrstRateRstFrqcyUnit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayCntBsis', type=CompareInterestComputationMethod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRefRate', type=CompareBenchmarkCurveName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxdIntrstRate', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsisPtSprd', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLnAmt', type=CompareAmountAndDirection1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
	))

