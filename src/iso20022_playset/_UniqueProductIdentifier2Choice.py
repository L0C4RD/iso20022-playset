from . import base_types
from ._GenericIdentification185 import GenericIdentification185
from ._Max52Text import Max52Text

class UniqueProductIdentifier2Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Id"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
		base_types.FieldEntry(name='Prtry', type=GenericIdentification185, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
	))

