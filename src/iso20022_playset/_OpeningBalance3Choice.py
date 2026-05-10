from . import base_types
from .FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1

class OpeningBalance3Choice(base_types._BaseFieldType):

	__slots__ = ["_FrstOpngBal", "_IntrmyOpngBal"]
	@property
	def FrstOpngBal(self):
		return self._FrstOpngBal

	@FrstOpngBal.setter
	def FrstOpngBal(self, value):
		self._FrstOpngBal = value if type(value) != base_types.auto else self.make_default("FrstOpngBal")

	@FrstOpngBal.deleter
	def FrstOpngBal(self):
		del self._FrstOpngBal
		self._FrstOpngBal = None

	@property
	def IntrmyOpngBal(self):
		return self._IntrmyOpngBal

	@IntrmyOpngBal.setter
	def IntrmyOpngBal(self, value):
		self._IntrmyOpngBal = value if type(value) != base_types.auto else self.make_default("IntrmyOpngBal")

	@IntrmyOpngBal.deleter
	def IntrmyOpngBal(self):
		del self._IntrmyOpngBal
		self._IntrmyOpngBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstOpngBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrmyOpngBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
	))

