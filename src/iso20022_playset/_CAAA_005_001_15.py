# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorCancellationRequestV15

class CAAA_005_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.005.001.15"
		_docname = "caaa.005.001.15"

		__slots__ = ["_AccptrCxlReq"]
		@property
		def AccptrCxlReq(self):
			return self._AccptrCxlReq

		@AccptrCxlReq.setter
		def AccptrCxlReq(self, value):
			self._AccptrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'AccptrCxlReq', AcceptorCancellationRequestV15, False)

		@AccptrCxlReq.deleter
		def AccptrCxlReq(self):
			del self._AccptrCxlReq
			self._AccptrCxlReq = base_types.UninitialisedField(self, 'AccptrCxlReq', AcceptorCancellationRequestV15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlReq', type=AcceptorCancellationRequestV15, min=1, max=1, mutex_group=None, array=False),
		))