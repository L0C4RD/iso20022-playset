# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAMovementInstructionV01 import AgentCAMovementInstructionV01

class SEEV_019_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:seev.019.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AgtCAMvmntInstr"]
		@property
		def AgtCAMvmntInstr(self):
			return self._AgtCAMvmntInstr

		@AgtCAMvmntInstr.setter
		def AgtCAMvmntInstr(self, value):
			self._AgtCAMvmntInstr = value if type(value) != base_types.auto else self.make_default("AgtCAMvmntInstr")

		@AgtCAMvmntInstr.deleter
		def AgtCAMvmntInstr(self):
			del self._AgtCAMvmntInstr
			self._AgtCAMvmntInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAMvmntInstr', type=AgentCAMovementInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))