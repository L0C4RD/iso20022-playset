# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvestigationResponseV02 import InvestigationResponseV02

class CAMT_111_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.111.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_InvstgtnRspn"]
		@property
		def InvstgtnRspn(self):
			return self._InvstgtnRspn

		@InvstgtnRspn.setter
		def InvstgtnRspn(self, value):
			self._InvstgtnRspn = value if type(value) != base_types.auto else self.make_default("InvstgtnRspn")

		@InvstgtnRspn.deleter
		def InvstgtnRspn(self):
			del self._InvstgtnRspn
			self._InvstgtnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvstgtnRspn', type=InvestigationResponseV02, min=1, max=1, mutex_group=None, array=False),
		))