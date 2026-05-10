from . import base_types
from .IntentToPayNotificationV02 import IntentToPayNotificationV02

class TSMT_044_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InttToPayNtfctn"]
		@property
		def InttToPayNtfctn(self):
			return self._InttToPayNtfctn

		@InttToPayNtfctn.setter
		def InttToPayNtfctn(self, value):
			self._InttToPayNtfctn = value if type(value) != base_types.auto else self.make_default("InttToPayNtfctn")

		@InttToPayNtfctn.deleter
		def InttToPayNtfctn(self):
			del self._InttToPayNtfctn
			self._InttToPayNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InttToPayNtfctn', type=IntentToPayNotificationV02, min=1, max=1, mutex_group=None, array=False),
		))

