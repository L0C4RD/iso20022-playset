# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._UndertakingIssuanceNotificationV01 import UndertakingIssuanceNotificationV01

class TSRV_003_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_UdrtkgIssncNtfctn"]
		@property
		def UdrtkgIssncNtfctn(self):
			return self._UdrtkgIssncNtfctn

		@UdrtkgIssncNtfctn.setter
		def UdrtkgIssncNtfctn(self, value):
			self._UdrtkgIssncNtfctn = value if type(value) != base_types.auto else self.make_default("UdrtkgIssncNtfctn")

		@UdrtkgIssncNtfctn.deleter
		def UdrtkgIssncNtfctn(self):
			del self._UdrtkgIssncNtfctn
			self._UdrtkgIssncNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgIssncNtfctn', type=UndertakingIssuanceNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))