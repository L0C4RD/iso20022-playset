# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCANotificationCancellationRequestV01 import AgentCANotificationCancellationRequestV01

class SEEV_010_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCANtfctnCxlReq"]
		@property
		def AgtCANtfctnCxlReq(self):
			return self._AgtCANtfctnCxlReq

		@AgtCANtfctnCxlReq.setter
		def AgtCANtfctnCxlReq(self, value):
			self._AgtCANtfctnCxlReq = value if type(value) != base_types.auto else self.make_default("AgtCANtfctnCxlReq")

		@AgtCANtfctnCxlReq.deleter
		def AgtCANtfctnCxlReq(self):
			del self._AgtCANtfctnCxlReq
			self._AgtCANtfctnCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCANtfctnCxlReq', type=AgentCANotificationCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))