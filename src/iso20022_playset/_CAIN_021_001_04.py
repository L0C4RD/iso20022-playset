from . import base_types
from ._RetrievalInitiationV04 import RetrievalInitiationV04

class CAIN_021_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrvlInitn"]
		@property
		def RtrvlInitn(self):
			return self._RtrvlInitn

		@RtrvlInitn.setter
		def RtrvlInitn(self, value):
			self._RtrvlInitn = value if type(value) != base_types.auto else self.make_default("RtrvlInitn")

		@RtrvlInitn.deleter
		def RtrvlInitn(self):
			del self._RtrvlInitn
			self._RtrvlInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrvlInitn', type=RetrievalInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))

