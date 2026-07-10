# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransferCancellationStatusReportV07 import TransferCancellationStatusReportV07

class SESE_010_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.010.001.07"
		_docname = "sese.010.001.07"

		__slots__ = ["_TrfCxlStsRpt"]
		@property
		def TrfCxlStsRpt(self):
			return self._TrfCxlStsRpt

		@TrfCxlStsRpt.setter
		def TrfCxlStsRpt(self, value):
			self._TrfCxlStsRpt = value if type(value) != base_types.auto else self.make_default("TrfCxlStsRpt")

		@TrfCxlStsRpt.deleter
		def TrfCxlStsRpt(self):
			del self._TrfCxlStsRpt
			self._TrfCxlStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TrfCxlStsRpt', type=TransferCancellationStatusReportV07, min=1, max=1, mutex_group=None, array=False),
		))