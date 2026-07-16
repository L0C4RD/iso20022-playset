# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AirportName1Choice
from . import CountryCode
from . import Max70Text

class TransportByAir5(base_types._BaseFieldType):

	__slots__ = ["_AirCrrierCtry", "_AirCrrierNm", "_CrrierAgtCtry", "_CrrierAgtNm", "_DprtureAirprt", "_DstnAirprt"]
	@property
	def AirCrrierCtry(self):
		return self._AirCrrierCtry

	@AirCrrierCtry.setter
	def AirCrrierCtry(self, value):
		self._AirCrrierCtry = value if value is not None else base_types.UninitialisedField(self, 'AirCrrierCtry', CountryCode, False)

	@AirCrrierCtry.deleter
	def AirCrrierCtry(self):
		del self._AirCrrierCtry
		self._AirCrrierCtry = base_types.UninitialisedField(self, 'AirCrrierCtry', CountryCode, False)

	@property
	def AirCrrierNm(self):
		return self._AirCrrierNm

	@AirCrrierNm.setter
	def AirCrrierNm(self, value):
		self._AirCrrierNm = value if value is not None else base_types.UninitialisedField(self, 'AirCrrierNm', Max70Text, False)

	@AirCrrierNm.deleter
	def AirCrrierNm(self):
		del self._AirCrrierNm
		self._AirCrrierNm = base_types.UninitialisedField(self, 'AirCrrierNm', Max70Text, False)

	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = base_types.UninitialisedField(self, 'CrrierAgtCtry', CountryCode, False)

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if value is not None else base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = base_types.UninitialisedField(self, 'CrrierAgtNm', Max70Text, False)

	@property
	def DprtureAirprt(self):
		return self._DprtureAirprt

	@DprtureAirprt.setter
	def DprtureAirprt(self, value):
		self._DprtureAirprt = value if value is not None else base_types.UninitialisedField(self, 'DprtureAirprt', AirportName1Choice, True)

	@DprtureAirprt.deleter
	def DprtureAirprt(self):
		del self._DprtureAirprt
		self._DprtureAirprt = base_types.UninitialisedField(self, 'DprtureAirprt', AirportName1Choice, True)

	@property
	def DstnAirprt(self):
		return self._DstnAirprt

	@DstnAirprt.setter
	def DstnAirprt(self, value):
		self._DstnAirprt = value if value is not None else base_types.UninitialisedField(self, 'DstnAirprt', AirportName1Choice, True)

	@DstnAirprt.deleter
	def DstnAirprt(self):
		del self._DstnAirprt
		self._DstnAirprt = base_types.UninitialisedField(self, 'DstnAirprt', AirportName1Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AirCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AirCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DprtureAirprt', type=AirportName1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DstnAirprt', type=AirportName1Choice, min=1, max=None, mutex_group=None, array=True),
	))