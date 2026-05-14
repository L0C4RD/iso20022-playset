# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SystemEventAcknowledgementV01 import SystemEventAcknowledgementV01

class ADMI_011_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SysEvtAck"]
		@property
		def SysEvtAck(self):
			return self._SysEvtAck

		@SysEvtAck.setter
		def SysEvtAck(self, value):
			self._SysEvtAck = value if type(value) != base_types.auto else self.make_default("SysEvtAck")

		@SysEvtAck.deleter
		def SysEvtAck(self):
			del self._SysEvtAck
			self._SysEvtAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SysEvtAck', type=SystemEventAcknowledgementV01, min=1, max=1, mutex_group=None, array=False),
		))