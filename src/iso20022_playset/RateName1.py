from . import base_types
from .Max35Text import Max35Text
from .Max8Text import Max8Text

class RateName1(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_RateNm"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def RateNm(self):
		return self._RateNm

	@RateNm.setter
	def RateNm(self, value):
		self._RateNm = value if type(value) != auto else self.make_default("RateNm")

	@RateNm.deleter
	def RateNm(self):
		del self._RateNm
		self._RateNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

