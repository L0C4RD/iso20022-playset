# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyExchange20
from . import ErrorHandling3

class ExchangeRateReportOrError4Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_CcyXchg"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling3, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling3, True)

	@property
	def CcyXchg(self):
		return self._CcyXchg

	@CcyXchg.setter
	def CcyXchg(self, value):
		self._CcyXchg = value if value is not None else base_types.UninitialisedField(self, 'CcyXchg', CurrencyExchange20, False)

	@CcyXchg.deleter
	def CcyXchg(self):
		del self._CcyXchg
		self._CcyXchg = base_types.UninitialisedField(self, 'CcyXchg', CurrencyExchange20, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling3, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='CcyXchg', type=CurrencyExchange20, min=0, max=1, mutex_group=1, array=False),
	))