# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import CountryCode
from . import Max35Text

class AdditionalParameters1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Ctry", "_GeoArea"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

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
	def GeoArea(self):
		return self._GeoArea

	@GeoArea.setter
	def GeoArea(self, value):
		self._GeoArea = value if value is not None else base_types.UninitialisedField(self, 'GeoArea', Max35Text, False)

	@GeoArea.deleter
	def GeoArea(self):
		del self._GeoArea
		self._GeoArea = base_types.UninitialisedField(self, 'GeoArea', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeoArea', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))