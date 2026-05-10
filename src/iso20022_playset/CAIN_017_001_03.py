from . import base_types
from .InquiryResponseV03 import InquiryResponseV03

class CAIN_017_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NqryRspn"]
		@property
		def NqryRspn(self):
			return self._NqryRspn

		@NqryRspn.setter
		def NqryRspn(self, value):
			self._NqryRspn = value if type(value) != auto else self.make_default("NqryRspn")

		@NqryRspn.deleter
		def NqryRspn(self):
			del self._NqryRspn
			self._NqryRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NqryRspn', type=InquiryResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

