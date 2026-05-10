from . import base_types
from ._GenericIdentification89 import GenericIdentification89
from ._CountryCode import CountryCode
from ._DTI2024Identifier import DTI2024Identifier
from ._SafekeepingPlaceTypeAndText9 import SafekeepingPlaceTypeAndText9
from ._SafekeepingPlaceTypeAndIdentification1 import SafekeepingPlaceTypeAndIdentification1

class SafekeepingPlaceFormat45Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_Prtry", "_TpAndId", "_Id", "_DgtlLdgrId"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def DgtlLdgrId(self):
		return self._DgtlLdgrId

	@DgtlLdgrId.setter
	def DgtlLdgrId(self, value):
		self._DgtlLdgrId = value if type(value) != base_types.auto else self.make_default("DgtlLdgrId")

	@DgtlLdgrId.deleter
	def DgtlLdgrId(self):
		del self._DgtlLdgrId
		self._DgtlLdgrId = None

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
	def TpAndId(self):
		return self._TpAndId

	@TpAndId.setter
	def TpAndId(self, value):
		self._TpAndId = value if type(value) != base_types.auto else self.make_default("TpAndId")

	@TpAndId.deleter
	def TpAndId(self):
		del self._TpAndId
		self._TpAndId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DgtlLdgrId', type=DTI2024Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=SafekeepingPlaceTypeAndText9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification89, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TpAndId', type=SafekeepingPlaceTypeAndIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

