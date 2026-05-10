from . import base_types
import RemittanceLocationAdviceV03

class REMT_002_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RmtLctnAdvc"]
		@property
		def RmtLctnAdvc(self):
			return self._RmtLctnAdvc

		@RmtLctnAdvc.setter
		def RmtLctnAdvc(self, value):
			self._RmtLctnAdvc = value if type(value) != auto else self.make_default("RmtLctnAdvc")

		@RmtLctnAdvc.deleter
		def RmtLctnAdvc(self):
			del self._RmtLctnAdvc
			self._RmtLctnAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RmtLctnAdvc', type=RemittanceLocationAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))

