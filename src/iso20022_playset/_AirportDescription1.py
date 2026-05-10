from . import base_types
from ._Max35Text import Max35Text

class AirportDescription1(base_types._BaseFieldType):

	__slots__ = ["_AirprtNm", "_Twn"]
	@property
	def AirprtNm(self):
		return self._AirprtNm

	@AirprtNm.setter
	def AirprtNm(self, value):
		self._AirprtNm = value if type(value) != base_types.auto else self.make_default("AirprtNm")

	@AirprtNm.deleter
	def AirprtNm(self):
		del self._AirprtNm
		self._AirprtNm = None

	@property
	def Twn(self):
		return self._Twn

	@Twn.setter
	def Twn(self, value):
		self._Twn = value if type(value) != base_types.auto else self.make_default("Twn")

	@Twn.deleter
	def Twn(self):
		del self._Twn
		self._Twn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AirprtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Twn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

