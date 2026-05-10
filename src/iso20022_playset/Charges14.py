from . import base_types
from .CashAccount40 import CashAccount40
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .ChargeType3Choice import ChargeType3Choice
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8

class Charges14(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_AgtAcct", "_Amt", "_Agt"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def AgtAcct(self):
		return self._AgtAcct

	@AgtAcct.setter
	def AgtAcct(self, value):
		self._AgtAcct = value if type(value) != auto else self.make_default("AgtAcct")

	@AgtAcct.deleter
	def AgtAcct(self):
		del self._AgtAcct
		self._AgtAcct = None

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

	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=ChargeType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

