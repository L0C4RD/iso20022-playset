# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPositionMovementInstructionV07

class SEMT_013_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.013.001.07"
		_docname = "semt.013.001.07"

		__slots__ = ["_IntraPosMvmntInstr"]
		@property
		def IntraPosMvmntInstr(self):
			return self._IntraPosMvmntInstr

		@IntraPosMvmntInstr.setter
		def IntraPosMvmntInstr(self, value):
			self._IntraPosMvmntInstr = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmntInstr', IntraPositionMovementInstructionV07, False)

		@IntraPosMvmntInstr.deleter
		def IntraPosMvmntInstr(self):
			del self._IntraPosMvmntInstr
			self._IntraPosMvmntInstr = base_types.UninitialisedField(self, 'IntraPosMvmntInstr', IntraPositionMovementInstructionV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntInstr', type=IntraPositionMovementInstructionV07, min=1, max=1, mutex_group=None, array=False),
		))