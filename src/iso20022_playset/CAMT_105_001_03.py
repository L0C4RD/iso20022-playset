from . import base_types
import ChargesPaymentNotificationV03

class CAMT_105_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ChrgsPmtNtfctn"]
		@property
		def ChrgsPmtNtfctn(self):
			return self._ChrgsPmtNtfctn

		@ChrgsPmtNtfctn.setter
		def ChrgsPmtNtfctn(self, value):
			self._ChrgsPmtNtfctn = value if type(value) != auto else self.make_default("ChrgsPmtNtfctn")

		@ChrgsPmtNtfctn.deleter
		def ChrgsPmtNtfctn(self):
			del self._ChrgsPmtNtfctn
			self._ChrgsPmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgsPmtNtfctn', type=ChargesPaymentNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

