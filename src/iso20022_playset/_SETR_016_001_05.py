# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrderInstructionStatusReportV05

class SETR_016_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:setr.016.001.05"
		_docname = "setr.016.001.05"

		__slots__ = ["_OrdrInstrStsRpt"]
		@property
		def OrdrInstrStsRpt(self):
			return self._OrdrInstrStsRpt

		@OrdrInstrStsRpt.setter
		def OrdrInstrStsRpt(self, value):
			self._OrdrInstrStsRpt = value if value is not None else base_types.UninitialisedField(self, 'OrdrInstrStsRpt', OrderInstructionStatusReportV05, False)

		@OrdrInstrStsRpt.deleter
		def OrdrInstrStsRpt(self):
			del self._OrdrInstrStsRpt
			self._OrdrInstrStsRpt = base_types.UninitialisedField(self, 'OrdrInstrStsRpt', OrderInstructionStatusReportV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='OrdrInstrStsRpt', type=OrderInstructionStatusReportV05, min=1, max=1, mutex_group=None, array=False),
		))