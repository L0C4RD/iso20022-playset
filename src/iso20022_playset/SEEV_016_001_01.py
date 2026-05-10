from . import base_types
import AgentCADistributionBreakdownAdviceV01

class SEEV_016_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCADstrbtnBrkdwnAdvc"]
		@property
		def AgtCADstrbtnBrkdwnAdvc(self):
			return self._AgtCADstrbtnBrkdwnAdvc

		@AgtCADstrbtnBrkdwnAdvc.setter
		def AgtCADstrbtnBrkdwnAdvc(self, value):
			self._AgtCADstrbtnBrkdwnAdvc = value if type(value) != auto else self.make_default("AgtCADstrbtnBrkdwnAdvc")

		@AgtCADstrbtnBrkdwnAdvc.deleter
		def AgtCADstrbtnBrkdwnAdvc(self):
			del self._AgtCADstrbtnBrkdwnAdvc
			self._AgtCADstrbtnBrkdwnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADstrbtnBrkdwnAdvc', type=AgentCADistributionBreakdownAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

