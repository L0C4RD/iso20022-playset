# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._CountryCode import CountryCode
from ._Max35Text import Max35Text

class AdditionalParameters1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Ctry", "_GeoArea"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

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
	def GeoArea(self):
		return self._GeoArea

	@GeoArea.setter
	def GeoArea(self, value):
		self._GeoArea = value if type(value) != base_types.auto else self.make_default("GeoArea")

	@GeoArea.deleter
	def GeoArea(self):
		del self._GeoArea
		self._GeoArea = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeoArea', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))