# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAStandingInstructionRequestV01

class SEEV_025_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.025.001.01"
		_docname = "seev.025.001.01"

		__slots__ = ["_AgtCAStgInstrReq"]
		@property
		def AgtCAStgInstrReq(self):
			return self._AgtCAStgInstrReq

		@AgtCAStgInstrReq.setter
		def AgtCAStgInstrReq(self, value):
			self._AgtCAStgInstrReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCAStgInstrReq', AgentCAStandingInstructionRequestV01, False)

		@AgtCAStgInstrReq.deleter
		def AgtCAStgInstrReq(self):
			del self._AgtCAStgInstrReq
			self._AgtCAStgInstrReq = base_types.UninitialisedField(self, 'AgtCAStgInstrReq', AgentCAStandingInstructionRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAStgInstrReq', type=AgentCAStandingInstructionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))