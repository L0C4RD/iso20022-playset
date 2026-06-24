# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyerProtectionInstructionReportV01 import BuyerProtectionInstructionReportV01

class SEEV_067_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.067.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_BuyrPrtcnInstrRpt"]
		@property
		def BuyrPrtcnInstrRpt(self):
			return self._BuyrPrtcnInstrRpt

		@BuyrPrtcnInstrRpt.setter
		def BuyrPrtcnInstrRpt(self, value):
			self._BuyrPrtcnInstrRpt = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrRpt")

		@BuyrPrtcnInstrRpt.deleter
		def BuyrPrtcnInstrRpt(self):
			del self._BuyrPrtcnInstrRpt
			self._BuyrPrtcnInstrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrRpt', type=BuyerProtectionInstructionReportV01, min=1, max=1, mutex_group=None, array=False),
		))