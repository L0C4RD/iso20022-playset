from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._PartyIdentification182Choice import PartyIdentification182Choice

class PartyIdentification220(base_types._BaseFieldType):

	__slots__ = ["_Id", "_LglNttyIdr"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if type(value) != base_types.auto else self.make_default("LglNttyIdr")

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification182Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

