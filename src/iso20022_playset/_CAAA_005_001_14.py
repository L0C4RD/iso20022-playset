# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCancellationRequestV14

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
			self._AccptrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'AccptrCxlReq', AcceptorCancellationRequestV14, False)

		@AccptrCxlReq.deleter
		def AccptrCxlReq(self):
			del self._AccptrCxlReq
			self._AccptrCxlReq = base_types.UninitialisedField(self, 'AccptrCxlReq', AcceptorCancellationRequestV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlReq', type=AcceptorCancellationRequestV14, min=1, max=1, mutex_group=None, array=False),
		))