# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInstructionStatusAdvice002V15

class SEEV_034_002_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.034.002.15"
		_docname = "seev.034.002.15"

		__slots__ = ["_CorpActnInstrStsAdvc"]
		@property
		def CorpActnInstrStsAdvc(self):
			return self._CorpActnInstrStsAdvc

		@CorpActnInstrStsAdvc.setter
		def CorpActnInstrStsAdvc(self, value):
			self._CorpActnInstrStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'CorpActnInstrStsAdvc', CorporateActionInstructionStatusAdvice002V15, False)

		@CorpActnInstrStsAdvc.deleter
		def CorpActnInstrStsAdvc(self):
			del self._CorpActnInstrStsAdvc
			self._CorpActnInstrStsAdvc = base_types.UninitialisedField(self, 'CorpActnInstrStsAdvc', CorporateActionInstructionStatusAdvice002V15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrStsAdvc', type=CorporateActionInstructionStatusAdvice002V15, min=1, max=1, mutex_group=None, array=False),
		))