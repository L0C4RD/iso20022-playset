# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCurrencyConversionRequestV12 import AcceptorCurrencyConversionRequestV12

class CAAA_016_001_12():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.016.001.12"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AccptrCcyConvsReq"]
		@property
		def AccptrCcyConvsReq(self):
			return self._AccptrCcyConvsReq

		@AccptrCcyConvsReq.setter
		def AccptrCcyConvsReq(self, value):
			self._AccptrCcyConvsReq = value if type(value) != base_types.auto else self.make_default("AccptrCcyConvsReq")

		@AccptrCcyConvsReq.deleter
		def AccptrCcyConvsReq(self):
			del self._AccptrCcyConvsReq
			self._AccptrCcyConvsReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsReq', type=AcceptorCurrencyConversionRequestV12, min=1, max=1, mutex_group=None, array=False),
		))