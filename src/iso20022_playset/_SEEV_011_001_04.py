# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCANotificationStatusAdviceV04

class SEEV_011_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.011.001.04"
		_docname = "seev.011.001.04"

		__slots__ = ["_AgtCANtfctnStsAdvc"]
		@property
		def AgtCANtfctnStsAdvc(self):
			return self._AgtCANtfctnStsAdvc

		@AgtCANtfctnStsAdvc.setter
		def AgtCANtfctnStsAdvc(self, value):
			self._AgtCANtfctnStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCANtfctnStsAdvc', AgentCANotificationStatusAdviceV04, False)

		@AgtCANtfctnStsAdvc.deleter
		def AgtCANtfctnStsAdvc(self):
			del self._AgtCANtfctnStsAdvc
			self._AgtCANtfctnStsAdvc = base_types.UninitialisedField(self, 'AgtCANtfctnStsAdvc', AgentCANotificationStatusAdviceV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCANtfctnStsAdvc', type=AgentCANotificationStatusAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))