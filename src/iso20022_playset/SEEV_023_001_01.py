import base_types
import AgentCAInformationAdviceV01

class SEEV_023_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAInfAdvc"]
		@property
		def AgtCAInfAdvc(self):
			return self._AgtCAInfAdvc

		@AgtCAInfAdvc.setter
		def AgtCAInfAdvc(self, value):
			self._AgtCAInfAdvc = value if type(value) != auto else self.make_default("AgtCAInfAdvc")

		@AgtCAInfAdvc.deleter
		def AgtCAInfAdvc(self):
			del self._AgtCAInfAdvc
			self._AgtCAInfAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAInfAdvc', type=AgentCAInformationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

