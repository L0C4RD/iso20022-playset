# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingReferenceDataDeltaReportV03 import FinancialInstrumentReportingReferenceDataDeltaReportV03

class AUTH_036_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgRefDataDltaRpt"]
		@property
		def FinInstrmRptgRefDataDltaRpt(self):
			return self._FinInstrmRptgRefDataDltaRpt

		@FinInstrmRptgRefDataDltaRpt.setter
		def FinInstrmRptgRefDataDltaRpt(self, value):
			self._FinInstrmRptgRefDataDltaRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgRefDataDltaRpt")

		@FinInstrmRptgRefDataDltaRpt.deleter
		def FinInstrmRptgRefDataDltaRpt(self):
			del self._FinInstrmRptgRefDataDltaRpt
			self._FinInstrmRptgRefDataDltaRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataDltaRpt', type=FinancialInstrumentReportingReferenceDataDeltaReportV03, min=1, max=1, mutex_group=None, array=False),
		))