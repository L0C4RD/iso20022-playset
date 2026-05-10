from . import base_types
from .AmountAndDirection53 import AmountAndDirection53
from .InterestRate27Choice import InterestRate27Choice

class InterestRate6(base_types._BaseFieldType):

	__slots__ = ["_IntrstRate", "_Amt"]
	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstRate', type=InterestRate27Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountAndDirection53, min=1, max=1, mutex_group=None, array=False),
	))

