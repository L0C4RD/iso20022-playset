# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AirportName1Choice import AirportName1Choice
from ._Max35Text import Max35Text

class TransportByAir2(base_types._BaseFieldType):

	__slots__ = ["_AirCrrierNm", "_DprtureAirprt", "_DstnAirprt"]
	@property
	def AirCrrierNm(self):
		return self._AirCrrierNm

	@AirCrrierNm.setter
	def AirCrrierNm(self, value):
		self._AirCrrierNm = value if type(value) != base_types.auto else self.make_default("AirCrrierNm")

	@AirCrrierNm.deleter
	def AirCrrierNm(self):
		del self._AirCrrierNm
		self._AirCrrierNm = None

	@property
	def DprtureAirprt(self):
		return self._DprtureAirprt

	@DprtureAirprt.setter
	def DprtureAirprt(self, value):
		self._DprtureAirprt = value if type(value) != base_types.auto else self.make_default("DprtureAirprt")

	@DprtureAirprt.deleter
	def DprtureAirprt(self):
		del self._DprtureAirprt
		self._DprtureAirprt = None

	@property
	def DstnAirprt(self):
		return self._DstnAirprt

	@DstnAirprt.setter
	def DstnAirprt(self, value):
		self._DstnAirprt = value if type(value) != base_types.auto else self.make_default("DstnAirprt")

	@DstnAirprt.deleter
	def DstnAirprt(self):
		del self._DstnAirprt
		self._DstnAirprt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AirCrrierNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DprtureAirprt', type=AirportName1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAirprt', type=AirportName1Choice, min=1, max=1, mutex_group=None, array=False),
	))