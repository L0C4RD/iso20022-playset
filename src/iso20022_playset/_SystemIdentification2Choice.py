from . import base_types
from .MarketInfrastructureIdentification1Choice import MarketInfrastructureIdentification1Choice
from .CountryCode import CountryCode

class SystemIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_MktInfrstrctrId", "_Ctry"]
	@property
	def MktInfrstrctrId(self):
		return self._MktInfrstrctrId

	@MktInfrstrctrId.setter
	def MktInfrstrctrId(self, value):
		self._MktInfrstrctrId = value if type(value) != base_types.auto else self.make_default("MktInfrstrctrId")

	@MktInfrstrctrId.deleter
	def MktInfrstrctrId(self):
		del self._MktInfrstrctrId
		self._MktInfrstrctrId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktInfrstrctrId', type=MarketInfrastructureIdentification1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
	))

