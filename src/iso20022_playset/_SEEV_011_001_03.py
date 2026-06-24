# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCANotificationStatusAdviceV03 import AgentCANotificationStatusAdviceV03

class SEEV_011_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.011.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AgtCANtfctnStsAdvc"]
		@property
		def AgtCANtfctnStsAdvc(self):
			return self._AgtCANtfctnStsAdvc

		@AgtCANtfctnStsAdvc.setter
		def AgtCANtfctnStsAdvc(self, value):
			self._AgtCANtfctnStsAdvc = value if type(value) != base_types.auto else self.make_default("AgtCANtfctnStsAdvc")

		@AgtCANtfctnStsAdvc.deleter
		def AgtCANtfctnStsAdvc(self):
			del self._AgtCANtfctnStsAdvc
			self._AgtCANtfctnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCANtfctnStsAdvc', type=AgentCANotificationStatusAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))