from . import base_types
import StatusExtensionRequestV03

class TSMT_035_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsXtnsnReq"]
		@property
		def StsXtnsnReq(self):
			return self._StsXtnsnReq

		@StsXtnsnReq.setter
		def StsXtnsnReq(self, value):
			self._StsXtnsnReq = value if type(value) != auto else self.make_default("StsXtnsnReq")

		@StsXtnsnReq.deleter
		def StsXtnsnReq(self):
			del self._StsXtnsnReq
			self._StsXtnsnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnReq', type=StatusExtensionRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

