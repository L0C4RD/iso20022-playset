from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._BranchAndFinancialInstitutionIdentification6 import BranchAndFinancialInstitutionIdentification6

class Charges7(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Agt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != base_types.auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification6, min=1, max=1, mutex_group=None, array=False),
	))

