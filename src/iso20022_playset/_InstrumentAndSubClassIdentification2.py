from . import base_types
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._NonEquityInstrumentReportingClassification1Code import NonEquityInstrumentReportingClassification1Code
from ._NonEquitySubClass1 import NonEquitySubClass1

class InstrumentAndSubClassIdentification2(base_types._BaseFieldType):

	__slots__ = ["_DerivSubClss", "_FinInstrmClssfctn", "_ISIN"]
	@property
	def DerivSubClss(self):
		return self._DerivSubClss

	@DerivSubClss.setter
	def DerivSubClss(self, value):
		self._DerivSubClss = value if type(value) != base_types.auto else self.make_default("DerivSubClss")

	@DerivSubClss.deleter
	def DerivSubClss(self):
		del self._DerivSubClss
		self._DerivSubClss = None

	@property
	def FinInstrmClssfctn(self):
		return self._FinInstrmClssfctn

	@FinInstrmClssfctn.setter
	def FinInstrmClssfctn(self, value):
		self._FinInstrmClssfctn = value if type(value) != base_types.auto else self.make_default("FinInstrmClssfctn")

	@FinInstrmClssfctn.deleter
	def FinInstrmClssfctn(self):
		del self._FinInstrmClssfctn
		self._FinInstrmClssfctn = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DerivSubClss', type=NonEquitySubClass1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmClssfctn', type=NonEquityInstrumentReportingClassification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))

