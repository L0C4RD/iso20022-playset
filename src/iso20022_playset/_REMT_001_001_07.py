from . import base_types
from ._RemittanceAdviceV07 import RemittanceAdviceV07

class REMT_001_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RmtAdvc"]
		@property
		def RmtAdvc(self):
			return self._RmtAdvc

		@RmtAdvc.setter
		def RmtAdvc(self, value):
			self._RmtAdvc = value if type(value) != base_types.auto else self.make_default("RmtAdvc")

		@RmtAdvc.deleter
		def RmtAdvc(self):
			del self._RmtAdvc
			self._RmtAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RmtAdvc', type=RemittanceAdviceV07, min=1, max=1, mutex_group=None, array=False),
		))

