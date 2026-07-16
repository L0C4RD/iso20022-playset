# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAInformationAdviceV01

class SEEV_023_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.023.001.01"
		_docname = "seev.023.001.01"

		__slots__ = ["_AgtCAInfAdvc"]
		@property
		def AgtCAInfAdvc(self):
			return self._AgtCAInfAdvc

		@AgtCAInfAdvc.setter
		def AgtCAInfAdvc(self, value):
			self._AgtCAInfAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCAInfAdvc', AgentCAInformationAdviceV01, False)

		@AgtCAInfAdvc.deleter
		def AgtCAInfAdvc(self):
			del self._AgtCAInfAdvc
			self._AgtCAInfAdvc = base_types.UninitialisedField(self, 'AgtCAInfAdvc', AgentCAInformationAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAInfAdvc', type=AgentCAInformationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))