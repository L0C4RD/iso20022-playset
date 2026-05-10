from . import base_types
from ._PersonName2 import PersonName2
from ._PartyIdentification198Choice import PartyIdentification198Choice

class PartyIdentification201(base_types._BaseFieldType):

	__slots__ = ["_Id", "_NmAndAdr"]
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
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != base_types.auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification198Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=PersonName2, min=0, max=1, mutex_group=None, array=False),
	))

