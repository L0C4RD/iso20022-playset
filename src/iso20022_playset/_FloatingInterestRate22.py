from . import base_types
from ._BenchmarkCurveName10Choice import BenchmarkCurveName10Choice
from ._InterestComputationMethodFormat6Choice import InterestComputationMethodFormat6Choice
from ._InterestRateContractTerm2 import InterestRateContractTerm2
from ._RateAdjustment1 import RateAdjustment1
from ._SecuritiesTransactionPrice18Choice import SecuritiesTransactionPrice18Choice

class FloatingInterestRate22(base_types._BaseFieldType):

	__slots__ = ["_DayCntBsis", "_PmtFrqcy", "_RateAdjstmnt", "_RefRate", "_RstFrqcy", "_Sprd", "_Term"]
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
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != base_types.auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def RateAdjstmnt(self):
		return self._RateAdjstmnt

	@RateAdjstmnt.setter
	def RateAdjstmnt(self, value):
		self._RateAdjstmnt = value if type(value) != base_types.auto else self.make_default("RateAdjstmnt")

	@RateAdjstmnt.deleter
	def RateAdjstmnt(self):
		del self._RateAdjstmnt
		self._RateAdjstmnt = None

	@property
	def RefRate(self):
		return self._RefRate

	@RefRate.setter
	def RefRate(self, value):
		self._RefRate = value if type(value) != base_types.auto else self.make_default("RefRate")

	@RefRate.deleter
	def RefRate(self):
		del self._RefRate
		self._RefRate = None

	@property
	def RstFrqcy(self):
		return self._RstFrqcy

	@RstFrqcy.setter
	def RstFrqcy(self, value):
		self._RstFrqcy = value if type(value) != base_types.auto else self.make_default("RstFrqcy")

	@RstFrqcy.deleter
	def RstFrqcy(self):
		del self._RstFrqcy
		self._RstFrqcy = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != base_types.auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if type(value) != base_types.auto else self.make_default("Term")

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayCntBsis', type=InterestComputationMethodFormat6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateAdjstmnt', type=RateAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefRate', type=BenchmarkCurveName10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstFrqcy', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=SecuritiesTransactionPrice18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
	))

