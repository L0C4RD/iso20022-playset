import base_types
import ExtendOrPayResponseV01

class TSRV_015_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_XtndOrPayRspn"]
		@property
		def XtndOrPayRspn(self):
			return self._XtndOrPayRspn

		@XtndOrPayRspn.setter
		def XtndOrPayRspn(self, value):
			self._XtndOrPayRspn = value if type(value) != auto else self.make_default("XtndOrPayRspn")

		@XtndOrPayRspn.deleter
		def XtndOrPayRspn(self):
			del self._XtndOrPayRspn
			self._XtndOrPayRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='XtndOrPayRspn', type=ExtendOrPayResponseV01, min=1, max=1, mutex_group=None, array=False),
		))

