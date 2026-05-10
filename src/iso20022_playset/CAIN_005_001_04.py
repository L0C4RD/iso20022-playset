from . import base_types
import ReversalInitiationV04

class CAIN_005_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RvslInitn"]
		@property
		def RvslInitn(self):
			return self._RvslInitn

		@RvslInitn.setter
		def RvslInitn(self, value):
			self._RvslInitn = value if type(value) != auto else self.make_default("RvslInitn")

		@RvslInitn.deleter
		def RvslInitn(self):
			del self._RvslInitn
			self._RvslInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslInitn', type=ReversalInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))

