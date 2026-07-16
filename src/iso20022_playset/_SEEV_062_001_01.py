# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionInstructionCancellationRequestV01

class SEEV_062_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.062.001.01"
		_docname = "seev.062.001.01"

		__slots__ = ["_BuyrPrtcnInstrCxlReq"]
		@property
		def BuyrPrtcnInstrCxlReq(self):
			return self._BuyrPrtcnInstrCxlReq

		@BuyrPrtcnInstrCxlReq.setter
		def BuyrPrtcnInstrCxlReq(self, value):
			self._BuyrPrtcnInstrCxlReq = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstrCxlReq', BuyerProtectionInstructionCancellationRequestV01, False)

		@BuyrPrtcnInstrCxlReq.deleter
		def BuyrPrtcnInstrCxlReq(self):
			del self._BuyrPrtcnInstrCxlReq
			self._BuyrPrtcnInstrCxlReq = base_types.UninitialisedField(self, 'BuyrPrtcnInstrCxlReq', BuyerProtectionInstructionCancellationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrCxlReq', type=BuyerProtectionInstructionCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))