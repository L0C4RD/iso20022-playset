from . import base_types
from ._MeetingEntitlementNotificationV10 import MeetingEntitlementNotificationV10

class SEEV_003_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgEntitlmntNtfctn"]
		@property
		def MtgEntitlmntNtfctn(self):
			return self._MtgEntitlmntNtfctn

		@MtgEntitlmntNtfctn.setter
		def MtgEntitlmntNtfctn(self, value):
			self._MtgEntitlmntNtfctn = value if type(value) != base_types.auto else self.make_default("MtgEntitlmntNtfctn")

		@MtgEntitlmntNtfctn.deleter
		def MtgEntitlmntNtfctn(self):
			del self._MtgEntitlmntNtfctn
			self._MtgEntitlmntNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgEntitlmntNtfctn', type=MeetingEntitlementNotificationV10, min=1, max=1, mutex_group=None, array=False),
		))

