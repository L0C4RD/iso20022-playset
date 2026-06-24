# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyerProtectionInstructionV01 import BuyerProtectionInstructionV01

class SEEV_060_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.060.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_BuyrPrtcnInstr"]
		@property
		def BuyrPrtcnInstr(self):
			return self._BuyrPrtcnInstr

		@BuyrPrtcnInstr.setter
		def BuyrPrtcnInstr(self, value):
			self._BuyrPrtcnInstr = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstr")

		@BuyrPrtcnInstr.deleter
		def BuyrPrtcnInstr(self):
			del self._BuyrPrtcnInstr
			self._BuyrPrtcnInstr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstr', type=BuyerProtectionInstructionV01, min=1, max=1, mutex_group=None, array=False),
		))