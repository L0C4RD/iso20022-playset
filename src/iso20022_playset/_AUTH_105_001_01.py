# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesFinancingReportingPositionSetReportV01

class AUTH_105_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.105.001.01"
		_docname = "auth.105.001.01"

		__slots__ = ["_SctiesFincgRptgPosSetRpt"]
		@property
		def SctiesFincgRptgPosSetRpt(self):
			return self._SctiesFincgRptgPosSetRpt

		@SctiesFincgRptgPosSetRpt.setter
		def SctiesFincgRptgPosSetRpt(self, value):
			self._SctiesFincgRptgPosSetRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgRptgPosSetRpt', SecuritiesFinancingReportingPositionSetReportV01, False)

		@SctiesFincgRptgPosSetRpt.deleter
		def SctiesFincgRptgPosSetRpt(self):
			del self._SctiesFincgRptgPosSetRpt
			self._SctiesFincgRptgPosSetRpt = base_types.UninitialisedField(self, 'SctiesFincgRptgPosSetRpt', SecuritiesFinancingReportingPositionSetReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgPosSetRpt', type=SecuritiesFinancingReportingPositionSetReportV01, min=1, max=1, mutex_group=None, array=False),
		))