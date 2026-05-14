# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CurrencySourceTarget1 import CurrencySourceTarget1
from ._ExchangeRateReportOrError4Choice import ExchangeRateReportOrError4Choice

class CurrencyExchangeReport4(base_types._BaseFieldType):

	__slots__ = ["_CcyRef", "_CcyXchgOrErr"]
	@property
	def CcyRef(self):
		return self._CcyRef

	@CcyRef.setter
	def CcyRef(self, value):
		self._CcyRef = value if type(value) != base_types.auto else self.make_default("CcyRef")

	@CcyRef.deleter
	def CcyRef(self):
		del self._CcyRef
		self._CcyRef = None

	@property
	def CcyXchgOrErr(self):
		return self._CcyXchgOrErr

	@CcyXchgOrErr.setter
	def CcyXchgOrErr(self, value):
		self._CcyXchgOrErr = value if type(value) != base_types.auto else self.make_default("CcyXchgOrErr")

	@CcyXchgOrErr.deleter
	def CcyXchgOrErr(self):
		del self._CcyXchgOrErr
		self._CcyXchgOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CcyRef', type=CurrencySourceTarget1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyXchgOrErr', type=ExchangeRateReportOrError4Choice, min=1, max=1, mutex_group=None, array=False),
	))