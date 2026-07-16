# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCADeactivationInstructionV01

class SEEV_028_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.028.001.01"
		_docname = "seev.028.001.01"

		__slots__ = ["_AgtCADeactvtnInstr"]
		@property
		def AgtCADeactvtnInstr(self):
			return self._AgtCADeactvtnInstr

		@AgtCADeactvtnInstr.setter
		def AgtCADeactvtnInstr(self, value):
			self._AgtCADeactvtnInstr = value if value is not None else base_types.UninitialisedField(self, 'AgtCADeactvtnInstr', AgentCADeactivationInstructionV01, False)

		@AgtCADeactvtnInstr.deleter
		def AgtCADeactvtnInstr(self):
			del self._AgtCADeactvtnInstr
			self._AgtCADeactvtnInstr = base_types.UninitialisedField(self, 'AgtCADeactvtnInstr', AgentCADeactivationInstructionV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADeactvtnInstr', type=AgentCADeactivationInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))