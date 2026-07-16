# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInstructionCancellationRequestStatusAdviceV14

class SEEV_041_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14"
		_docname = "seev.041.001.14"

		__slots__ = ["_CorpActnInstrCxlReqStsAdvc"]
		@property
		def CorpActnInstrCxlReqStsAdvc(self):
			return self._CorpActnInstrCxlReqStsAdvc

		@CorpActnInstrCxlReqStsAdvc.setter
		def CorpActnInstrCxlReqStsAdvc(self, value):
			self._CorpActnInstrCxlReqStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'CorpActnInstrCxlReqStsAdvc', CorporateActionInstructionCancellationRequestStatusAdviceV14, False)

		@CorpActnInstrCxlReqStsAdvc.deleter
		def CorpActnInstrCxlReqStsAdvc(self):
			del self._CorpActnInstrCxlReqStsAdvc
			self._CorpActnInstrCxlReqStsAdvc = base_types.UninitialisedField(self, 'CorpActnInstrCxlReqStsAdvc', CorporateActionInstructionCancellationRequestStatusAdviceV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrCxlReqStsAdvc', type=CorporateActionInstructionCancellationRequestStatusAdviceV14, min=1, max=1, mutex_group=None, array=False),
		))