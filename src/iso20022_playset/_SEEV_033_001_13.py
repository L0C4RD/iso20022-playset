# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInstructionV13

class SEEV_033_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.033.001.13"
		_docname = "seev.033.001.13"

		__slots__ = ["_CorpActnInstr"]
		@property
		def CorpActnInstr(self):
			return self._CorpActnInstr

		@CorpActnInstr.setter
		def CorpActnInstr(self, value):
			self._CorpActnInstr = value if value is not None else base_types.UninitialisedField(self, 'CorpActnInstr', CorporateActionInstructionV13, False)

		@CorpActnInstr.deleter
		def CorpActnInstr(self):
			del self._CorpActnInstr
			self._CorpActnInstr = base_types.UninitialisedField(self, 'CorpActnInstr', CorporateActionInstructionV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionInstructionV13, min=1, max=1, mutex_group=None, array=False),
		))