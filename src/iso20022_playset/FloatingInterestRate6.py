from . import base_types
from .Max5Number import Max5Number
from .BenchmarkCurveName6Choice import BenchmarkCurveName6Choice
from .InterestRateContractTerm2 import InterestRateContractTerm2

class FloatingInterestRate6(base_types._BaseFieldType):

	__slots__ = ["_RefRate", "_Term", "_BsisPtSprd"]
	@property
	def RefRate(self):
		return self._RefRate

	@RefRate.setter
	def RefRate(self, value):
		self._RefRate = value if type(value) != auto else self.make_default("RefRate")

	@RefRate.deleter
	def RefRate(self):
		del self._RefRate
		self._RefRate = None

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if type(value) != auto else self.make_default("Term")

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = None

	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if type(value) != auto else self.make_default("BsisPtSprd")

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefRate', type=BenchmarkCurveName6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsisPtSprd', type=Max5Number, min=1, max=1, mutex_group=None, array=False),
	))

