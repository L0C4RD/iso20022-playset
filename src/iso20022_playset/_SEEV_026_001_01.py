# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAStandingInstructionCancellationRequestV01

class SEEV_026_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.026.001.01"
		_docname = "seev.026.001.01"

		__slots__ = ["_AgtCAStgInstrCxlReq"]
		@property
		def AgtCAStgInstrCxlReq(self):
			return self._AgtCAStgInstrCxlReq

		@AgtCAStgInstrCxlReq.setter
		def AgtCAStgInstrCxlReq(self, value):
			self._AgtCAStgInstrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCAStgInstrCxlReq', AgentCAStandingInstructionCancellationRequestV01, False)

		@AgtCAStgInstrCxlReq.deleter
		def AgtCAStgInstrCxlReq(self):
			del self._AgtCAStgInstrCxlReq
			self._AgtCAStgInstrCxlReq = base_types.UninitialisedField(self, 'AgtCAStgInstrCxlReq', AgentCAStandingInstructionCancellationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAStgInstrCxlReq', type=AgentCAStandingInstructionCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))