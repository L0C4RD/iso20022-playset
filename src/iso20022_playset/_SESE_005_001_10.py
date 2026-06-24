# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransferInInstructionV10 import TransferInInstructionV10

class SESE_005_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.005.001.10"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_TrfInInstr"]
		@property
		def TrfInInstr(self):
			return self._TrfInInstr

		@TrfInInstr.setter
		def TrfInInstr(self, value):
			self._TrfInInstr = value if type(value) != base_types.auto else self.make_default("TrfInInstr")

		@TrfInInstr.deleter
		def TrfInInstr(self):
			del self._TrfInInstr
			self._TrfInInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInInstr', type=TransferInInstructionV10, min=1, max=1, mutex_group=None, array=False),
		))