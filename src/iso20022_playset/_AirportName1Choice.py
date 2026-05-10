from . import base_types
from ._AirportDescription1 import AirportDescription1
from ._Max6Text import Max6Text

class AirportName1Choice(base_types._BaseFieldType):

	__slots__ = ["_AirprtCd", "_OthrAirprtDesc"]
	@property
	def AirprtCd(self):
		return self._AirprtCd

	@AirprtCd.setter
	def AirprtCd(self, value):
		self._AirprtCd = value if type(value) != base_types.auto else self.make_default("AirprtCd")

	@AirprtCd.deleter
	def AirprtCd(self):
		del self._AirprtCd
		self._AirprtCd = None

	@property
	def OthrAirprtDesc(self):
		return self._OthrAirprtDesc

	@OthrAirprtDesc.setter
	def OthrAirprtDesc(self, value):
		self._OthrAirprtDesc = value if type(value) != base_types.auto else self.make_default("OthrAirprtDesc")

	@OthrAirprtDesc.deleter
	def OthrAirprtDesc(self):
		del self._OthrAirprtDesc
		self._OthrAirprtDesc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AirprtCd', type=Max6Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrAirprtDesc', type=AirportDescription1, min=0, max=1, mutex_group=1, array=False),
	))

