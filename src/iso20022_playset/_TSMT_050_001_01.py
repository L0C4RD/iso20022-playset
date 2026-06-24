# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RoleAndBaselineRejectionV01 import RoleAndBaselineRejectionV01

class TSMT_050_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.050.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_RoleAndBaselnRjctn"]
		@property
		def RoleAndBaselnRjctn(self):
			return self._RoleAndBaselnRjctn

		@RoleAndBaselnRjctn.setter
		def RoleAndBaselnRjctn(self, value):
			self._RoleAndBaselnRjctn = value if type(value) != base_types.auto else self.make_default("RoleAndBaselnRjctn")

		@RoleAndBaselnRjctn.deleter
		def RoleAndBaselnRjctn(self):
			del self._RoleAndBaselnRjctn
			self._RoleAndBaselnRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RoleAndBaselnRjctn', type=RoleAndBaselineRejectionV01, min=1, max=1, mutex_group=None, array=False),
		))