# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAElectionAdviceV01

class SEEV_012_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.012.001.01"
		_docname = "seev.012.001.01"

		__slots__ = ["_AgtCAElctnAdvc"]
		@property
		def AgtCAElctnAdvc(self):
			return self._AgtCAElctnAdvc

		@AgtCAElctnAdvc.setter
		def AgtCAElctnAdvc(self, value):
			self._AgtCAElctnAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnAdvc', AgentCAElectionAdviceV01, False)

		@AgtCAElctnAdvc.deleter
		def AgtCAElctnAdvc(self):
			del self._AgtCAElctnAdvc
			self._AgtCAElctnAdvc = base_types.UninitialisedField(self, 'AgtCAElctnAdvc', AgentCAElectionAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnAdvc', type=AgentCAElectionAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))