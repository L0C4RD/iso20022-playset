# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCurrencyConversionRequestV13

class CAAA_016_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.016.001.13"
		_docname = "caaa.016.001.13"

		__slots__ = ["_AccptrCcyConvsReq"]
		@property
		def AccptrCcyConvsReq(self):
			return self._AccptrCcyConvsReq

		@AccptrCcyConvsReq.setter
		def AccptrCcyConvsReq(self, value):
			self._AccptrCcyConvsReq = value if value is not None else base_types.UninitialisedField(self, 'AccptrCcyConvsReq', AcceptorCurrencyConversionRequestV13, False)

		@AccptrCcyConvsReq.deleter
		def AccptrCcyConvsReq(self):
			del self._AccptrCcyConvsReq
			self._AccptrCcyConvsReq = base_types.UninitialisedField(self, 'AccptrCcyConvsReq', AcceptorCurrencyConversionRequestV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsReq', type=AcceptorCurrencyConversionRequestV13, min=1, max=1, mutex_group=None, array=False),
		))