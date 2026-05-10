from . import base_types
from .ISINOct2015Identifier import ISINOct2015Identifier
from .LEIIdentifier import LEIIdentifier

class FinancialInstrument53(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_LEI"]
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

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=None, mutex_group=None, array=True),
	))

