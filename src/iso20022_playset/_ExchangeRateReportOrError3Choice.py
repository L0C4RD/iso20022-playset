# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencyExchangeReport4 import CurrencyExchangeReport4
from ._ErrorHandling3 import ErrorHandling3

class ExchangeRateReportOrError3Choice(base_types._BaseFieldType):

	__slots__ = ["_CcyXchgRpt", "_OprlErr"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyXchgRpt', type=CurrencyExchangeReport4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling3, min=1, max=None, mutex_group=1, array=True),
	))