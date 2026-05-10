from . import base_types
from ._NotificationToReceiveCancellationAdviceV09 import NotificationToReceiveCancellationAdviceV09

class CAMT_058_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NtfctnToRcvCxlAdvc"]
		@property
		def NtfctnToRcvCxlAdvc(self):
			return self._NtfctnToRcvCxlAdvc

		@NtfctnToRcvCxlAdvc.setter
		def NtfctnToRcvCxlAdvc(self, value):
			self._NtfctnToRcvCxlAdvc = value if type(value) != base_types.auto else self.make_default("NtfctnToRcvCxlAdvc")

		@NtfctnToRcvCxlAdvc.deleter
		def NtfctnToRcvCxlAdvc(self):
			del self._NtfctnToRcvCxlAdvc
			self._NtfctnToRcvCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnToRcvCxlAdvc', type=NotificationToReceiveCancellationAdviceV09, min=1, max=1, mutex_group=None, array=False),
		))

