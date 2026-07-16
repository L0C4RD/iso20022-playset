# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCADistributionBreakdownAdviceV01

class SEEV_016_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.016.001.01"
		_docname = "seev.016.001.01"

		__slots__ = ["_AgtCADstrbtnBrkdwnAdvc"]
		@property
		def AgtCADstrbtnBrkdwnAdvc(self):
			return self._AgtCADstrbtnBrkdwnAdvc

		@AgtCADstrbtnBrkdwnAdvc.setter
		def AgtCADstrbtnBrkdwnAdvc(self, value):
			self._AgtCADstrbtnBrkdwnAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCADstrbtnBrkdwnAdvc', AgentCADistributionBreakdownAdviceV01, False)

		@AgtCADstrbtnBrkdwnAdvc.deleter
		def AgtCADstrbtnBrkdwnAdvc(self):
			del self._AgtCADstrbtnBrkdwnAdvc
			self._AgtCADstrbtnBrkdwnAdvc = base_types.UninitialisedField(self, 'AgtCADstrbtnBrkdwnAdvc', AgentCADistributionBreakdownAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADstrbtnBrkdwnAdvc', type=AgentCADistributionBreakdownAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))