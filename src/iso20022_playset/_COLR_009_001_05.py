# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginCallDisputeNotificationV05

class COLR_009_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.009.001.05"
		_docname = "colr.009.001.05"

		__slots__ = ["_MrgnCallDsptNtfctn"]
		@property
		def MrgnCallDsptNtfctn(self):
			return self._MrgnCallDsptNtfctn

		@MrgnCallDsptNtfctn.setter
		def MrgnCallDsptNtfctn(self, value):
			self._MrgnCallDsptNtfctn = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallDsptNtfctn', MarginCallDisputeNotificationV05, False)

		@MrgnCallDsptNtfctn.deleter
		def MrgnCallDsptNtfctn(self):
			del self._MrgnCallDsptNtfctn
			self._MrgnCallDsptNtfctn = base_types.UninitialisedField(self, 'MrgnCallDsptNtfctn', MarginCallDisputeNotificationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnCallDsptNtfctn', type=MarginCallDisputeNotificationV05, min=1, max=1, mutex_group=None, array=False),
		))