# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesNonTradingDay1
from . import TradingVenueIdentification1Choice

class SecuritiesNonTradingDayReport1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_NonWorkgDay"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', TradingVenueIdentification1Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', TradingVenueIdentification1Choice, False)

	@property
	def NonWorkgDay(self):
		return self._NonWorkgDay

	@NonWorkgDay.setter
	def NonWorkgDay(self, value):
		self._NonWorkgDay = value if value is not None else base_types.UninitialisedField(self, 'NonWorkgDay', SecuritiesNonTradingDay1, True)

	@NonWorkgDay.deleter
	def NonWorkgDay(self):
		del self._NonWorkgDay
		self._NonWorkgDay = base_types.UninitialisedField(self, 'NonWorkgDay', SecuritiesNonTradingDay1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=TradingVenueIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonWorkgDay', type=SecuritiesNonTradingDay1, min=1, max=None, mutex_group=None, array=True),
	))