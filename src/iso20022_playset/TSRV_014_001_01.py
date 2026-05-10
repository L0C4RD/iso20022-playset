from . import base_types
import ExtendOrPayRequestV01

class TSRV_014_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_XtndOrPayReq"]
		@property
		def XtndOrPayReq(self):
			return self._XtndOrPayReq

		@XtndOrPayReq.setter
		def XtndOrPayReq(self, value):
			self._XtndOrPayReq = value if type(value) != auto else self.make_default("XtndOrPayReq")

		@XtndOrPayReq.deleter
		def XtndOrPayReq(self):
			del self._XtndOrPayReq
			self._XtndOrPayReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='XtndOrPayReq', type=ExtendOrPayRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

