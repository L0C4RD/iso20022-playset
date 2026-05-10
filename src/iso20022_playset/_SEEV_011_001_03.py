from . import base_types
from ._AgentCANotificationStatusAdviceV03 import AgentCANotificationStatusAdviceV03

class SEEV_011_001_03():

	class Document(base_types._BaseFieldType):

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

