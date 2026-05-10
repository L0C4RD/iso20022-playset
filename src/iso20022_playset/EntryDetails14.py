from . import base_types
from .BatchInformation2 import BatchInformation2
from .EntryTransaction15 import EntryTransaction15

class EntryDetails14(base_types._BaseFieldType):

	__slots__ = ["_TxDtls", "_Btch"]
	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def Btch(self):
		return self._Btch

	@Btch.setter
	def Btch(self, value):
		self._Btch = value if type(value) != base_types.auto else self.make_default("Btch")

	@Btch.deleter
	def Btch(self):
		del self._Btch
		self._Btch = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxDtls', type=EntryTransaction15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Btch', type=BatchInformation2, min=0, max=1, mutex_group=None, array=False),
	))

