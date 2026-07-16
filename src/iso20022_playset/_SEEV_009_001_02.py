# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCANotificationAdviceV02

class SEEV_009_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.009.001.02"
		_docname = "seev.009.001.02"

		__slots__ = ["_AgtCANtfctnAdvc"]
		@property
		def AgtCANtfctnAdvc(self):
			return self._AgtCANtfctnAdvc

		@AgtCANtfctnAdvc.setter
		def AgtCANtfctnAdvc(self, value):
			self._AgtCANtfctnAdvc = value if value is not None else base_types.UninitialisedField(self, 'AgtCANtfctnAdvc', AgentCANotificationAdviceV02, False)

		@AgtCANtfctnAdvc.deleter
		def AgtCANtfctnAdvc(self):
			del self._AgtCANtfctnAdvc
			self._AgtCANtfctnAdvc = base_types.UninitialisedField(self, 'AgtCANtfctnAdvc', AgentCANotificationAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCANtfctnAdvc', type=AgentCANotificationAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))