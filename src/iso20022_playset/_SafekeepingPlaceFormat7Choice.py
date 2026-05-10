from . import base_types
from ._SafekeepingPlaceTypeAndText1 import SafekeepingPlaceTypeAndText1
from ._GenericIdentification58 import GenericIdentification58
from ._CountryCode import CountryCode
from ._SafekeepingPlaceTypeAndAnyBICIdentifier1 import SafekeepingPlaceTypeAndAnyBICIdentifier1

class SafekeepingPlaceFormat7Choice(base_types._BaseFieldType):

	__slots__ = ["_TpAndId", "_Ctry", "_Prtry", "_Id"]
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
		base_types.FieldEntry(name='TpAndId', type=SafekeepingPlaceTypeAndAnyBICIdentifier1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification58, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=SafekeepingPlaceTypeAndText1, min=0, max=1, mutex_group=1, array=False),
	))

