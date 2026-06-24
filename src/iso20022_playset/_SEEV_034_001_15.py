# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInstructionStatusAdviceV15 import CorporateActionInstructionStatusAdviceV15

class SEEV_034_001_15():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.034.001.15"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CorpActnInstrStsAdvc"]
		@property
		def CorpActnInstrStsAdvc(self):
			return self._CorpActnInstrStsAdvc

		@CorpActnInstrStsAdvc.setter
		def CorpActnInstrStsAdvc(self, value):
			self._CorpActnInstrStsAdvc = value if type(value) != base_types.auto else self.make_default("CorpActnInstrStsAdvc")

		@CorpActnInstrStsAdvc.deleter
		def CorpActnInstrStsAdvc(self):
			del self._CorpActnInstrStsAdvc
			self._CorpActnInstrStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrStsAdvc', type=CorporateActionInstructionStatusAdviceV15, min=1, max=1, mutex_group=None, array=False),
		))