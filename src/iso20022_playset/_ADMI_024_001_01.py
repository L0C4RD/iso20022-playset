from . import base_types
from ._NotificationOfCorrespondenceV01 import NotificationOfCorrespondenceV01

class ADMI_024_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NtfctnOfCrspdc"]
		@property
		def NtfctnOfCrspdc(self):
			return self._NtfctnOfCrspdc

		@NtfctnOfCrspdc.setter
		def NtfctnOfCrspdc(self, value):
			self._NtfctnOfCrspdc = value if type(value) != base_types.auto else self.make_default("NtfctnOfCrspdc")

		@NtfctnOfCrspdc.deleter
		def NtfctnOfCrspdc(self):
			del self._NtfctnOfCrspdc
			self._NtfctnOfCrspdc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtfctnOfCrspdc', type=NotificationOfCorrespondenceV01, min=1, max=1, mutex_group=None, array=False),
		))

