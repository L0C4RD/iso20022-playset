# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingReferenceDataReportV02 import FinancialInstrumentReportingReferenceDataReportV02

class AUTH_017_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgRefDataRpt"]
		@property
		def FinInstrmRptgRefDataRpt(self):
			return self._FinInstrmRptgRefDataRpt

		@FinInstrmRptgRefDataRpt.setter
		def FinInstrmRptgRefDataRpt(self, value):
			self._FinInstrmRptgRefDataRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgRefDataRpt")

		@FinInstrmRptgRefDataRpt.deleter
		def FinInstrmRptgRefDataRpt(self):
			del self._FinInstrmRptgRefDataRpt
			self._FinInstrmRptgRefDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataRpt', type=FinancialInstrumentReportingReferenceDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))