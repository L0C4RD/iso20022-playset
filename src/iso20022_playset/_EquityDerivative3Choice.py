from . import base_types
from ._UnderlyingEquityType3Code import UnderlyingEquityType3Code
from ._UnderlyingEquityType4Code import UnderlyingEquityType4Code
from ._UnderlyingEquityType5Code import UnderlyingEquityType5Code
from ._UnderlyingEquityType6Code import UnderlyingEquityType6Code

class EquityDerivative3Choice(base_types._BaseFieldType):

	__slots__ = ["_Bskt", "_Indx", "_Othr", "_SnglNm"]
	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if type(value) != base_types.auto else self.make_default("Bskt")

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = None

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != base_types.auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def SnglNm(self):
		return self._SnglNm

	@SnglNm.setter
	def SnglNm(self, value):
		self._SnglNm = value if type(value) != base_types.auto else self.make_default("SnglNm")

	@SnglNm.deleter
	def SnglNm(self):
		del self._SnglNm
		self._SnglNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bskt', type=UnderlyingEquityType3Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indx', type=UnderlyingEquityType4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=UnderlyingEquityType6Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SnglNm', type=UnderlyingEquityType5Code, min=0, max=1, mutex_group=1, array=False),
	))

