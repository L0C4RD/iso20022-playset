from . import base_types
from ._PartyOrBusinessError4Choice import PartyOrBusinessError4Choice
from ._SystemPartyIdentification8 import SystemPartyIdentification8

class PartyReport4(base_types._BaseFieldType):

	__slots__ = ["_PtyId", "_PtyOrErr"]
	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def PtyOrErr(self):
		return self._PtyOrErr

	@PtyOrErr.setter
	def PtyOrErr(self, value):
		self._PtyOrErr = value if type(value) != base_types.auto else self.make_default("PtyOrErr")

	@PtyOrErr.deleter
	def PtyOrErr(self):
		del self._PtyOrErr
		self._PtyOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyOrErr', type=PartyOrBusinessError4Choice, min=1, max=1, mutex_group=None, array=False),
	))

