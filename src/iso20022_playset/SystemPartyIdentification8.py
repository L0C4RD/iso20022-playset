import base_types
import PartyIdentification136

class SystemPartyIdentification8(base_types._BaseFieldType):

	__slots__ = ["_RspnsblPtyId", "_Id"]
	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if type(value) != auto else self.make_default("RspnsblPtyId")

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
	))

