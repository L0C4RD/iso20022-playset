# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationRequestV14 import AcceptorCancellationRequestV14

class CAAA_005_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.005.001.14"
		_docname = "caaa.005.001.14"

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
			base_types.FieldEntry(name='AccptrCxlReq', type=AcceptorCancellationRequestV14, min=1, max=1, mutex_group=None, array=False),
		))