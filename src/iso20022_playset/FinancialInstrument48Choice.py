import base_types
import FinancialInstrument58
import ISINOct2015Identifier
import LEIIdentifier

class FinancialInstrument48Choice(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_ISIN", "_Indx"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

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
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indx', type=FinancialInstrument58, min=0, max=1, mutex_group=1, array=False),
	))

