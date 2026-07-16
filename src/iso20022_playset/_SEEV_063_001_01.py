# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionInstructionCancellationRequestStatusAdviceV01

class SEEV_063_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.063.001.01"
		_docname = "seev.063.001.01"

		__slots__ = ["_BuyrPrtcnInstrCxlReqStsAdvc"]
		@property
		def BuyrPrtcnInstrCxlReqStsAdvc(self):
			return self._BuyrPrtcnInstrCxlReqStsAdvc

		@BuyrPrtcnInstrCxlReqStsAdvc.setter
		def BuyrPrtcnInstrCxlReqStsAdvc(self, value):
			self._BuyrPrtcnInstrCxlReqStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrCxlReqStsAdvc', BuyerProtectionInstructionCancellationRequestStatusAdviceV01, False)

		@BuyrPrtcnInstrCxlReqStsAdvc.deleter
		def BuyrPrtcnInstrCxlReqStsAdvc(self):
			del self._BuyrPrtcnInstrCxlReqStsAdvc
			self._BuyrPrtcnInstrCxlReqStsAdvc = base_types.UninitialisedField(self, 'BuyrPrtcnInstrCxlReqStsAdvc', BuyerProtectionInstructionCancellationRequestStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrCxlReqStsAdvc', type=BuyerProtectionInstructionCancellationRequestStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))