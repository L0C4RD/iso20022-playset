from . import base_types
from ._BenchmarkCurveName3Code import BenchmarkCurveName3Code
from ._Max350Text import Max350Text

class BenchmarkCurveName10Choice(base_types._BaseFieldType):

	__slots__ = ["_Indx", "_Nm"]
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
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Indx', type=BenchmarkCurveName3Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=1, array=False),
	))

