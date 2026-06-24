# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyerProtectionInstructionCancellationRequestV01 import BuyerProtectionInstructionCancellationRequestV01

class SEEV_062_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:seev.062.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_BuyrPrtcnInstrCxlReq"]
		@property
		def BuyrPrtcnInstrCxlReq(self):
			return self._BuyrPrtcnInstrCxlReq

		@BuyrPrtcnInstrCxlReq.setter
		def BuyrPrtcnInstrCxlReq(self, value):
			self._BuyrPrtcnInstrCxlReq = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrCxlReq")

		@BuyrPrtcnInstrCxlReq.deleter
		def BuyrPrtcnInstrCxlReq(self):
			del self._BuyrPrtcnInstrCxlReq
			self._BuyrPrtcnInstrCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrCxlReq', type=BuyerProtectionInstructionCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))