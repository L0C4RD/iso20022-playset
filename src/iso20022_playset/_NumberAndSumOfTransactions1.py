from . import base_types
from ._Max15NumericText import Max15NumericText
from ._DecimalNumber import DecimalNumber

class NumberAndSumOfTransactions1(base_types._BaseFieldType):

	__slots__ = ["_NbOfNtries", "_Sum"]
	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if type(value) != base_types.auto else self.make_default("NbOfNtries")

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = None

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if type(value) != base_types.auto else self.make_default("Sum")

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

