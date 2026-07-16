# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StandingSettlementInstructionCancellationV01

class REDA_059_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.059.001.01"
		_docname = "reda.059.001.01"

		__slots__ = ["_StgSttlmInstrCxl"]
		@property
		def StgSttlmInstrCxl(self):
			return self._StgSttlmInstrCxl

		@StgSttlmInstrCxl.setter
		def StgSttlmInstrCxl(self, value):
			self._StgSttlmInstrCxl = value if value is not None else base_types.UninitialisedField(self, 'StgSttlmInstrCxl', StandingSettlementInstructionCancellationV01, False)

		@StgSttlmInstrCxl.deleter
		def StgSttlmInstrCxl(self):
			del self._StgSttlmInstrCxl
			self._StgSttlmInstrCxl = base_types.UninitialisedField(self, 'StgSttlmInstrCxl', StandingSettlementInstructionCancellationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstrCxl', type=StandingSettlementInstructionCancellationV01, min=1, max=1, mutex_group=None, array=False),
		))