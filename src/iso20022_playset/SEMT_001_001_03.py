from . import base_types
from .SecuritiesMessageRejectionV03 import SecuritiesMessageRejectionV03

class SEMT_001_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesMsgRjctn"]
		@property
		def SctiesMsgRjctn(self):
			return self._SctiesMsgRjctn

		@SctiesMsgRjctn.setter
		def SctiesMsgRjctn(self, value):
			self._SctiesMsgRjctn = value if type(value) != auto else self.make_default("SctiesMsgRjctn")

		@SctiesMsgRjctn.deleter
		def SctiesMsgRjctn(self):
			del self._SctiesMsgRjctn
			self._SctiesMsgRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesMsgRjctn', type=SecuritiesMessageRejectionV03, min=1, max=1, mutex_group=None, array=False),
		))

