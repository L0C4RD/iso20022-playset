import base_types
import StatusChangeRequestAcceptanceV02

class TSMT_027_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsChngReqAccptnc"]
		@property
		def StsChngReqAccptnc(self):
			return self._StsChngReqAccptnc

		@StsChngReqAccptnc.setter
		def StsChngReqAccptnc(self, value):
			self._StsChngReqAccptnc = value if type(value) != auto else self.make_default("StsChngReqAccptnc")

		@StsChngReqAccptnc.deleter
		def StsChngReqAccptnc(self):
			del self._StsChngReqAccptnc
			self._StsChngReqAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqAccptnc', type=StatusChangeRequestAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))

