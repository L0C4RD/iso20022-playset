from . import base_types
import InquiryInitiationV03

class CAIN_016_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NqryInitn"]
		@property
		def NqryInitn(self):
			return self._NqryInitn

		@NqryInitn.setter
		def NqryInitn(self, value):
			self._NqryInitn = value if type(value) != auto else self.make_default("NqryInitn")

		@NqryInitn.deleter
		def NqryInitn(self):
			del self._NqryInitn
			self._NqryInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NqryInitn', type=InquiryInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))

