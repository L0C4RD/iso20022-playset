import base_types
import BenchmarkCurveName5Choice
import InterestRateContractTerm2

class FloatingInterestRate8(base_types._BaseFieldType):

	__slots__ = ["_Term", "_RefRate"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefRate', type=BenchmarkCurveName5Choice, min=1, max=1, mutex_group=None, array=False),
	))

