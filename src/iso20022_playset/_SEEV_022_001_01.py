# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAMovementStatusAdviceV01 import AgentCAMovementStatusAdviceV01

class SEEV_022_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:seev.022.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AgtCAMvmntStsAdvc"]
		@property
		def AgtCAMvmntStsAdvc(self):
			return self._AgtCAMvmntStsAdvc

		@AgtCAMvmntStsAdvc.setter
		def AgtCAMvmntStsAdvc(self, value):
			self._AgtCAMvmntStsAdvc = value if type(value) != base_types.auto else self.make_default("AgtCAMvmntStsAdvc")

		@AgtCAMvmntStsAdvc.deleter
		def AgtCAMvmntStsAdvc(self):
			del self._AgtCAMvmntStsAdvc
			self._AgtCAMvmntStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAMvmntStsAdvc', type=AgentCAMovementStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))