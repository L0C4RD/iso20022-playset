from . import base_types
from .SettlementTypeAndIdentification25 import SettlementTypeAndIdentification25
from .SignedQuantityFormat10 import SignedQuantityFormat10

class PendingBalance7(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_PdgTxs"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def PdgTxs(self):
		return self._PdgTxs

	@PdgTxs.setter
	def PdgTxs(self, value):
		self._PdgTxs = value if type(value) != base_types.auto else self.make_default("PdgTxs")

	@PdgTxs.deleter
	def PdgTxs(self):
		del self._PdgTxs
		self._PdgTxs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgTxs', type=SettlementTypeAndIdentification25, min=0, max=None, mutex_group=None, array=True),
	))

