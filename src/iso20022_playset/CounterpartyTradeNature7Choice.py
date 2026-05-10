import base_types
import FinancialPartyClassification1
import FinancialPartyClassification2

class CounterpartyTradeNature7Choice(base_types._BaseFieldType):

	__slots__ = ["_FI", "_NFI"]
	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if type(value) != auto else self.make_default("FI")

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = None

	@property
	def NFI(self):
		return self._NFI

	@NFI.setter
	def NFI(self, value):
		self._NFI = value if type(value) != auto else self.make_default("NFI")

	@NFI.deleter
	def NFI(self):
		del self._NFI
		self._NFI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FI', type=FinancialPartyClassification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NFI', type=FinancialPartyClassification2, min=1, max=None, mutex_group=1, array=True),
	))

