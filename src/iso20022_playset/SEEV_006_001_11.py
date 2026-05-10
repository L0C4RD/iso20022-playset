from . import base_types
from .MeetingInstructionStatusV11 import MeetingInstructionStatusV11

class SEEV_006_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgInstrSts"]
		@property
		def MtgInstrSts(self):
			return self._MtgInstrSts

		@MtgInstrSts.setter
		def MtgInstrSts(self, value):
			self._MtgInstrSts = value if type(value) != auto else self.make_default("MtgInstrSts")

		@MtgInstrSts.deleter
		def MtgInstrSts(self):
			del self._MtgInstrSts
			self._MtgInstrSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgInstrSts', type=MeetingInstructionStatusV11, min=1, max=1, mutex_group=None, array=False),
		))

