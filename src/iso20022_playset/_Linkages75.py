from . import base_types
from ._Max35Text import Max35Text

class Linkages75(base_types._BaseFieldType):

	__slots__ = ["_SctiesSttlmTxId"]
	@property
	def SctiesSttlmTxId(self):
		return self._SctiesSttlmTxId

	@SctiesSttlmTxId.setter
	def SctiesSttlmTxId(self, value):
		self._SctiesSttlmTxId = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxId")

	@SctiesSttlmTxId.deleter
	def SctiesSttlmTxId(self):
		del self._SctiesSttlmTxId
		self._SctiesSttlmTxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesSttlmTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

