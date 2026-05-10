from . import base_types
from .ProcessingPosition23Choice import ProcessingPosition23Choice
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text

class Linkages50(base_types._BaseFieldType):

	__slots__ = ["_PrcgPos", "_SctiesSttlmTxId"]
	@property
	def PrcgPos(self):
		return self._PrcgPos

	@PrcgPos.setter
	def PrcgPos(self, value):
		self._PrcgPos = value if type(value) != base_types.auto else self.make_default("PrcgPos")

	@PrcgPos.deleter
	def PrcgPos(self):
		del self._PrcgPos
		self._PrcgPos = None

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
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmTxId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
	))

