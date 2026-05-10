from . import base_types
from ._BenchmarkCurveName2Code import BenchmarkCurveName2Code
from ._Max20000Text import Max20000Text
from ._Max350Text import Max350Text

class BenchmarkDetail1(base_types._BaseFieldType):

	__slots__ = ["_Cmnt", "_FullNm", "_Indx"]
	@property
	def Cmnt(self):
		return self._Cmnt

	@Cmnt.setter
	def Cmnt(self, value):
		self._Cmnt = value if type(value) != base_types.auto else self.make_default("Cmnt")

	@Cmnt.deleter
	def Cmnt(self):
		del self._Cmnt
		self._Cmnt = None

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if type(value) != base_types.auto else self.make_default("FullNm")

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmnt', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Indx', type=BenchmarkCurveName2Code, min=0, max=1, mutex_group=None, array=False),
	))

