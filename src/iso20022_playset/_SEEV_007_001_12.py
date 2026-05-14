from . import base_types
from ._MeetingVoteExecutionConfirmationV12 import MeetingVoteExecutionConfirmationV12

class SEEV_007_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgVoteExctnConf"]
		@property
		def MtgVoteExctnConf(self):
			return self._MtgVoteExctnConf

		@MtgVoteExctnConf.setter
		def MtgVoteExctnConf(self, value):
			self._MtgVoteExctnConf = value if type(value) != base_types.auto else self.make_default("MtgVoteExctnConf")

		@MtgVoteExctnConf.deleter
		def MtgVoteExctnConf(self):
			del self._MtgVoteExctnConf
			self._MtgVoteExctnConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgVoteExctnConf', type=MeetingVoteExecutionConfirmationV12, min=1, max=1, mutex_group=None, array=False),
		))

