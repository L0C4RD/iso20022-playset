from . import base_types
from ._SettlementFailsParticipant1 import SettlementFailsParticipant1

class SettlementFailsParticipantRange1(base_types._BaseFieldType):

	__slots__ = ["_HghstInVal", "_HghstInVol"]
	@property
	def HghstInVal(self):
		return self._HghstInVal

	@HghstInVal.setter
	def HghstInVal(self, value):
		self._HghstInVal = value if type(value) != base_types.auto else self.make_default("HghstInVal")

	@HghstInVal.deleter
	def HghstInVal(self):
		del self._HghstInVal
		self._HghstInVal = None

	@property
	def HghstInVol(self):
		return self._HghstInVol

	@HghstInVol.setter
	def HghstInVol(self, value):
		self._HghstInVol = value if type(value) != base_types.auto else self.make_default("HghstInVol")

	@HghstInVol.deleter
	def HghstInVol(self):
		del self._HghstInVol
		self._HghstInVol = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghstInVal', type=SettlementFailsParticipant1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HghstInVol', type=SettlementFailsParticipant1, min=1, max=None, mutex_group=None, array=True),
	))

