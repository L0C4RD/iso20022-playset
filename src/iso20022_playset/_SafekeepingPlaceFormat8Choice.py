from . import base_types
from ._CountryCode import CountryCode
from ._GenericIdentification78 import GenericIdentification78
from ._SafekeepingPlaceTypeAndAnyBICIdentifier1 import SafekeepingPlaceTypeAndAnyBICIdentifier1
from ._SafekeepingPlaceTypeAndText6 import SafekeepingPlaceTypeAndText6

class SafekeepingPlaceFormat8Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_Id", "_Prtry", "_TpAndId"]
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
		base_types.FieldEntry(name='Id', type=SafekeepingPlaceTypeAndText6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification78, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TpAndId', type=SafekeepingPlaceTypeAndAnyBICIdentifier1, min=0, max=1, mutex_group=1, array=False),
	))

