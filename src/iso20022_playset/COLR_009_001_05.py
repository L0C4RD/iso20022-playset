from . import base_types
from .MarginCallDisputeNotificationV05 import MarginCallDisputeNotificationV05

class COLR_009_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MrgnCallDsptNtfctn"]
		@property
		def MrgnCallDsptNtfctn(self):
			return self._MrgnCallDsptNtfctn

		@MrgnCallDsptNtfctn.setter
		def MrgnCallDsptNtfctn(self, value):
			self._MrgnCallDsptNtfctn = value if type(value) != base_types.auto else self.make_default("MrgnCallDsptNtfctn")

		@MrgnCallDsptNtfctn.deleter
		def MrgnCallDsptNtfctn(self):
			del self._MrgnCallDsptNtfctn
			self._MrgnCallDsptNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnCallDsptNtfctn', type=MarginCallDisputeNotificationV05, min=1, max=1, mutex_group=None, array=False),
		))

