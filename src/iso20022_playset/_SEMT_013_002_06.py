# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementInstruction002V06 import IntraPositionMovementInstruction002V06

class SEMT_013_002_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.013.002.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_IntraPosMvmntInstr"]
		@property
		def IntraPosMvmntInstr(self):
			return self._IntraPosMvmntInstr

		@IntraPosMvmntInstr.setter
		def IntraPosMvmntInstr(self, value):
			self._IntraPosMvmntInstr = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntInstr")

		@IntraPosMvmntInstr.deleter
		def IntraPosMvmntInstr(self):
			del self._IntraPosMvmntInstr
			self._IntraPosMvmntInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntInstr', type=IntraPositionMovementInstruction002V06, min=1, max=1, mutex_group=None, array=False),
		))