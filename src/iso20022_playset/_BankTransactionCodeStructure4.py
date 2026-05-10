from . import base_types
from .BankTransactionCodeStructure5 import BankTransactionCodeStructure5
from .ProprietaryBankTransactionCodeStructure1 import ProprietaryBankTransactionCodeStructure1

class BankTransactionCodeStructure4(base_types._BaseFieldType):

	__slots__ = ["_Domn", "_Prtry"]
	@property
	def Domn(self):
		return self._Domn

	@Domn.setter
	def Domn(self, value):
		self._Domn = value if type(value) != base_types.auto else self.make_default("Domn")

	@Domn.deleter
	def Domn(self):
		del self._Domn
		self._Domn = None

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
		base_types.FieldEntry(name='Domn', type=BankTransactionCodeStructure5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryBankTransactionCodeStructure1, min=0, max=1, mutex_group=None, array=False),
	))

