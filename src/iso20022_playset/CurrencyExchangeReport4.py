from . import base_types
import CurrencySourceTarget1
import ExchangeRateReportOrError4Choice

class CurrencyExchangeReport4(base_types._BaseFieldType):

	__slots__ = ["_CcyXchgOrErr", "_CcyRef"]
	@property
	def CcyXchgOrErr(self):
		return self._CcyXchgOrErr

	@CcyXchgOrErr.setter
	def CcyXchgOrErr(self, value):
		self._CcyXchgOrErr = value if type(value) != auto else self.make_default("CcyXchgOrErr")

	@CcyXchgOrErr.deleter
	def CcyXchgOrErr(self):
		del self._CcyXchgOrErr
		self._CcyXchgOrErr = None

	@property
	def CcyRef(self):
		return self._CcyRef

	@CcyRef.setter
	def CcyRef(self, value):
		self._CcyRef = value if type(value) != auto else self.make_default("CcyRef")

	@CcyRef.deleter
	def CcyRef(self):
		del self._CcyRef
		self._CcyRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyXchgOrErr', type=ExchangeRateReportOrError4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyRef', type=CurrencySourceTarget1, min=1, max=1, mutex_group=None, array=False),
	))

