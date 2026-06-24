# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInstructionCancellationRequestStatusAdviceV15 import CorporateActionInstructionCancellationRequestStatusAdviceV15

class SEEV_041_001_15():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.041.001.15"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CorpActnInstrCxlReqStsAdvc"]
		@property
		def CorpActnInstrCxlReqStsAdvc(self):
			return self._CorpActnInstrCxlReqStsAdvc

		@CorpActnInstrCxlReqStsAdvc.setter
		def CorpActnInstrCxlReqStsAdvc(self, value):
			self._CorpActnInstrCxlReqStsAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnInstrCxlReqStsAdvc")

		@CorpActnInstrCxlReqStsAdvc.deleter
		def CorpActnInstrCxlReqStsAdvc(self):
			del self._CorpActnInstrCxlReqStsAdvc
			self._CorpActnInstrCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrCxlReqStsAdvc', type=CorporateActionInstructionCancellationRequestStatusAdviceV15, min=1, max=1, mutex_group=None, array=False),
		))