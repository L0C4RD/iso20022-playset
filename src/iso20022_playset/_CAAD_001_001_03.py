# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BatchManagementInitiationV03 import BatchManagementInitiationV03

class CAAD_001_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caad.001.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_BtchMgmtInitn"]
		@property
		def BtchMgmtInitn(self):
			return self._BtchMgmtInitn

		@BtchMgmtInitn.setter
		def BtchMgmtInitn(self, value):
			self._BtchMgmtInitn = value if type(value) != base_types.auto else self.make_default("BtchMgmtInitn")

		@BtchMgmtInitn.deleter
		def BtchMgmtInitn(self):
			del self._BtchMgmtInitn
			self._BtchMgmtInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchMgmtInitn', type=BatchManagementInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))