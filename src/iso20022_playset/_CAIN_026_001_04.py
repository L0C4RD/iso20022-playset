from . import base_types
from ._AddendumResponseV04 import AddendumResponseV04

class CAIN_026_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AdddmRspn"]
		@property
		def AdddmRspn(self):
			return self._AdddmRspn

		@AdddmRspn.setter
		def AdddmRspn(self, value):
			self._AdddmRspn = value if type(value) != base_types.auto else self.make_default("AdddmRspn")

		@AdddmRspn.deleter
		def AdddmRspn(self):
			del self._AdddmRspn
			self._AdddmRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdddmRspn', type=AddendumResponseV04, min=1, max=1, mutex_group=None, array=False),
		))

