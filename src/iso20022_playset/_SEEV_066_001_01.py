# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyerProtectionInstructionReportRequestV01 import BuyerProtectionInstructionReportRequestV01

class SEEV_066_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.066.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_BuyrPrtcnInstrRptReq"]
		@property
		def BuyrPrtcnInstrRptReq(self):
			return self._BuyrPrtcnInstrRptReq

		@BuyrPrtcnInstrRptReq.setter
		def BuyrPrtcnInstrRptReq(self, value):
			self._BuyrPrtcnInstrRptReq = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnInstrRptReq")

		@BuyrPrtcnInstrRptReq.deleter
		def BuyrPrtcnInstrRptReq(self):
			del self._BuyrPrtcnInstrRptReq
			self._BuyrPrtcnInstrRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyrPrtcnInstrRptReq', type=BuyerProtectionInstructionReportRequestV01, min=1, max=1, mutex_group=None, array=False),
		))