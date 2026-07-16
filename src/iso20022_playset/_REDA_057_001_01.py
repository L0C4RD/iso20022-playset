# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StandingSettlementInstructionDeletionV01

class REDA_057_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.057.001.01"
		_docname = "reda.057.001.01"

		__slots__ = ["_StgSttlmInstrDeltn"]
		@property
		def StgSttlmInstrDeltn(self):
			return self._StgSttlmInstrDeltn

		@StgSttlmInstrDeltn.setter
		def StgSttlmInstrDeltn(self, value):
			self._StgSttlmInstrDeltn = value if value is not None else base_types.UninitialisedField(self, 'StgSttlmInstrDeltn', StandingSettlementInstructionDeletionV01, False)

		@StgSttlmInstrDeltn.deleter
		def StgSttlmInstrDeltn(self):
			del self._StgSttlmInstrDeltn
			self._StgSttlmInstrDeltn = base_types.UninitialisedField(self, 'StgSttlmInstrDeltn', StandingSettlementInstructionDeletionV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StgSttlmInstrDeltn', type=StandingSettlementInstructionDeletionV01, min=1, max=1, mutex_group=None, array=False),
		))