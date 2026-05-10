from . import base_types
from .SaleToPOIEventNotificationV07 import SaleToPOIEventNotificationV07

class CASP_012_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SaleToPOIEvtNtfctn"]
		@property
		def SaleToPOIEvtNtfctn(self):
			return self._SaleToPOIEvtNtfctn

		@SaleToPOIEvtNtfctn.setter
		def SaleToPOIEvtNtfctn(self, value):
			self._SaleToPOIEvtNtfctn = value if type(value) != auto else self.make_default("SaleToPOIEvtNtfctn")

		@SaleToPOIEvtNtfctn.deleter
		def SaleToPOIEvtNtfctn(self):
			del self._SaleToPOIEvtNtfctn
			self._SaleToPOIEvtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIEvtNtfctn', type=SaleToPOIEventNotificationV07, min=1, max=1, mutex_group=None, array=False),
		))

