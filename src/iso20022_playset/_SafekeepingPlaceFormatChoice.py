# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import GenericIdentification5
from . import SafekeepingPlaceAsCodeAndPartyIdentification

class SafekeepingPlaceFormatChoice(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdAsCtry", "_IdAsDSS"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SafekeepingPlaceAsCodeAndPartyIdentification, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SafekeepingPlaceAsCodeAndPartyIdentification, False)

	@property
	def IdAsCtry(self):
		return self._IdAsCtry

	@IdAsCtry.setter
	def IdAsCtry(self, value):
		self._IdAsCtry = value if value is not None else base_types.UninitialisedField(self, 'IdAsCtry', CountryCode, False)

	@IdAsCtry.deleter
	def IdAsCtry(self):
		del self._IdAsCtry
		self._IdAsCtry = base_types.UninitialisedField(self, 'IdAsCtry', CountryCode, False)

	@property
	def IdAsDSS(self):
		return self._IdAsDSS

	@IdAsDSS.setter
	def IdAsDSS(self, value):
		self._IdAsDSS = value if value is not None else base_types.UninitialisedField(self, 'IdAsDSS', GenericIdentification5, False)

	@IdAsDSS.deleter
	def IdAsDSS(self):
		del self._IdAsDSS
		self._IdAsDSS = base_types.UninitialisedField(self, 'IdAsDSS', GenericIdentification5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=SafekeepingPlaceAsCodeAndPartyIdentification, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdAsCtry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdAsDSS', type=GenericIdentification5, min=0, max=1, mutex_group=1, array=False),
	))