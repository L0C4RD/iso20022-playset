# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentNotificationCancellationIdentificationAndStatus1
from . import AgentNotificationIdentificationAndStatus1

class AgentDocumentIdentificationAndStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_AgtCANtfctnAdvcIdAndSts", "_AgtCANtfctnCxlReqIdAndSts"]
	@property
	def AgtCANtfctnAdvcIdAndSts(self):
		return self._AgtCANtfctnAdvcIdAndSts

	@AgtCANtfctnAdvcIdAndSts.setter
	def AgtCANtfctnAdvcIdAndSts(self, value):
		self._AgtCANtfctnAdvcIdAndSts = value if value is not None else base_types.UninitialisedField(self, 'AgtCANtfctnAdvcIdAndSts', AgentNotificationIdentificationAndStatus1, False)

	@AgtCANtfctnAdvcIdAndSts.deleter
	def AgtCANtfctnAdvcIdAndSts(self):
		del self._AgtCANtfctnAdvcIdAndSts
		self._AgtCANtfctnAdvcIdAndSts = base_types.UninitialisedField(self, 'AgtCANtfctnAdvcIdAndSts', AgentNotificationIdentificationAndStatus1, False)

	@property
	def AgtCANtfctnCxlReqIdAndSts(self):
		return self._AgtCANtfctnCxlReqIdAndSts

	@AgtCANtfctnCxlReqIdAndSts.setter
	def AgtCANtfctnCxlReqIdAndSts(self, value):
		self._AgtCANtfctnCxlReqIdAndSts = value if value is not None else base_types.UninitialisedField(self, 'AgtCANtfctnCxlReqIdAndSts', AgentNotificationCancellationIdentificationAndStatus1, False)

	@AgtCANtfctnCxlReqIdAndSts.deleter
	def AgtCANtfctnCxlReqIdAndSts(self):
		del self._AgtCANtfctnCxlReqIdAndSts
		self._AgtCANtfctnCxlReqIdAndSts = base_types.UninitialisedField(self, 'AgtCANtfctnCxlReqIdAndSts', AgentNotificationCancellationIdentificationAndStatus1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCANtfctnAdvcIdAndSts', type=AgentNotificationIdentificationAndStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AgtCANtfctnCxlReqIdAndSts', type=AgentNotificationCancellationIdentificationAndStatus1, min=0, max=1, mutex_group=1, array=False),
	))