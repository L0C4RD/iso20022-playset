# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import MarketInfrastructureIdentification1Choice

class SystemIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_MktInfrstrctrId"]
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
	def MktInfrstrctrId(self):
		return self._MktInfrstrctrId

	@MktInfrstrctrId.setter
	def MktInfrstrctrId(self, value):
		self._MktInfrstrctrId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrId', MarketInfrastructureIdentification1Choice, False)

	@MktInfrstrctrId.deleter
	def MktInfrstrctrId(self):
		del self._MktInfrstrctrId
		self._MktInfrstrctrId = base_types.UninitialisedField(self, 'MktInfrstrctrId', MarketInfrastructureIdentification1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktInfrstrctrId', type=MarketInfrastructureIdentification1Choice, min=0, max=1, mutex_group=1, array=False),
	))