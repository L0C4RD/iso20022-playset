# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingNonExtensionNotificationV01 import UndertakingNonExtensionNotificationV01

class TSRV_011_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsrv.011.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_UdrtkgNonXtnsnNtfctn"]
		@property
		def UdrtkgNonXtnsnNtfctn(self):
			return self._UdrtkgNonXtnsnNtfctn

		@UdrtkgNonXtnsnNtfctn.setter
		def UdrtkgNonXtnsnNtfctn(self, value):
			self._UdrtkgNonXtnsnNtfctn = value if type(value) != base_types.auto else self.make_default("UdrtkgNonXtnsnNtfctn")

		@UdrtkgNonXtnsnNtfctn.deleter
		def UdrtkgNonXtnsnNtfctn(self):
			del self._UdrtkgNonXtnsnNtfctn
			self._UdrtkgNonXtnsnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgNonXtnsnNtfctn', type=UndertakingNonExtensionNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))