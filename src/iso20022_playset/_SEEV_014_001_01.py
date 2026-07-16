# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAElectionCancellationRequestV01

class SEEV_014_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.014.001.01"
		_docname = "seev.014.001.01"

		__slots__ = ["_AgtCAElctnCxlReq"]
		@property
		def AgtCAElctnCxlReq(self):
			return self._AgtCAElctnCxlReq

		@AgtCAElctnCxlReq.setter
		def AgtCAElctnCxlReq(self, value):
			self._AgtCAElctnCxlReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnCxlReq', AgentCAElectionCancellationRequestV01, False)

		@AgtCAElctnCxlReq.deleter
		def AgtCAElctnCxlReq(self):
			del self._AgtCAElctnCxlReq
			self._AgtCAElctnCxlReq = base_types.UninitialisedField(self, 'AgtCAElctnCxlReq', AgentCAElectionCancellationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnCxlReq', type=AgentCAElectionCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))