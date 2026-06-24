# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MarginCallDisputeNotificationV05 import MarginCallDisputeNotificationV05

class COLR_009_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.009.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

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