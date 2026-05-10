from . import base_types
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._Max3Number import Max3Number

class SecuritiesTradeDetails103(base_types._BaseFieldType):

	__slots__ = ["_OpngSttlmDt", "_NbOfDaysAcrd", "_InstrPrcgAddtlDtls", "_TradDt"]
	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if type(value) != base_types.auto else self.make_default("InstrPrcgAddtlDtls")

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = None

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != base_types.auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def OpngSttlmDt(self):
		return self._OpngSttlmDt

	@OpngSttlmDt.setter
	def OpngSttlmDt(self, value):
		self._OpngSttlmDt = value if type(value) != base_types.auto else self.make_default("OpngSttlmDt")

	@OpngSttlmDt.deleter
	def OpngSttlmDt(self):
		del self._OpngSttlmDt
		self._OpngSttlmDt = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

