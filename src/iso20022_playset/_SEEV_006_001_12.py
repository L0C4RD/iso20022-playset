# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MeetingInstructionStatusV12 import MeetingInstructionStatusV12

class SEEV_006_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgInstrSts"]
		@property
		def MtgInstrSts(self):
			return self._MtgInstrSts

		@MtgInstrSts.setter
		def MtgInstrSts(self, value):
			self._MtgInstrSts = value if type(value) != base_types.auto else self.make_default("MtgInstrSts")

		@MtgInstrSts.deleter
		def MtgInstrSts(self):
			del self._MtgInstrSts
			self._MtgInstrSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgInstrSts', type=MeetingInstructionStatusV12, min=1, max=1, mutex_group=None, array=False),
		))