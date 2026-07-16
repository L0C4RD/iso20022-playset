# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCANotificationCancellationRequestV01

class SEEV_010_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.010.001.01"
		_docname = "seev.010.001.01"

		__slots__ = ["_AgtCANtfctnCxlReq"]
		@property
		def AgtCANtfctnCxlReq(self):
			return self._AgtCANtfctnCxlReq

		@AgtCANtfctnCxlReq.setter
		def AgtCANtfctnCxlReq(self, value):
			self._AgtCANtfctnCxlReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCANtfctnCxlReq', AgentCANotificationCancellationRequestV01, False)

		@AgtCANtfctnCxlReq.deleter
		def AgtCANtfctnCxlReq(self):
			del self._AgtCANtfctnCxlReq
			self._AgtCANtfctnCxlReq = base_types.UninitialisedField(self, 'AgtCANtfctnCxlReq', AgentCANotificationCancellationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCANtfctnCxlReq', type=AgentCANotificationCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))