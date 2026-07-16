# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencySourceTarget1
from . import ExchangeRateReportOrError4Choice

class CurrencyExchangeReport4(base_types._BaseFieldType):

	__slots__ = ["_CcyRef", "_CcyXchgOrErr"]
	@property
	def CcyRef(self):
		return self._CcyRef

	@CcyRef.setter
	def CcyRef(self, value):
		self._CcyRef = value if value is not None else base_types.UninitialisedField(self, 'CcyRef', CurrencySourceTarget1, False)

	@CcyRef.deleter
	def CcyRef(self):
		del self._CcyRef
		self._CcyRef = base_types.UninitialisedField(self, 'CcyRef', CurrencySourceTarget1, False)

	@property
	def CcyXchgOrErr(self):
		return self._CcyXchgOrErr

	@CcyXchgOrErr.setter
	def CcyXchgOrErr(self, value):
		self._CcyXchgOrErr = value if value is not None else base_types.UninitialisedField(self, 'CcyXchgOrErr', ExchangeRateReportOrError4Choice, False)

	@CcyXchgOrErr.deleter
	def CcyXchgOrErr(self):
		del self._CcyXchgOrErr
		self._CcyXchgOrErr = base_types.UninitialisedField(self, 'CcyXchgOrErr', ExchangeRateReportOrError4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyRef', type=CurrencySourceTarget1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchgOrErr', type=ExchangeRateReportOrError4Choice, min=1, max=1, mutex_group=None, array=False),
	))