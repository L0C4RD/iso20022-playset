# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RoleAndBaselineAcceptanceNotificationV01 import RoleAndBaselineAcceptanceNotificationV01

class TSMT_051_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.051.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_RoleAndBaselnAccptncNtfctn"]
		@property
		def RoleAndBaselnAccptncNtfctn(self):
			return self._RoleAndBaselnAccptncNtfctn

		@RoleAndBaselnAccptncNtfctn.setter
		def RoleAndBaselnAccptncNtfctn(self, value):
			self._RoleAndBaselnAccptncNtfctn = value if type(value) != base_types.auto else self.make_default("RoleAndBaselnAccptncNtfctn")

		@RoleAndBaselnAccptncNtfctn.deleter
		def RoleAndBaselnAccptncNtfctn(self):
			del self._RoleAndBaselnAccptncNtfctn
			self._RoleAndBaselnAccptncNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnAccptncNtfctn', type=RoleAndBaselineAcceptanceNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))