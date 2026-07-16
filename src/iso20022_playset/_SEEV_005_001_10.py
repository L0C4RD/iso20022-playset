# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MeetingInstructionCancellationRequestV10

class SEEV_005_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.005.001.10"
		_docname = "seev.005.001.10"

		__slots__ = ["_MtgInstrCxlReq"]
		@property
		def MtgInstrCxlReq(self):
			return self._MtgInstrCxlReq

		@MtgInstrCxlReq.setter
		def MtgInstrCxlReq(self, value):
			self._MtgInstrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'MtgInstrCxlReq', MeetingInstructionCancellationRequestV10, False)

		@MtgInstrCxlReq.deleter
		def MtgInstrCxlReq(self):
			del self._MtgInstrCxlReq
			self._MtgInstrCxlReq = base_types.UninitialisedField(self, 'MtgInstrCxlReq', MeetingInstructionCancellationRequestV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgInstrCxlReq', type=MeetingInstructionCancellationRequestV10, min=1, max=1, mutex_group=None, array=False),
		))