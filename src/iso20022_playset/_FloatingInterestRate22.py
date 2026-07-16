# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BenchmarkCurveName10Choice
from . import InterestComputationMethodFormat6Choice
from . import InterestRateContractTerm2
from . import RateAdjustment1
from . import SecuritiesTransactionPrice18Choice

class FloatingInterestRate22(base_types._BaseFieldType):

	__slots__ = ["_DayCntBsis", "_PmtFrqcy", "_RateAdjstmnt", "_RefRate", "_RstFrqcy", "_Sprd", "_Term"]
	@property
	def DayCntBsis(self):
		return self._DayCntBsis

	@DayCntBsis.setter
	def DayCntBsis(self, value):
		self._DayCntBsis = value if value is not None else base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat6Choice, False)

	@DayCntBsis.deleter
	def DayCntBsis(self):
		del self._DayCntBsis
		self._DayCntBsis = base_types.UninitialisedField(self, 'DayCntBsis', InterestComputationMethodFormat6Choice, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', InterestRateContractTerm2, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', InterestRateContractTerm2, False)

	@property
	def RateAdjstmnt(self):
		return self._RateAdjstmnt

	@RateAdjstmnt.setter
	def RateAdjstmnt(self, value):
		self._RateAdjstmnt = value if value is not None else base_types.UninitialisedField(self, 'RateAdjstmnt', RateAdjustment1, True)

	@RateAdjstmnt.deleter
	def RateAdjstmnt(self):
		del self._RateAdjstmnt
		self._RateAdjstmnt = base_types.UninitialisedField(self, 'RateAdjstmnt', RateAdjustment1, True)

	@property
	def RefRate(self):
		return self._RefRate

	@RefRate.setter
	def RefRate(self, value):
		self._RefRate = value if value is not None else base_types.UninitialisedField(self, 'RefRate', BenchmarkCurveName10Choice, False)

	@RefRate.deleter
	def RefRate(self):
		del self._RefRate
		self._RefRate = base_types.UninitialisedField(self, 'RefRate', BenchmarkCurveName10Choice, False)

	@property
	def RstFrqcy(self):
		return self._RstFrqcy

	@RstFrqcy.setter
	def RstFrqcy(self, value):
		self._RstFrqcy = value if value is not None else base_types.UninitialisedField(self, 'RstFrqcy', InterestRateContractTerm2, False)

	@RstFrqcy.deleter
	def RstFrqcy(self):
		del self._RstFrqcy
		self._RstFrqcy = base_types.UninitialisedField(self, 'RstFrqcy', InterestRateContractTerm2, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', SecuritiesTransactionPrice18Choice, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', SecuritiesTransactionPrice18Choice, False)

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if value is not None else base_types.UninitialisedField(self, 'Term', InterestRateContractTerm2, False)

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = base_types.UninitialisedField(self, 'Term', InterestRateContractTerm2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAdjstmnt', type=RateAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefRate', type=BenchmarkCurveName10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstFrqcy', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=SecuritiesTransactionPrice18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
	))