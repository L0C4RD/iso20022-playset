# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusExtensionNotificationV03 import StatusExtensionNotificationV03

class TSMT_032_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.032.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_StsXtnsnNtfctn"]
		@property
		def StsXtnsnNtfctn(self):
			return self._StsXtnsnNtfctn

		@StsXtnsnNtfctn.setter
		def StsXtnsnNtfctn(self, value):
			self._StsXtnsnNtfctn = value if type(value) != base_types.auto else self.make_default("StsXtnsnNtfctn")

		@StsXtnsnNtfctn.deleter
		def StsXtnsnNtfctn(self):
			del self._StsXtnsnNtfctn
			self._StsXtnsnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnNtfctn', type=StatusExtensionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))