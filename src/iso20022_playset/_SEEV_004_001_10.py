# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MeetingInstructionV10 import MeetingInstructionV10

class SEEV_004_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:seev.004.001.10",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_MtgInstr"]
		@property
		def MtgInstr(self):
			return self._MtgInstr

		@MtgInstr.setter
		def MtgInstr(self, value):
			self._MtgInstr = value if type(value) != base_types.auto else self.make_default("MtgInstr")

		@MtgInstr.deleter
		def MtgInstr(self):
			del self._MtgInstr
			self._MtgInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgInstr', type=MeetingInstructionV10, min=1, max=1, mutex_group=None, array=False),
		))