# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInstruction002V13 import CorporateActionInstruction002V13

class SEEV_033_002_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.033.002.13"
		_docname = "seev.033.002.13"

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
			base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionInstruction002V13, min=1, max=1, mutex_group=None, array=False),
		))