# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCADistributionBreakdownAdviceV01 import AgentCADistributionBreakdownAdviceV01

class SEEV_016_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.016.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AgtCADstrbtnBrkdwnAdvc"]
		@property
		def AgtCADstrbtnBrkdwnAdvc(self):
			return self._AgtCADstrbtnBrkdwnAdvc

		@AgtCADstrbtnBrkdwnAdvc.setter
		def AgtCADstrbtnBrkdwnAdvc(self, value):
			self._AgtCADstrbtnBrkdwnAdvc = value if type(value) != base_types.auto else self.make_default("AgtCADstrbtnBrkdwnAdvc")

		@AgtCADstrbtnBrkdwnAdvc.deleter
		def AgtCADstrbtnBrkdwnAdvc(self):
			del self._AgtCADstrbtnBrkdwnAdvc
			self._AgtCADstrbtnBrkdwnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADstrbtnBrkdwnAdvc', type=AgentCADistributionBreakdownAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))