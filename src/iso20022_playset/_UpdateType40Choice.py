from . import base_types
from ._SecuritiesSettlementTransactionDetails59 import SecuritiesSettlementTransactionDetails59
from ._SecuritiesSettlementTransactionDetails60 import SecuritiesSettlementTransactionDetails60
from ._SecuritiesSettlementTransactionDetails61 import SecuritiesSettlementTransactionDetails61

class UpdateType40Choice(base_types._BaseFieldType):

	__slots__ = ["_Addtn", "_Deltn", "_Mod"]
	@property
	def Addtn(self):
		return self._Addtn

	@Addtn.setter
	def Addtn(self, value):
		self._Addtn = value if type(value) != base_types.auto else self.make_default("Addtn")

	@Addtn.deleter
	def Addtn(self):
		del self._Addtn
		self._Addtn = None

	@property
	def Deltn(self):
		return self._Deltn

	@Deltn.setter
	def Deltn(self, value):
		self._Deltn = value if type(value) != base_types.auto else self.make_default("Deltn")

	@Deltn.deleter
	def Deltn(self):
		del self._Deltn
		self._Deltn = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Addtn', type=SecuritiesSettlementTransactionDetails59, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Deltn', type=SecuritiesSettlementTransactionDetails60, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=SecuritiesSettlementTransactionDetails61, min=0, max=1, mutex_group=1, array=False),
	))

