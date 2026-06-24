# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StandingSettlementInstructionCancellationV01 import StandingSettlementInstructionCancellationV01

class REDA_059_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.059.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_StgSttlmInstrCxl"]
		@property
		def StgSttlmInstrCxl(self):
			return self._StgSttlmInstrCxl

		@StgSttlmInstrCxl.setter
		def StgSttlmInstrCxl(self, value):
			self._StgSttlmInstrCxl = value if type(value) != base_types.auto else self.make_default("StgSttlmInstrCxl")

		@StgSttlmInstrCxl.deleter
		def StgSttlmInstrCxl(self):
			del self._StgSttlmInstrCxl
			self._StgSttlmInstrCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstrCxl', type=StandingSettlementInstructionCancellationV01, min=1, max=1, mutex_group=None, array=False),
		))