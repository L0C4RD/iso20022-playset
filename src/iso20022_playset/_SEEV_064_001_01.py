# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyerProtectionInstructionAllegementNotificationV01 import BuyerProtectionInstructionAllegementNotificationV01

class SEEV_064_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.064.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_BuyrPrtcnInstrAllgmtNtfctn"]
		@property
		def BuyrPrtcnInstrAllgmtNtfctn(self):
			return self._BuyrPrtcnInstrAllgmtNtfctn

		@BuyrPrtcnInstrAllgmtNtfctn.setter
		def BuyrPrtcnInstrAllgmtNtfctn(self, value):
			self._BuyrPrtcnInstrAllgmtNtfctn = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrAllgmtNtfctn")

		@BuyrPrtcnInstrAllgmtNtfctn.deleter
		def BuyrPrtcnInstrAllgmtNtfctn(self):
			del self._BuyrPrtcnInstrAllgmtNtfctn
			self._BuyrPrtcnInstrAllgmtNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrAllgmtNtfctn', type=BuyerProtectionInstructionAllegementNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))