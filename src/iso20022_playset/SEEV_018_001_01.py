from . import base_types
import AgentCAGlobalDistributionStatusAdviceV01

class SEEV_018_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCAGblDstrbtnStsAdvc"]
		@property
		def AgtCAGblDstrbtnStsAdvc(self):
			return self._AgtCAGblDstrbtnStsAdvc

		@AgtCAGblDstrbtnStsAdvc.setter
		def AgtCAGblDstrbtnStsAdvc(self, value):
			self._AgtCAGblDstrbtnStsAdvc = value if type(value) != auto else self.make_default("AgtCAGblDstrbtnStsAdvc")

		@AgtCAGblDstrbtnStsAdvc.deleter
		def AgtCAGblDstrbtnStsAdvc(self):
			del self._AgtCAGblDstrbtnStsAdvc
			self._AgtCAGblDstrbtnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAGblDstrbtnStsAdvc', type=AgentCAGlobalDistributionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

