# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AirportName1Choice
from . import Max35Text

class TransportByAir2(base_types._BaseFieldType):

	__slots__ = ["_AirCrrierNm", "_DprtureAirprt", "_DstnAirprt"]
	@property
	def AirCrrierNm(self):
		return self._AirCrrierNm

	@AirCrrierNm.setter
	def AirCrrierNm(self, value):
		self._AirCrrierNm = value if value is not None else base_types.UninitialisedField(self, 'AirCrrierNm', Max35Text, False)

	@AirCrrierNm.deleter
	def AirCrrierNm(self):
		del self._AirCrrierNm
		self._AirCrrierNm = base_types.UninitialisedField(self, 'AirCrrierNm', Max35Text, False)

	@property
	def DprtureAirprt(self):
		return self._DprtureAirprt

	@DprtureAirprt.setter
	def DprtureAirprt(self, value):
		self._DprtureAirprt = value if value is not None else base_types.UninitialisedField(self, 'DprtureAirprt', AirportName1Choice, False)

	@DprtureAirprt.deleter
	def DprtureAirprt(self):
		del self._DprtureAirprt
		self._DprtureAirprt = base_types.UninitialisedField(self, 'DprtureAirprt', AirportName1Choice, False)

	@property
	def DstnAirprt(self):
		return self._DstnAirprt

	@DstnAirprt.setter
	def DstnAirprt(self, value):
		self._DstnAirprt = value if value is not None else base_types.UninitialisedField(self, 'DstnAirprt', AirportName1Choice, False)

	@DstnAirprt.deleter
	def DstnAirprt(self):
		del self._DstnAirprt
		self._DstnAirprt = base_types.UninitialisedField(self, 'DstnAirprt', AirportName1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AirCrrierNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DprtureAirprt', type=AirportName1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAirprt', type=AirportName1Choice, min=1, max=1, mutex_group=None, array=False),
	))