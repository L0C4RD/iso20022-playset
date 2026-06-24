# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementInstructionV07 import IntraPositionMovementInstructionV07

class SEMT_013_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.013.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
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
			base_types.FieldEntry(name='IntraPosMvmntInstr', type=IntraPositionMovementInstructionV07, min=1, max=1, mutex_group=None, array=False),
		))