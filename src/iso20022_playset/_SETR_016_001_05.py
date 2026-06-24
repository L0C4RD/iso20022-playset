# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._OrderInstructionStatusReportV05 import OrderInstructionStatusReportV05

class SETR_016_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.016.001.05",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_OrdrInstrStsRpt"]
		@property
		def OrdrInstrStsRpt(self):
			return self._OrdrInstrStsRpt

		@OrdrInstrStsRpt.setter
		def OrdrInstrStsRpt(self, value):
			self._OrdrInstrStsRpt = value if type(value) != base_types.auto else self.make_default("OrdrInstrStsRpt")

		@OrdrInstrStsRpt.deleter
		def OrdrInstrStsRpt(self):
			del self._OrdrInstrStsRpt
			self._OrdrInstrStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrInstrStsRpt', type=OrderInstructionStatusReportV05, min=1, max=1, mutex_group=None, array=False),
		))