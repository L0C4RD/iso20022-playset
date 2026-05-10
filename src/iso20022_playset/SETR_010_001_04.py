from . import base_types
from .SubscriptionOrderV04 import SubscriptionOrderV04

class SETR_010_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptOrdr"]
		@property
		def SbcptOrdr(self):
			return self._SbcptOrdr

		@SbcptOrdr.setter
		def SbcptOrdr(self, value):
			self._SbcptOrdr = value if type(value) != auto else self.make_default("SbcptOrdr")

		@SbcptOrdr.deleter
		def SbcptOrdr(self):
			del self._SbcptOrdr
			self._SbcptOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdr', type=SubscriptionOrderV04, min=1, max=1, mutex_group=None, array=False),
		))

