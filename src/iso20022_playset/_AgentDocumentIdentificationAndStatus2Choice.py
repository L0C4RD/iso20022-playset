from . import base_types
from ._AgentNotificationCancellationIdentificationAndStatus2 import AgentNotificationCancellationIdentificationAndStatus2
from ._AgentNotificationIdentificationAndStatus2 import AgentNotificationIdentificationAndStatus2

class AgentDocumentIdentificationAndStatus2Choice(base_types._BaseFieldType):

	__slots__ = ["_AgtCANtfctnAdvcIdAndSts", "_AgtCANtfctnCxlReqIdAndSts"]
	@property
	def AgtCANtfctnAdvcIdAndSts(self):
		return self._AgtCANtfctnAdvcIdAndSts

	@AgtCANtfctnAdvcIdAndSts.setter
	def AgtCANtfctnAdvcIdAndSts(self, value):
		self._AgtCANtfctnAdvcIdAndSts = value if type(value) != base_types.auto else self.make_default("AgtCANtfctnAdvcIdAndSts")

	@AgtCANtfctnAdvcIdAndSts.deleter
	def AgtCANtfctnAdvcIdAndSts(self):
		del self._AgtCANtfctnAdvcIdAndSts
		self._AgtCANtfctnAdvcIdAndSts = None

	@property
	def AgtCANtfctnCxlReqIdAndSts(self):
		return self._AgtCANtfctnCxlReqIdAndSts

	@AgtCANtfctnCxlReqIdAndSts.setter
	def AgtCANtfctnCxlReqIdAndSts(self, value):
		self._AgtCANtfctnCxlReqIdAndSts = value if type(value) != base_types.auto else self.make_default("AgtCANtfctnCxlReqIdAndSts")

	@AgtCANtfctnCxlReqIdAndSts.deleter
	def AgtCANtfctnCxlReqIdAndSts(self):
		del self._AgtCANtfctnCxlReqIdAndSts
		self._AgtCANtfctnCxlReqIdAndSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCANtfctnAdvcIdAndSts', type=AgentNotificationIdentificationAndStatus2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCANtfctnCxlReqIdAndSts', type=AgentNotificationCancellationIdentificationAndStatus2, min=0, max=1, mutex_group=1, array=False),
	))

