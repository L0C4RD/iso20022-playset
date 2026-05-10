from . import base_types
from .SpecialNotificationV01 import SpecialNotificationV01

class TSMT_048_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SpclNtfctn"]
		@property
		def SpclNtfctn(self):
			return self._SpclNtfctn

		@SpclNtfctn.setter
		def SpclNtfctn(self, value):
			self._SpclNtfctn = value if type(value) != base_types.auto else self.make_default("SpclNtfctn")

		@SpclNtfctn.deleter
		def SpclNtfctn(self):
			del self._SpclNtfctn
			self._SpclNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SpclNtfctn', type=SpecialNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

