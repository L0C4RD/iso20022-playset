# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StandingSettlementInstructionV01 import StandingSettlementInstructionV01

class REDA_056_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.056.001.01"
		_docname = "reda.056.001.01"

		__slots__ = ["_StgSttlmInstr"]
		@property
		def StgSttlmInstr(self):
			return self._StgSttlmInstr

		@StgSttlmInstr.setter
		def StgSttlmInstr(self, value):
			self._StgSttlmInstr = value if type(value) != base_types.auto else self.make_default("StgSttlmInstr")

		@StgSttlmInstr.deleter
		def StgSttlmInstr(self):
			del self._StgSttlmInstr
			self._StgSttlmInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstr', type=StandingSettlementInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))