from . import base_types
from .ErrorHandling3 import ErrorHandling3
from .CurrencyExchangeReport4 import CurrencyExchangeReport4

class ExchangeRateReportOrError3Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_CcyXchgRpt"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	@property
	def CcyXchgRpt(self):
		return self._CcyXchgRpt

	@CcyXchgRpt.setter
	def CcyXchgRpt(self, value):
		self._CcyXchgRpt = value if type(value) != base_types.auto else self.make_default("CcyXchgRpt")

	@CcyXchgRpt.deleter
	def CcyXchgRpt(self):
		del self._CcyXchgRpt
		self._CcyXchgRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling3, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='CcyXchgRpt', type=CurrencyExchangeReport4, min=1, max=None, mutex_group=1, array=True),
	))

