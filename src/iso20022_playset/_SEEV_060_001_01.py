# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionInstructionV01

class SEEV_060_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.060.001.01"
		_docname = "seev.060.001.01"

		__slots__ = ["_BuyrPrtcnInstr"]
		@property
		def BuyrPrtcnInstr(self):
			return self._BuyrPrtcnInstr

		@BuyrPrtcnInstr.setter
		def BuyrPrtcnInstr(self, value):
			self._BuyrPrtcnInstr = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnInstr', BuyerProtectionInstructionV01, False)

		@BuyrPrtcnInstr.deleter
		def BuyrPrtcnInstr(self):
			del self._BuyrPrtcnInstr
			self._BuyrPrtcnInstr = base_types.UninitialisedField(self, 'BuyrPrtcnInstr', BuyerProtectionInstructionV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstr', type=BuyerProtectionInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))