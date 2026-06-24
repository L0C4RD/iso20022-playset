# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationRequestV15 import AcceptorCancellationRequestV15

class CAAA_005_001_15():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.005.001.15"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AccptrCxlReq"]
		@property
		def AccptrCxlReq(self):
			return self._AccptrCxlReq

		@AccptrCxlReq.setter
		def AccptrCxlReq(self, value):
			self._AccptrCxlReq = value if type(value) != base_types.auto else self.make_default("AccptrCxlReq")

		@AccptrCxlReq.deleter
		def AccptrCxlReq(self):
			del self._AccptrCxlReq
			self._AccptrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlReq', type=AcceptorCancellationRequestV15, min=1, max=1, mutex_group=None, array=False),
		))