# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAGlobalDistributionAuthorisationRequestV01

class SEEV_017_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.017.001.01"
		_docname = "seev.017.001.01"

		__slots__ = ["_AgtCAGblDstrbtnAuthstnReq"]
		@property
		def AgtCAGblDstrbtnAuthstnReq(self):
			return self._AgtCAGblDstrbtnAuthstnReq

		@AgtCAGblDstrbtnAuthstnReq.setter
		def AgtCAGblDstrbtnAuthstnReq(self, value):
			self._AgtCAGblDstrbtnAuthstnReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCAGblDstrbtnAuthstnReq', AgentCAGlobalDistributionAuthorisationRequestV01, False)

		@AgtCAGblDstrbtnAuthstnReq.deleter
		def AgtCAGblDstrbtnAuthstnReq(self):
			del self._AgtCAGblDstrbtnAuthstnReq
			self._AgtCAGblDstrbtnAuthstnReq = base_types.UninitialisedField(self, 'AgtCAGblDstrbtnAuthstnReq', AgentCAGlobalDistributionAuthorisationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAGblDstrbtnAuthstnReq', type=AgentCAGlobalDistributionAuthorisationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))