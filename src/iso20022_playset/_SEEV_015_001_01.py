# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCAElectionStatusAdviceV01

class SEEV_015_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.015.001.01"
		_docname = "seev.015.001.01"

		__slots__ = ["_AgtCAElctnStsAdvc"]
		@property
		def AgtCAElctnStsAdvc(self):
			return self._AgtCAElctnStsAdvc

		@AgtCAElctnStsAdvc.setter
		def AgtCAElctnStsAdvc(self, value):
			self._AgtCAElctnStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnStsAdvc', AgentCAElectionStatusAdviceV01, False)

		@AgtCAElctnStsAdvc.deleter
		def AgtCAElctnStsAdvc(self):
			del self._AgtCAElctnStsAdvc
			self._AgtCAElctnStsAdvc = base_types.UninitialisedField(self, 'AgtCAElctnStsAdvc', AgentCAElectionStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnStsAdvc', type=AgentCAElectionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))