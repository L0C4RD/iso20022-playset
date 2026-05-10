import base_types
import ISINOct2015Identifier
import BenchmarkCurveName2Code

class FinancialInstrument46Choice(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_Indx"]
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
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indx', type=BenchmarkCurveName2Code, min=0, max=1, mutex_group=1, array=False),
	))

