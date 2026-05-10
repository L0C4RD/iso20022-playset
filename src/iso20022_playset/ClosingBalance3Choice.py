from . import base_types
import FinancialInstrumentQuantity1

class ClosingBalance3Choice(base_types._BaseFieldType):

	__slots__ = ["_FnlClsgBal", "_IntrmyClsgBal"]
	@property
	def FnlClsgBal(self):
		return self._FnlClsgBal

	@FnlClsgBal.setter
	def FnlClsgBal(self, value):
		self._FnlClsgBal = value if type(value) != auto else self.make_default("FnlClsgBal")

	@FnlClsgBal.deleter
	def FnlClsgBal(self):
		del self._FnlClsgBal
		self._FnlClsgBal = None

	@property
	def IntrmyClsgBal(self):
		return self._IntrmyClsgBal

	@IntrmyClsgBal.setter
	def IntrmyClsgBal(self, value):
		self._IntrmyClsgBal = value if type(value) != auto else self.make_default("IntrmyClsgBal")

	@IntrmyClsgBal.deleter
	def IntrmyClsgBal(self):
		del self._IntrmyClsgBal
		self._IntrmyClsgBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FnlClsgBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrmyClsgBal', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
	))

