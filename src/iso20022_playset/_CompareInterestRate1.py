# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareAmountAndDirection1
from . import CompareBenchmarkCurveName3
from . import CompareDecimalNumber3
from . import CompareInterestComputationMethod3
from . import CompareNumber5
from . import CompareNumber6
from . import ComparePercentageRate3
from . import CompareRateBasis3

class CompareInterestRate1(base_types._BaseFieldType):

	__slots__ = ["_BsisPtSprd", "_DayCntBsis", "_FltgIntrstRatePmtFrqcyUnit", "_FltgIntrstRatePmtFrqcyVal", "_FltgIntrstRateRstFrqcyUnit", "_FltgIntrstRateRstFrqcyVal", "_FltgIntrstRateTermUnit", "_FltgIntrstRateTermVal", "_FltgIntrstRefRate", "_FxdIntrstRate", "_MrgnLnAmt"]
	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if value is not None else base_types.UninitialisedField(self, 'BsisPtSprd', CompareDecimalNumber3, False)

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = base_types.UninitialisedField(self, 'BsisPtSprd', CompareDecimalNumber3, False)

	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', CompareInterestComputationMethod3, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', CompareInterestComputationMethod3, False)

	@property
	def FltgIntrstRatePmtFrqcyUnit(self):
		return self._FltgIntrstRatePmtFrqcyUnit

	@FltgIntrstRatePmtFrqcyUnit.setter
	def FltgIntrstRatePmtFrqcyUnit(self, value):
		self._FltgIntrstRatePmtFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyUnit', CompareRateBasis3, False)

	@FltgIntrstRatePmtFrqcyUnit.deleter
	def FltgIntrstRatePmtFrqcyUnit(self):
		del self._FltgIntrstRatePmtFrqcyUnit
		self._FltgIntrstRatePmtFrqcyUnit = base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyUnit', CompareRateBasis3, False)

	@property
	def FltgIntrstRatePmtFrqcyVal(self):
		return self._FltgIntrstRatePmtFrqcyVal

	@FltgIntrstRatePmtFrqcyVal.setter
	def FltgIntrstRatePmtFrqcyVal(self, value):
		self._FltgIntrstRatePmtFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyVal', CompareNumber5, False)

	@FltgIntrstRatePmtFrqcyVal.deleter
	def FltgIntrstRatePmtFrqcyVal(self):
		del self._FltgIntrstRatePmtFrqcyVal
		self._FltgIntrstRatePmtFrqcyVal = base_types.UninitialisedField(self, 'FltgIntrstRatePmtFrqcyVal', CompareNumber5, False)

	@property
	def FltgIntrstRateRstFrqcyUnit(self):
		return self._FltgIntrstRateRstFrqcyUnit

	@FltgIntrstRateRstFrqcyUnit.setter
	def FltgIntrstRateRstFrqcyUnit(self, value):
		self._FltgIntrstRateRstFrqcyUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyUnit', CompareRateBasis3, False)

	@FltgIntrstRateRstFrqcyUnit.deleter
	def FltgIntrstRateRstFrqcyUnit(self):
		del self._FltgIntrstRateRstFrqcyUnit
		self._FltgIntrstRateRstFrqcyUnit = base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyUnit', CompareRateBasis3, False)

	@property
	def FltgIntrstRateRstFrqcyVal(self):
		return self._FltgIntrstRateRstFrqcyVal

	@FltgIntrstRateRstFrqcyVal.setter
	def FltgIntrstRateRstFrqcyVal(self, value):
		self._FltgIntrstRateRstFrqcyVal = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyVal', CompareNumber6, False)

	@FltgIntrstRateRstFrqcyVal.deleter
	def FltgIntrstRateRstFrqcyVal(self):
		del self._FltgIntrstRateRstFrqcyVal
		self._FltgIntrstRateRstFrqcyVal = base_types.UninitialisedField(self, 'FltgIntrstRateRstFrqcyVal', CompareNumber6, False)

	@property
	def FltgIntrstRateTermUnit(self):
		return self._FltgIntrstRateTermUnit

	@FltgIntrstRateTermUnit.setter
	def FltgIntrstRateTermUnit(self, value):
		self._FltgIntrstRateTermUnit = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateTermUnit', CompareRateBasis3, False)

	@FltgIntrstRateTermUnit.deleter
	def FltgIntrstRateTermUnit(self):
		del self._FltgIntrstRateTermUnit
		self._FltgIntrstRateTermUnit = base_types.UninitialisedField(self, 'FltgIntrstRateTermUnit', CompareRateBasis3, False)

	@property
	def FltgIntrstRateTermVal(self):
		return self._FltgIntrstRateTermVal

	@FltgIntrstRateTermVal.setter
	def FltgIntrstRateTermVal(self, value):
		self._FltgIntrstRateTermVal = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRateTermVal', CompareNumber5, False)

	@FltgIntrstRateTermVal.deleter
	def FltgIntrstRateTermVal(self):
		del self._FltgIntrstRateTermVal
		self._FltgIntrstRateTermVal = base_types.UninitialisedField(self, 'FltgIntrstRateTermVal', CompareNumber5, False)

	@property
	def FltgIntrstRefRate(self):
		return self._FltgIntrstRefRate

	@FltgIntrstRefRate.setter
	def FltgIntrstRefRate(self, value):
		self._FltgIntrstRefRate = value if value is not None else base_types.UninitialisedField(self, 'FltgIntrstRefRate', CompareBenchmarkCurveName3, False)

	@FltgIntrstRefRate.deleter
	def FltgIntrstRefRate(self):
		del self._FltgIntrstRefRate
		self._FltgIntrstRefRate = base_types.UninitialisedField(self, 'FltgIntrstRefRate', CompareBenchmarkCurveName3, False)

	@property
	def FxdIntrstRate(self):
		return self._FxdIntrstRate

	@FxdIntrstRate.setter
	def FxdIntrstRate(self, value):
		self._FxdIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'FxdIntrstRate', ComparePercentageRate3, False)

	@FxdIntrstRate.deleter
	def FxdIntrstRate(self):
		del self._FxdIntrstRate
		self._FxdIntrstRate = base_types.UninitialisedField(self, 'FxdIntrstRate', ComparePercentageRate3, False)

	@property
	def MrgnLnAmt(self):
		return self._MrgnLnAmt

	@MrgnLnAmt.setter
	def MrgnLnAmt(self, value):
		self._MrgnLnAmt = value if value is not None else base_types.UninitialisedField(self, 'MrgnLnAmt', CompareAmountAndDirection1, False)

	@MrgnLnAmt.deleter
	def MrgnLnAmt(self):
		del self._MrgnLnAmt
		self._MrgnLnAmt = base_types.UninitialisedField(self, 'MrgnLnAmt', CompareAmountAndDirection1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPtSprd', type=CompareDecimalNumber3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DayCntBsis', type=CompareInterestComputationMethod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRatePmtFrqcyVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateRstFrqcyVal', type=CompareNumber6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermUnit', type=CompareRateBasis3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRateTermVal', type=CompareNumber5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FltgIntrstRefRate', type=CompareBenchmarkCurveName3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxdIntrstRate', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnLnAmt', type=CompareAmountAndDirection1, min=0, max=1, mutex_group=None, array=False),
	))