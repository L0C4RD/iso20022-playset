from . import base_types
import RemittanceAdviceV06

class REMT_001_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RmtAdvc"]
		@property
		def RmtAdvc(self):
			return self._RmtAdvc

		@RmtAdvc.setter
		def RmtAdvc(self, value):
			self._RmtAdvc = value if type(value) != auto else self.make_default("RmtAdvc")

		@RmtAdvc.deleter
		def RmtAdvc(self):
			del self._RmtAdvc
			self._RmtAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RmtAdvc', type=RemittanceAdviceV06, min=1, max=1, mutex_group=None, array=False),
		))

