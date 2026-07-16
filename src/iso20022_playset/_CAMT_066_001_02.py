# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraBalanceMovementInstructionV02

class CAMT_066_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.066.001.02"
		_docname = "camt.066.001.02"

		__slots__ = ["_IntraBalMvmntInstr"]
		@property
		def IntraBalMvmntInstr(self):
			return self._IntraBalMvmntInstr

		@IntraBalMvmntInstr.setter
		def IntraBalMvmntInstr(self, value):
			self._IntraBalMvmntInstr = value if value is not None else base_types.UninitialisedField(self, 'IntraBalMvmntInstr', IntraBalanceMovementInstructionV02, False)

		@IntraBalMvmntInstr.deleter
		def IntraBalMvmntInstr(self):
			del self._IntraBalMvmntInstr
			self._IntraBalMvmntInstr = base_types.UninitialisedField(self, 'IntraBalMvmntInstr', IntraBalanceMovementInstructionV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntInstr', type=IntraBalanceMovementInstructionV02, min=1, max=1, mutex_group=None, array=False),
		))