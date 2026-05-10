from . import base_types
from ._StatusExtensionRequestRejectionV03 import StatusExtensionRequestRejectionV03

class TSMT_033_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsXtnsnReqRjctn"]
		@property
		def StsXtnsnReqRjctn(self):
			return self._StsXtnsnReqRjctn

		@StsXtnsnReqRjctn.setter
		def StsXtnsnReqRjctn(self, value):
			self._StsXtnsnReqRjctn = value if type(value) != base_types.auto else self.make_default("StsXtnsnReqRjctn")

		@StsXtnsnReqRjctn.deleter
		def StsXtnsnReqRjctn(self):
			del self._StsXtnsnReqRjctn
			self._StsXtnsnReqRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnReqRjctn', type=StatusExtensionRequestRejectionV03, min=1, max=1, mutex_group=None, array=False),
		))

