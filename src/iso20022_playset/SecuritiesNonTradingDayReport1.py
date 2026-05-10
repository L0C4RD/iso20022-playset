import base_types
import SecuritiesNonTradingDay1
import TradingVenueIdentification1Choice

class SecuritiesNonTradingDayReport1(base_types._BaseFieldType):

	__slots__ = ["_NonWorkgDay", "_Id"]
	@property
	def NonWorkgDay(self):
		return self._NonWorkgDay

	@NonWorkgDay.setter
	def NonWorkgDay(self, value):
		self._NonWorkgDay = value if type(value) != auto else self.make_default("NonWorkgDay")

	@NonWorkgDay.deleter
	def NonWorkgDay(self):
		del self._NonWorkgDay
		self._NonWorkgDay = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonWorkgDay', type=SecuritiesNonTradingDay1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=TradingVenueIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
	))

