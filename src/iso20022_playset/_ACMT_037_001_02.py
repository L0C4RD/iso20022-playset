# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchTechnicalRejectionV02 import AccountSwitchTechnicalRejectionV02

class ACMT_037_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.037.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctSwtchTechRjctn"]
		@property
		def AcctSwtchTechRjctn(self):
			return self._AcctSwtchTechRjctn

		@AcctSwtchTechRjctn.setter
		def AcctSwtchTechRjctn(self, value):
			self._AcctSwtchTechRjctn = value if type(value) != base_types.auto else self.make_default("AcctSwtchTechRjctn")

		@AcctSwtchTechRjctn.deleter
		def AcctSwtchTechRjctn(self):
			del self._AcctSwtchTechRjctn
			self._AcctSwtchTechRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchTechRjctn', type=AccountSwitchTechnicalRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))