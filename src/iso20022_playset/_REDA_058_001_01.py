# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StandingSettlementInstructionStatusAdviceV01 import StandingSettlementInstructionStatusAdviceV01

class REDA_058_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:reda.058.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_StgSttlmInstrStsAdvc"]
		@property
		def StgSttlmInstrStsAdvc(self):
			return self._StgSttlmInstrStsAdvc

		@StgSttlmInstrStsAdvc.setter
		def StgSttlmInstrStsAdvc(self, value):
			self._StgSttlmInstrStsAdvc = value if type(value) != base_types.auto else self.make_default("StgSttlmInstrStsAdvc")

		@StgSttlmInstrStsAdvc.deleter
		def StgSttlmInstrStsAdvc(self):
			del self._StgSttlmInstrStsAdvc
			self._StgSttlmInstrStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstrStsAdvc', type=StandingSettlementInstructionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))