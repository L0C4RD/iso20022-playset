from . import base_types
import StatusChangeRequestV02

class TSMT_026_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsChngReq"]
		@property
		def StsChngReq(self):
			return self._StsChngReq

		@StsChngReq.setter
		def StsChngReq(self, value):
			self._StsChngReq = value if type(value) != auto else self.make_default("StsChngReq")

		@StsChngReq.deleter
		def StsChngReq(self):
			del self._StsChngReq
			self._StsChngReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReq', type=StatusChangeRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

