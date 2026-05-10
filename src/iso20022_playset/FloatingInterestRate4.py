import base_types
import Number
import BenchmarkCurveName4Choice
import InterestRateContractTerm1

class FloatingInterestRate4(base_types._BaseFieldType):

	__slots__ = ["_Term", "_RefRate", "_BsisPtSprd"]
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
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefRate', type=BenchmarkCurveName4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsisPtSprd', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

