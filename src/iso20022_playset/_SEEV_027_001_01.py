# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAStandingInstructionStatusAdviceV01

class SEEV_027_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.027.001.01"
		_docname = "seev.027.001.01"

		__slots__ = ["_AgtCAStgInstrStsAdvc"]
		@property
		def AgtCAStgInstrStsAdvc(self):
			return self._AgtCAStgInstrStsAdvc

		@AgtCAStgInstrStsAdvc.setter
		def AgtCAStgInstrStsAdvc(self, value):
			self._AgtCAStgInstrStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCAStgInstrStsAdvc', AgentCAStandingInstructionStatusAdviceV01, False)

		@AgtCAStgInstrStsAdvc.deleter
		def AgtCAStgInstrStsAdvc(self):
			del self._AgtCAStgInstrStsAdvc
			self._AgtCAStgInstrStsAdvc = base_types.UninitialisedField(self, 'AgtCAStgInstrStsAdvc', AgentCAStandingInstructionStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAStgInstrStsAdvc', type=AgentCAStandingInstructionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))