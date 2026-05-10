from . import base_types
import AgentCADeactivationStatusAdviceV01

class SEEV_030_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AgtCADeactvtnStsAdvc"]
		@property
		def AgtCADeactvtnStsAdvc(self):
			return self._AgtCADeactvtnStsAdvc

		@AgtCADeactvtnStsAdvc.setter
		def AgtCADeactvtnStsAdvc(self, value):
			self._AgtCADeactvtnStsAdvc = value if type(value) != auto else self.make_default("AgtCADeactvtnStsAdvc")

		@AgtCADeactvtnStsAdvc.deleter
		def AgtCADeactvtnStsAdvc(self):
			del self._AgtCADeactvtnStsAdvc
			self._AgtCADeactvtnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADeactvtnStsAdvc', type=AgentCADeactivationStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

