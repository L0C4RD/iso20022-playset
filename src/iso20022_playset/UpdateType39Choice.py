from . import base_types
from .SecuritiesSettlementTransactionDetails58 import SecuritiesSettlementTransactionDetails58
from .SecuritiesSettlementTransactionDetails57 import SecuritiesSettlementTransactionDetails57
from .SecuritiesSettlementTransactionDetails56 import SecuritiesSettlementTransactionDetails56

class UpdateType39Choice(base_types._BaseFieldType):

	__slots__ = ["_Deltn", "_Addtn", "_Mod"]
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
		base_types.FieldEntry(name='Deltn', type=SecuritiesSettlementTransactionDetails58, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Addtn', type=SecuritiesSettlementTransactionDetails56, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=SecuritiesSettlementTransactionDetails57, min=0, max=1, mutex_group=1, array=False),
	))

