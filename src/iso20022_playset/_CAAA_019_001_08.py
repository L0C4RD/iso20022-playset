# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCurrencyConversionAdviceResponseV08

class CAAA_019_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.019.001.08"
		_docname = "caaa.019.001.08"

		__slots__ = ["_AccptrCcyConvsAdvcRspn"]
		@property
		def AccptrCcyConvsAdvcRspn(self):
			return self._AccptrCcyConvsAdvcRspn

		@AccptrCcyConvsAdvcRspn.setter
		def AccptrCcyConvsAdvcRspn(self, value):
			self._AccptrCcyConvsAdvcRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrCcyConvsAdvcRspn', AcceptorCurrencyConversionAdviceResponseV08, False)

		@AccptrCcyConvsAdvcRspn.deleter
		def AccptrCcyConvsAdvcRspn(self):
			del self._AccptrCcyConvsAdvcRspn
			self._AccptrCcyConvsAdvcRspn = base_types.UninitialisedField(self, 'AccptrCcyConvsAdvcRspn', AcceptorCurrencyConversionAdviceResponseV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsAdvcRspn', type=AcceptorCurrencyConversionAdviceResponseV08, min=1, max=1, mutex_group=None, array=False),
		))