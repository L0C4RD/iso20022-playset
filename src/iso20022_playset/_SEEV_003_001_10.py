# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MeetingEntitlementNotificationV10

class SEEV_003_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.003.001.10"
		_docname = "seev.003.001.10"

		__slots__ = ["_MtgEntitlmntNtfctn"]
		@property
		def MtgEntitlmntNtfctn(self):
			return self._MtgEntitlmntNtfctn

		@MtgEntitlmntNtfctn.setter
		def MtgEntitlmntNtfctn(self, value):
			self._MtgEntitlmntNtfctn = value if value is not None else base_types.UninitialisedField(self, 'MtgEntitlmntNtfctn', MeetingEntitlementNotificationV10, False)

		@MtgEntitlmntNtfctn.deleter
		def MtgEntitlmntNtfctn(self):
			del self._MtgEntitlmntNtfctn
			self._MtgEntitlmntNtfctn = base_types.UninitialisedField(self, 'MtgEntitlmntNtfctn', MeetingEntitlementNotificationV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgEntitlmntNtfctn', type=MeetingEntitlementNotificationV10, min=1, max=1, mutex_group=None, array=False),
		))