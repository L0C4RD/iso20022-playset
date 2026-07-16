# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransferInInstructionV10

class SESE_005_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.005.001.10"
		_docname = "sese.005.001.10"

		__slots__ = ["_TrfInInstr"]
		@property
		def TrfInInstr(self):
			return self._TrfInInstr

		@TrfInInstr.setter
		def TrfInInstr(self, value):
			self._TrfInInstr = value if value is not None else base_types.UninitialisedField(self, 'TrfInInstr', TransferInInstructionV10, False)

		@TrfInInstr.deleter
		def TrfInInstr(self):
			del self._TrfInInstr
			self._TrfInInstr = base_types.UninitialisedField(self, 'TrfInInstr', TransferInInstructionV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfInInstr', type=TransferInInstructionV10, min=1, max=1, mutex_group=None, array=False),
		))