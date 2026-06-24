# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAGlobalDistributionStatusAdviceV01 import AgentCAGlobalDistributionStatusAdviceV01

class SEEV_018_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.018.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AgtCAGblDstrbtnStsAdvc"]
		@property
		def AgtCAGblDstrbtnStsAdvc(self):
			return self._AgtCAGblDstrbtnStsAdvc

		@AgtCAGblDstrbtnStsAdvc.setter
		def AgtCAGblDstrbtnStsAdvc(self, value):
			self._AgtCAGblDstrbtnStsAdvc = value if type(value) != base_types.auto else self.make_default("AgtCAGblDstrbtnStsAdvc")

		@AgtCAGblDstrbtnStsAdvc.deleter
		def AgtCAGblDstrbtnStsAdvc(self):
			del self._AgtCAGblDstrbtnStsAdvc
			self._AgtCAGblDstrbtnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAGblDstrbtnStsAdvc', type=AgentCAGlobalDistributionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))