from . import base_types
from .AccountIdentification26 import AccountIdentification26
from .PartyIdentification62 import PartyIdentification62

class PartyIdentificationAndAccount97(base_types._BaseFieldType):

	__slots__ = ["_PtyId", "_AcctId"]
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
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyId', type=PartyIdentification62, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountIdentification26, min=0, max=1, mutex_group=None, array=False),
	))

