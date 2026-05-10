import base_types
import SpecialRequestV01

class TSMT_047_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SpclReq"]
		@property
		def SpclReq(self):
			return self._SpclReq

		@SpclReq.setter
		def SpclReq(self, value):
			self._SpclReq = value if type(value) != auto else self.make_default("SpclReq")

		@SpclReq.deleter
		def SpclReq(self):
			del self._SpclReq
			self._SpclReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SpclReq', type=SpecialRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

