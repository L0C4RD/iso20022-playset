from . import base_types
from .ChequePresentmentNotificationV02 import ChequePresentmentNotificationV02

class CAMT_107_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ChqPresntmntNtfctn"]
		@property
		def ChqPresntmntNtfctn(self):
			return self._ChqPresntmntNtfctn

		@ChqPresntmntNtfctn.setter
		def ChqPresntmntNtfctn(self, value):
			self._ChqPresntmntNtfctn = value if type(value) != base_types.auto else self.make_default("ChqPresntmntNtfctn")

		@ChqPresntmntNtfctn.deleter
		def ChqPresntmntNtfctn(self):
			del self._ChqPresntmntNtfctn
			self._ChqPresntmntNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChqPresntmntNtfctn', type=ChequePresentmentNotificationV02, min=1, max=1, mutex_group=None, array=False),
		))

