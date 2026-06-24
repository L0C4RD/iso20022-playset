# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransferOutInstructionV09 import TransferOutInstructionV09

class SESE_001_001_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:sese.001.001.09",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_TrfOutInstr"]
		@property
		def TrfOutInstr(self):
			return self._TrfOutInstr

		@TrfOutInstr.setter
		def TrfOutInstr(self, value):
			self._TrfOutInstr = value if type(value) != base_types.auto else self.make_default("TrfOutInstr")

		@TrfOutInstr.deleter
		def TrfOutInstr(self):
			del self._TrfOutInstr
			self._TrfOutInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfOutInstr', type=TransferOutInstructionV09, min=1, max=1, mutex_group=None, array=False),
		))