# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReturnCurrencyExchangeRateV05

class CAMT_017_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.017.001.05"
		_docname = "camt.017.001.05"

		__slots__ = ["_RtrCcyXchgRate"]
		@property
		def RtrCcyXchgRate(self):
			return self._RtrCcyXchgRate

		@RtrCcyXchgRate.setter
		def RtrCcyXchgRate(self, value):
			self._RtrCcyXchgRate = value if value is not None else base_types.UninitialisedField(self, 'RtrCcyXchgRate', ReturnCurrencyExchangeRateV05, False)

		@RtrCcyXchgRate.deleter
		def RtrCcyXchgRate(self):
			del self._RtrCcyXchgRate
			self._RtrCcyXchgRate = base_types.UninitialisedField(self, 'RtrCcyXchgRate', ReturnCurrencyExchangeRateV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrCcyXchgRate', type=ReturnCurrencyExchangeRateV05, min=1, max=1, mutex_group=None, array=False),
		))