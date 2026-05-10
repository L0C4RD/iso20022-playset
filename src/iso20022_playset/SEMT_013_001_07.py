from . import base_types
import IntraPositionMovementInstructionV07

class SEMT_013_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraPosMvmntInstr"]
		@property
		def IntraPosMvmntInstr(self):
			return self._IntraPosMvmntInstr

		@IntraPosMvmntInstr.setter
		def IntraPosMvmntInstr(self, value):
			self._IntraPosMvmntInstr = value if type(value) != auto else self.make_default("IntraPosMvmntInstr")

		@IntraPosMvmntInstr.deleter
		def IntraPosMvmntInstr(self):
			del self._IntraPosMvmntInstr
			self._IntraPosMvmntInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntInstr', type=IntraPositionMovementInstructionV07, min=1, max=1, mutex_group=None, array=False),
		))

