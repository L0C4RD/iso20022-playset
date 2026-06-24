# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAStandingInstructionRequestV01 import AgentCAStandingInstructionRequestV01

class SEEV_025_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.025.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AgtCAStgInstrReq"]
		@property
		def AgtCAStgInstrReq(self):
			return self._AgtCAStgInstrReq

		@AgtCAStgInstrReq.setter
		def AgtCAStgInstrReq(self, value):
			self._AgtCAStgInstrReq = value if type(value) != base_types.auto else self.make_default("AgtCAStgInstrReq")

		@AgtCAStgInstrReq.deleter
		def AgtCAStgInstrReq(self):
			del self._AgtCAStgInstrReq
			self._AgtCAStgInstrReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAStgInstrReq', type=AgentCAStandingInstructionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))