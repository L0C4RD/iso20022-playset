from . import base_types
import AgentCAElectionAdviceV01

class SEEV_012_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAElctnAdvc"]
		@property
		def AgtCAElctnAdvc(self):
			return self._AgtCAElctnAdvc

		@AgtCAElctnAdvc.setter
		def AgtCAElctnAdvc(self, value):
			self._AgtCAElctnAdvc = value if type(value) != auto else self.make_default("AgtCAElctnAdvc")

		@AgtCAElctnAdvc.deleter
		def AgtCAElctnAdvc(self):
			del self._AgtCAElctnAdvc
			self._AgtCAElctnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnAdvc', type=AgentCAElectionAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

