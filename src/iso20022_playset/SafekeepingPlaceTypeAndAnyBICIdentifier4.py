from . import base_types
from .AnyBICDec2014Identifier import AnyBICDec2014Identifier
from .SafekeepingPlace1Code import SafekeepingPlace1Code

class SafekeepingPlaceTypeAndAnyBICIdentifier4(base_types._BaseFieldType):

	__slots__ = ["_Id", "_SfkpgPlcTp"]
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

	@property
	def SfkpgPlcTp(self):
		return self._SfkpgPlcTp

	@SfkpgPlcTp.setter
	def SfkpgPlcTp(self, value):
		self._SfkpgPlcTp = value if type(value) != auto else self.make_default("SfkpgPlcTp")

	@SfkpgPlcTp.deleter
	def SfkpgPlcTp(self):
		del self._SfkpgPlcTp
		self._SfkpgPlcTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=AnyBICDec2014Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlcTp', type=SafekeepingPlace1Code, min=1, max=1, mutex_group=None, array=False),
	))

