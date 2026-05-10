from . import base_types
from .ErrorHandling3 import ErrorHandling3
from .CurrencyExchange20 import CurrencyExchange20

class ExchangeRateReportOrError4Choice(base_types._BaseFieldType):

	__slots__ = ["_CcyXchg", "_BizErr"]
	@property
	def CcyXchg(self):
		return self._CcyXchg

	@CcyXchg.setter
	def CcyXchg(self, value):
		self._CcyXchg = value if type(value) != base_types.auto else self.make_default("CcyXchg")

	@CcyXchg.deleter
	def CcyXchg(self):
		del self._CcyXchg
		self._CcyXchg = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyXchg', type=CurrencyExchange20, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling3, min=1, max=None, mutex_group=1, array=True),
	))

