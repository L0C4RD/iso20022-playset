from . import base_types
import AgentCANotificationAdviceV02

class SEEV_009_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCANtfctnAdvc"]
		@property
		def AgtCANtfctnAdvc(self):
			return self._AgtCANtfctnAdvc

		@AgtCANtfctnAdvc.setter
		def AgtCANtfctnAdvc(self, value):
			self._AgtCANtfctnAdvc = value if type(value) != auto else self.make_default("AgtCANtfctnAdvc")

		@AgtCANtfctnAdvc.deleter
		def AgtCANtfctnAdvc(self):
			del self._AgtCANtfctnAdvc
			self._AgtCANtfctnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCANtfctnAdvc', type=AgentCANotificationAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

