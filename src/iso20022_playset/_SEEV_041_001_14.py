# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInstructionCancellationRequestStatusAdviceV14 import CorporateActionInstructionCancellationRequestStatusAdviceV14

class SEEV_041_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:seev.041.001.14",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
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
			base_types.FieldEntry(name='CorpActnInstrCxlReqStsAdvc', type=CorporateActionInstructionCancellationRequestStatusAdviceV14, min=1, max=1, mutex_group=None, array=False),
		))