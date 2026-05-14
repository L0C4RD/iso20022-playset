from . import base_types
from ._ProcessingStatus100Choice import ProcessingStatus100Choice
from ._SettlementStatus34Choice import SettlementStatus34Choice

class PendingStatusAndReason4(base_types._BaseFieldType):

	__slots__ = ["_PrcgSts", "_SttlmSts"]
	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != base_types.auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus100Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus34Choice, min=0, max=None, mutex_group=None, array=True),
	))

