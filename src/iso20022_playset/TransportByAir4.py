from . import base_types
from .CountryCode import CountryCode
from .Max35Text import Max35Text
from .Max70Text import Max70Text
from .AirportName1Choice import AirportName1Choice

class TransportByAir4(base_types._BaseFieldType):

	__slots__ = ["_FlghtNb", "_AirCrrierCtry", "_DstnAirprt", "_CrrierAgtCtry", "_AirCrrierNm", "_CrrierAgtNm", "_DprtureAirprt"]
	@property
	def FlghtNb(self):
		return self._FlghtNb

	@FlghtNb.setter
	def FlghtNb(self, value):
		self._FlghtNb = value if type(value) != auto else self.make_default("FlghtNb")

	@FlghtNb.deleter
	def FlghtNb(self):
		del self._FlghtNb
		self._FlghtNb = None

	@property
	def AirCrrierCtry(self):
		return self._AirCrrierCtry

	@AirCrrierCtry.setter
	def AirCrrierCtry(self, value):
		self._AirCrrierCtry = value if type(value) != auto else self.make_default("AirCrrierCtry")

	@AirCrrierCtry.deleter
	def AirCrrierCtry(self):
		del self._AirCrrierCtry
		self._AirCrrierCtry = None

	@property
	def DstnAirprt(self):
		return self._DstnAirprt

	@DstnAirprt.setter
	def DstnAirprt(self, value):
		self._DstnAirprt = value if type(value) != auto else self.make_default("DstnAirprt")

	@DstnAirprt.deleter
	def DstnAirprt(self):
		del self._DstnAirprt
		self._DstnAirprt = None

	@property
	def CrrierAgtCtry(self):
		return self._CrrierAgtCtry

	@CrrierAgtCtry.setter
	def CrrierAgtCtry(self, value):
		self._CrrierAgtCtry = value if type(value) != auto else self.make_default("CrrierAgtCtry")

	@CrrierAgtCtry.deleter
	def CrrierAgtCtry(self):
		del self._CrrierAgtCtry
		self._CrrierAgtCtry = None

	@property
	def AirCrrierNm(self):
		return self._AirCrrierNm

	@AirCrrierNm.setter
	def AirCrrierNm(self, value):
		self._AirCrrierNm = value if type(value) != auto else self.make_default("AirCrrierNm")

	@AirCrrierNm.deleter
	def AirCrrierNm(self):
		del self._AirCrrierNm
		self._AirCrrierNm = None

	@property
	def CrrierAgtNm(self):
		return self._CrrierAgtNm

	@CrrierAgtNm.setter
	def CrrierAgtNm(self, value):
		self._CrrierAgtNm = value if type(value) != auto else self.make_default("CrrierAgtNm")

	@CrrierAgtNm.deleter
	def CrrierAgtNm(self):
		del self._CrrierAgtNm
		self._CrrierAgtNm = None

	@property
	def DprtureAirprt(self):
		return self._DprtureAirprt

	@DprtureAirprt.setter
	def DprtureAirprt(self, value):
		self._DprtureAirprt = value if type(value) != auto else self.make_default("DprtureAirprt")

	@DprtureAirprt.deleter
	def DprtureAirprt(self):
		del self._DprtureAirprt
		self._DprtureAirprt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FlghtNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AirCrrierCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAirprt', type=AirportName1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AirCrrierNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrrierAgtNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DprtureAirprt', type=AirportName1Choice, min=1, max=1, mutex_group=None, array=False),
	))

