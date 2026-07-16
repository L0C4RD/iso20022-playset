# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAGlobalDistributionStatusAdviceV01

class SEEV_018_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.018.001.01"
		_docname = "seev.018.001.01"

		__slots__ = ["_AgtCAGblDstrbtnStsAdvc"]
		@property
		def AgtCAGblDstrbtnStsAdvc(self):
			return self._AgtCAGblDstrbtnStsAdvc

		@AgtCAGblDstrbtnStsAdvc.setter
		def AgtCAGblDstrbtnStsAdvc(self, value):
			self._AgtCAGblDstrbtnStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCAGblDstrbtnStsAdvc', AgentCAGlobalDistributionStatusAdviceV01, False)

		@AgtCAGblDstrbtnStsAdvc.deleter
		def AgtCAGblDstrbtnStsAdvc(self):
			del self._AgtCAGblDstrbtnStsAdvc
			self._AgtCAGblDstrbtnStsAdvc = base_types.UninitialisedField(self, 'AgtCAGblDstrbtnStsAdvc', AgentCAGlobalDistributionStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAGblDstrbtnStsAdvc', type=AgentCAGlobalDistributionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))