# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAMovementCancellationRequestV01

class SEEV_020_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.020.001.01"
		_docname = "seev.020.001.01"

		__slots__ = ["_AgtCAMvmntCxlReq"]
		@property
		def AgtCAMvmntCxlReq(self):
			return self._AgtCAMvmntCxlReq

		@AgtCAMvmntCxlReq.setter
		def AgtCAMvmntCxlReq(self, value):
			self._AgtCAMvmntCxlReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCAMvmntCxlReq', AgentCAMovementCancellationRequestV01, False)

		@AgtCAMvmntCxlReq.deleter
		def AgtCAMvmntCxlReq(self):
			del self._AgtCAMvmntCxlReq
			self._AgtCAMvmntCxlReq = base_types.UninitialisedField(self, 'AgtCAMvmntCxlReq', AgentCAMovementCancellationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAMvmntCxlReq', type=AgentCAMovementCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))