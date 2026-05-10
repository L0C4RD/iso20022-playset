from . import base_types
from .CashAccount43 import CashAccount43
from .CashEntry2 import CashEntry2

class CashAccountAndEntry5(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Ntry"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def Ntry(self):
		return self._Ntry

	@Ntry.setter
	def Ntry(self, value):
		self._Ntry = value if type(value) != base_types.auto else self.make_default("Ntry")

	@Ntry.deleter
	def Ntry(self):
		del self._Ntry
		self._Ntry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntry', type=CashEntry2, min=0, max=1, mutex_group=None, array=False),
	))

