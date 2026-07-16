# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyExchangeReport4
from . import ErrorHandling3

class ExchangeRateReportOrError3Choice(base_types._BaseFieldType):

	__slots__ = ["_CcyXchgRpt", "_OprlErr"]
	@property
	def CcyXchgRpt(self):
		return self._CcyXchgRpt

	@CcyXchgRpt.setter
	def CcyXchgRpt(self, value):
		self._CcyXchgRpt = value if value is not None else base_types.UninitialisedField(self, 'CcyXchgRpt', CurrencyExchangeReport4, True)

	@CcyXchgRpt.deleter
	def CcyXchgRpt(self):
		del self._CcyXchgRpt
		self._CcyXchgRpt = base_types.UninitialisedField(self, 'CcyXchgRpt', CurrencyExchangeReport4, True)

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if value is not None else base_types.UninitialisedField(self, 'OprlErr', ErrorHandling3, True)

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = base_types.UninitialisedField(self, 'OprlErr', ErrorHandling3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyXchgRpt', type=CurrencyExchangeReport4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling3, min=1, max=None, mutex_group=1, array=True),
	))