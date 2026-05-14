# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInstructionV14 import CorporateActionInstructionV14

class SEEV_033_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnInstr"]
		@property
		def CorpActnInstr(self):
			return self._CorpActnInstr

		@CorpActnInstr.setter
		def CorpActnInstr(self, value):
			self._CorpActnInstr = value if type(value) != base_types.auto else self.make_default("CorpActnInstr")

		@CorpActnInstr.deleter
		def CorpActnInstr(self):
			del self._CorpActnInstr
			self._CorpActnInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionInstructionV14, min=1, max=1, mutex_group=None, array=False),
		))