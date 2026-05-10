from . import base_types
from .FinancialPartyClassification2 import FinancialPartyClassification2
from .FinancialPartyClassification1 import FinancialPartyClassification1

class CounterpartyTradeNature7Choice(base_types._BaseFieldType):

	__slots__ = ["_NFI", "_FI"]
	@property
	def NFI(self):
		return self._NFI

	@NFI.setter
	def NFI(self, value):
		self._NFI = value if type(value) != base_types.auto else self.make_default("NFI")

	@NFI.deleter
	def NFI(self):
		del self._NFI
		self._NFI = None

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if type(value) != base_types.auto else self.make_default("FI")

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NFI', type=FinancialPartyClassification2, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='FI', type=FinancialPartyClassification1, min=0, max=1, mutex_group=1, array=False),
	))

