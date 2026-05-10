from . import base_types
from .Max52Text import Max52Text
from .InterestRateContractTerm4 import InterestRateContractTerm4

class InterestRateFrequency3Choice(base_types._BaseFieldType):

	__slots__ = ["_Term", "_Prtry"]
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

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Term', type=InterestRateContractTerm4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
	))

