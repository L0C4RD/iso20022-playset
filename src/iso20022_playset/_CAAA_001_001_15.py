# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorAuthorisationRequestV15 import AcceptorAuthorisationRequestV15

class CAAA_001_001_15():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.001.001.15"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AccptrAuthstnReq"]
		@property
		def AccptrAuthstnReq(self):
			return self._AccptrAuthstnReq

		@AccptrAuthstnReq.setter
		def AccptrAuthstnReq(self, value):
			self._AccptrAuthstnReq = value if type(value) != base_types.auto else self.make_default("AccptrAuthstnReq")

		@AccptrAuthstnReq.deleter
		def AccptrAuthstnReq(self):
			del self._AccptrAuthstnReq
			self._AccptrAuthstnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrAuthstnReq', type=AcceptorAuthorisationRequestV15, min=1, max=1, mutex_group=None, array=False),
		))