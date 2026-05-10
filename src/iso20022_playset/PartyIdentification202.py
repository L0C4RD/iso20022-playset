from . import base_types
from .NaturalPersonIdentification1 import NaturalPersonIdentification1
from .PersonName1 import PersonName1

class PartyIdentification202(base_types._BaseFieldType):

	__slots__ = ["_NmAndAdr", "_Id"]
	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

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
		base_types.FieldEntry(name='NmAndAdr', type=PersonName1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=NaturalPersonIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

