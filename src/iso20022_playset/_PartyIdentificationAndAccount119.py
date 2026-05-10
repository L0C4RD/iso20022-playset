from . import base_types
from ._AccountIdentification30 import AccountIdentification30
from ._PartyIdentification90 import PartyIdentification90

class PartyIdentificationAndAccount119(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_PtyId"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification30, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification90, min=1, max=None, mutex_group=None, array=True),
	))

