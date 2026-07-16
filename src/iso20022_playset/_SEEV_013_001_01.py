# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAElectionAmendmentRequestV01

class SEEV_013_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.013.001.01"
		_docname = "seev.013.001.01"

		__slots__ = ["_AgtCAElctnAmdmntReq"]
		@property
		def AgtCAElctnAmdmntReq(self):
			return self._AgtCAElctnAmdmntReq

		@AgtCAElctnAmdmntReq.setter
		def AgtCAElctnAmdmntReq(self, value):
			self._AgtCAElctnAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnAmdmntReq', AgentCAElectionAmendmentRequestV01, False)

		@AgtCAElctnAmdmntReq.deleter
		def AgtCAElctnAmdmntReq(self):
			del self._AgtCAElctnAmdmntReq
			self._AgtCAElctnAmdmntReq = base_types.UninitialisedField(self, 'AgtCAElctnAmdmntReq', AgentCAElectionAmendmentRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnAmdmntReq', type=AgentCAElectionAmendmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))