# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCANotificationAdviceV02 import AgentCANotificationAdviceV02

class SEEV_009_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCANtfctnAdvc"]
		@property
		def AgtCANtfctnAdvc(self):
			return self._AgtCANtfctnAdvc

		@AgtCANtfctnAdvc.setter
		def AgtCANtfctnAdvc(self, value):
			self._AgtCANtfctnAdvc = value if type(value) != base_types.auto else self.make_default("AgtCANtfctnAdvc")

		@AgtCANtfctnAdvc.deleter
		def AgtCANtfctnAdvc(self):
			del self._AgtCANtfctnAdvc
			self._AgtCANtfctnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCANtfctnAdvc', type=AgentCANotificationAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))