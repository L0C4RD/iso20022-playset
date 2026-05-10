from . import base_types
from .LEIIdentifier import LEIIdentifier
from .SupervisingAuthorityIdentification1Choice import SupervisingAuthorityIdentification1Choice

class SupervisingAuthorityIdentification1(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_Id"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SupervisingAuthorityIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
	))

