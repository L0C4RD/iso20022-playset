from . import base_types
import SystemEventNotificationV02

class ADMI_004_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SysEvtNtfctn"]
		@property
		def SysEvtNtfctn(self):
			return self._SysEvtNtfctn

		@SysEvtNtfctn.setter
		def SysEvtNtfctn(self, value):
			self._SysEvtNtfctn = value if type(value) != auto else self.make_default("SysEvtNtfctn")

		@SysEvtNtfctn.deleter
		def SysEvtNtfctn(self):
			del self._SysEvtNtfctn
			self._SysEvtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SysEvtNtfctn', type=SystemEventNotificationV02, min=1, max=1, mutex_group=None, array=False),
		))

