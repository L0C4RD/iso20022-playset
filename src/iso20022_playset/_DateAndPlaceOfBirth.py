# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISODate
from . import Max35Text

class DateAndPlaceOfBirth(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_CityOfBirth", "_CtryOfBirth", "_PrvcOfBirth"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if value is not None else base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@property
	def CityOfBirth(self):
		return self._CityOfBirth

	@CityOfBirth.setter
	def CityOfBirth(self, value):
		self._CityOfBirth = value if value is not None else base_types.UninitialisedField(self, 'CityOfBirth', Max35Text, False)

	@CityOfBirth.deleter
	def CityOfBirth(self):
		del self._CityOfBirth
		self._CityOfBirth = base_types.UninitialisedField(self, 'CityOfBirth', Max35Text, False)

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if value is not None else base_types.UninitialisedField(self, 'CtryOfBirth', CountryCode, False)

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = base_types.UninitialisedField(self, 'CtryOfBirth', CountryCode, False)

	@property
	def PrvcOfBirth(self):
		return self._PrvcOfBirth

	@PrvcOfBirth.setter
	def PrvcOfBirth(self, value):
		self._PrvcOfBirth = value if value is not None else base_types.UninitialisedField(self, 'PrvcOfBirth', Max35Text, False)

	@PrvcOfBirth.deleter
	def PrvcOfBirth(self):
		del self._PrvcOfBirth
		self._PrvcOfBirth = base_types.UninitialisedField(self, 'PrvcOfBirth', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CityOfBirth', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvcOfBirth', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))