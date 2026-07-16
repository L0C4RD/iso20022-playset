# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RoleAndBaselineAcceptanceNotificationV01

class TSMT_051_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.051.001.01"
		_docname = "tsmt.051.001.01"

		__slots__ = ["_RoleAndBaselnAccptncNtfctn"]
		@property
		def RoleAndBaselnAccptncNtfctn(self):
			return self._RoleAndBaselnAccptncNtfctn

		@RoleAndBaselnAccptncNtfctn.setter
		def RoleAndBaselnAccptncNtfctn(self, value):
			self._RoleAndBaselnAccptncNtfctn = value if value is not None else base_types.UninitialisedField(self, 'RoleAndBaselnAccptncNtfctn', RoleAndBaselineAcceptanceNotificationV01, False)

		@RoleAndBaselnAccptncNtfctn.deleter
		def RoleAndBaselnAccptncNtfctn(self):
			del self._RoleAndBaselnAccptncNtfctn
			self._RoleAndBaselnAccptncNtfctn = base_types.UninitialisedField(self, 'RoleAndBaselnAccptncNtfctn', RoleAndBaselineAcceptanceNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnAccptncNtfctn', type=RoleAndBaselineAcceptanceNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))