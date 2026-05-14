from . import base_types
from ._SaleToPOIEventNotificationV08 import SaleToPOIEventNotificationV08

class CASP_012_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIEvtNtfctn"]
		@property
		def SaleToPOIEvtNtfctn(self):
			return self._SaleToPOIEvtNtfctn

		@SaleToPOIEvtNtfctn.setter
		def SaleToPOIEvtNtfctn(self, value):
			self._SaleToPOIEvtNtfctn = value if type(value) != base_types.auto else self.make_default("SaleToPOIEvtNtfctn")

		@SaleToPOIEvtNtfctn.deleter
		def SaleToPOIEvtNtfctn(self):
			del self._SaleToPOIEvtNtfctn
			self._SaleToPOIEvtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIEvtNtfctn', type=SaleToPOIEventNotificationV08, min=1, max=1, mutex_group=None, array=False),
		))

