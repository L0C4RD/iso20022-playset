# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AirportDescription1
from . import Max6Text

class AirportName1Choice(base_types._BaseFieldType):

	__slots__ = ["_AirprtCd", "_OthrAirprtDesc"]
	@property
	def AirprtCd(self):
		return self._AirprtCd

	@AirprtCd.setter
	def AirprtCd(self, value):
		self._AirprtCd = value if value is not None else base_types.UninitialisedField(self, 'AirprtCd', Max6Text, False)

	@AirprtCd.deleter
	def AirprtCd(self):
		del self._AirprtCd
		self._AirprtCd = base_types.UninitialisedField(self, 'AirprtCd', Max6Text, False)

	@property
	def OthrAirprtDesc(self):
		return self._OthrAirprtDesc

	@OthrAirprtDesc.setter
	def OthrAirprtDesc(self, value):
		self._OthrAirprtDesc = value if value is not None else base_types.UninitialisedField(self, 'OthrAirprtDesc', AirportDescription1, False)

	@OthrAirprtDesc.deleter
	def OthrAirprtDesc(self):
		del self._OthrAirprtDesc
		self._OthrAirprtDesc = base_types.UninitialisedField(self, 'OthrAirprtDesc', AirportDescription1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AirprtCd', type=Max6Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrAirprtDesc', type=AirportDescription1, min=0, max=1, mutex_group=1, array=False),
	))