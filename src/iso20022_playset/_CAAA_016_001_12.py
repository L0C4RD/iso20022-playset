# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCurrencyConversionRequestV12

class CAAA_016_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.016.001.12"
		_docname = "caaa.016.001.12"

		__slots__ = ["_AccptrCcyConvsReq"]
		@property
		def AccptrCcyConvsReq(self):
			return self._AccptrCcyConvsReq

		@AccptrCcyConvsReq.setter
		def AccptrCcyConvsReq(self, value):
			self._AccptrCcyConvsReq = value if value is not None else base_types.UninitialisedField(self, 'AccptrCcyConvsReq', AcceptorCurrencyConversionRequestV12, False)

		@AccptrCcyConvsReq.deleter
		def AccptrCcyConvsReq(self):
			del self._AccptrCcyConvsReq
			self._AccptrCcyConvsReq = base_types.UninitialisedField(self, 'AccptrCcyConvsReq', AcceptorCurrencyConversionRequestV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsReq', type=AcceptorCurrencyConversionRequestV12, min=1, max=1, mutex_group=None, array=False),
		))