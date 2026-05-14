# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransferOutInstructionV10 import TransferOutInstructionV10

class SESE_001_001_10():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='TrfOutInstr', type=TransferOutInstructionV10, min=1, max=1, mutex_group=None, array=False),
		))