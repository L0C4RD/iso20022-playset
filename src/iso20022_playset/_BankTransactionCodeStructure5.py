from . import base_types
from ._BankTransactionCodeStructure6 import BankTransactionCodeStructure6
from ._ExternalBankTransactionDomain1Code import ExternalBankTransactionDomain1Code

class BankTransactionCodeStructure5(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Fmly"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Fmly(self):
		return self._Fmly

	@Fmly.setter
	def Fmly(self, value):
		self._Fmly = value if type(value) != base_types.auto else self.make_default("Fmly")

	@Fmly.deleter
	def Fmly(self):
		del self._Fmly
		self._Fmly = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=ExternalBankTransactionDomain1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fmly', type=BankTransactionCodeStructure6, min=1, max=1, mutex_group=None, array=False),
	))

