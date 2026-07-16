# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GetCurrencyExchangeRateV04

class CAMT_016_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.016.001.04"
		_docname = "camt.016.001.04"

		__slots__ = ["_GetCcyXchgRate"]
		@property
		def GetCcyXchgRate(self):
			return self._GetCcyXchgRate

		@GetCcyXchgRate.setter
		def GetCcyXchgRate(self, value):
			self._GetCcyXchgRate = value if value is not None else base_types.UninitialisedField(self, 'GetCcyXchgRate', GetCurrencyExchangeRateV04, False)

		@GetCcyXchgRate.deleter
		def GetCcyXchgRate(self):
			del self._GetCcyXchgRate
			self._GetCcyXchgRate = base_types.UninitialisedField(self, 'GetCcyXchgRate', GetCurrencyExchangeRateV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='GetCcyXchgRate', type=GetCurrencyExchangeRateV04, min=1, max=1, mutex_group=None, array=False),
		))