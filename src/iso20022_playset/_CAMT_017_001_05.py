# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReturnCurrencyExchangeRateV05 import ReturnCurrencyExchangeRateV05

class CAMT_017_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrCcyXchgRate"]
		@property
		def RtrCcyXchgRate(self):
			return self._RtrCcyXchgRate

		@RtrCcyXchgRate.setter
		def RtrCcyXchgRate(self, value):
			self._RtrCcyXchgRate = value if type(value) != base_types.auto else self.make_default("RtrCcyXchgRate")

		@RtrCcyXchgRate.deleter
		def RtrCcyXchgRate(self):
			del self._RtrCcyXchgRate
			self._RtrCcyXchgRate = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrCcyXchgRate', type=ReturnCurrencyExchangeRateV05, min=1, max=1, mutex_group=None, array=False),
		))