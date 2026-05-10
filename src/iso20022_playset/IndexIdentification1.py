from . import base_types
import Max350Text
import ExternalBenchmarkCurveName1Code
import ISINOct2015Identifier

class IndexIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Nm", "_ISIN", "_Indx"]
	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Indx', type=ExternalBenchmarkCurveName1Code, min=0, max=1, mutex_group=None, array=False),
	))

