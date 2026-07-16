# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAMovementStatusAdviceV01

class SEEV_022_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.022.001.01"
		_docname = "seev.022.001.01"

		__slots__ = ["_AgtCAMvmntStsAdvc"]
		@property
		def AgtCAMvmntStsAdvc(self):
			return self._AgtCAMvmntStsAdvc

		@AgtCAMvmntStsAdvc.setter
		def AgtCAMvmntStsAdvc(self, value):
			self._AgtCAMvmntStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCAMvmntStsAdvc', AgentCAMovementStatusAdviceV01, False)

		@AgtCAMvmntStsAdvc.deleter
		def AgtCAMvmntStsAdvc(self):
			del self._AgtCAMvmntStsAdvc
			self._AgtCAMvmntStsAdvc = base_types.UninitialisedField(self, 'AgtCAMvmntStsAdvc', AgentCAMovementStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAMvmntStsAdvc', type=AgentCAMovementStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))