from . import base_types
from .IntraPositionMovementInstruction002V06 import IntraPositionMovementInstruction002V06

class SEMT_013_002_06():

	class Document(base_types._BaseFieldType):

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

