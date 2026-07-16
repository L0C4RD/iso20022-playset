# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import GenericIdentification78
from . import SafekeepingPlaceTypeAndIdentification1
from . import SafekeepingPlaceTypeAndText6

class SafekeepingPlaceFormat28Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_Id", "_Prtry", "_TpAndId"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SafekeepingPlaceTypeAndText6, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SafekeepingPlaceTypeAndText6, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification78, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification78, False)

	@property
	def TpAndId(self):
		return self._TpAndId

	@TpAndId.setter
	def TpAndId(self, value):
		self._TpAndId = value if value is not None else base_types.UninitialisedField(self, 'TpAndId', SafekeepingPlaceTypeAndIdentification1, False)

	@TpAndId.deleter
	def TpAndId(self):
		del self._TpAndId
		self._TpAndId = base_types.UninitialisedField(self, 'TpAndId', SafekeepingPlaceTypeAndIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=SafekeepingPlaceTypeAndText6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification78, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TpAndId', type=SafekeepingPlaceTypeAndIdentification1, min=0, max=1, mutex_group=1, array=False),
	))