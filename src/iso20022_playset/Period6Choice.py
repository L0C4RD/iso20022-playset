from . import base_types
from .Period11 import Period11
from .DateType8Code import DateType8Code

class Period6Choice(base_types._BaseFieldType):

	__slots__ = ["_PrdCd", "_Prd"]
	@property
	def PrdCd(self):
		return self._PrdCd

	@PrdCd.setter
	def PrdCd(self, value):
		self._PrdCd = value if type(value) != base_types.auto else self.make_default("PrdCd")

	@PrdCd.deleter
	def PrdCd(self):
		del self._PrdCd
		self._PrdCd = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrdCd', type=DateType8Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prd', type=Period11, min=0, max=1, mutex_group=1, array=False),
	))

