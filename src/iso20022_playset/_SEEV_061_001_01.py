# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyerProtectionInstructionStatusAdviceV01 import BuyerProtectionInstructionStatusAdviceV01

class SEEV_061_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:seev.061.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_BuyrPrtcnInstrStsAdvc"]
		@property
		def BuyrPrtcnInstrStsAdvc(self):
			return self._BuyrPrtcnInstrStsAdvc

		@BuyrPrtcnInstrStsAdvc.setter
		def BuyrPrtcnInstrStsAdvc(self, value):
			self._BuyrPrtcnInstrStsAdvc = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrStsAdvc")

		@BuyrPrtcnInstrStsAdvc.deleter
		def BuyrPrtcnInstrStsAdvc(self):
			del self._BuyrPrtcnInstrStsAdvc
			self._BuyrPrtcnInstrStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrStsAdvc', type=BuyerProtectionInstructionStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))