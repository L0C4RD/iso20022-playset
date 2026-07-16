# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DefaultFundContributionReportV02

class SECL_006_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.006.001.02"
		_docname = "secl.006.001.02"

		__slots__ = ["_DfltFndCntrbtnRpt"]
		@property
		def DfltFndCntrbtnRpt(self):
			return self._DfltFndCntrbtnRpt

		@DfltFndCntrbtnRpt.setter
		def DfltFndCntrbtnRpt(self, value):
			self._DfltFndCntrbtnRpt = value if value is not None else base_types.UninitialisedField(self, 'DfltFndCntrbtnRpt', DefaultFundContributionReportV02, False)

		@DfltFndCntrbtnRpt.deleter
		def DfltFndCntrbtnRpt(self):
			del self._DfltFndCntrbtnRpt
			self._DfltFndCntrbtnRpt = base_types.UninitialisedField(self, 'DfltFndCntrbtnRpt', DefaultFundContributionReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DfltFndCntrbtnRpt', type=DefaultFundContributionReportV02, min=1, max=1, mutex_group=None, array=False),
		))