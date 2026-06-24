# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentReportingEquityTransparencyDataReportV01 import FinancialInstrumentReportingEquityTransparencyDataReportV01

class AUTH_032_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.032.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinInstrmRptgEqtyTrnsprncyDataRpt"]
		@property
		def FinInstrmRptgEqtyTrnsprncyDataRpt(self):
			return self._FinInstrmRptgEqtyTrnsprncyDataRpt

		@FinInstrmRptgEqtyTrnsprncyDataRpt.setter
		def FinInstrmRptgEqtyTrnsprncyDataRpt(self, value):
			self._FinInstrmRptgEqtyTrnsprncyDataRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgEqtyTrnsprncyDataRpt")

		@FinInstrmRptgEqtyTrnsprncyDataRpt.deleter
		def FinInstrmRptgEqtyTrnsprncyDataRpt(self):
			del self._FinInstrmRptgEqtyTrnsprncyDataRpt
			self._FinInstrmRptgEqtyTrnsprncyDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgEqtyTrnsprncyDataRpt', type=FinancialInstrumentReportingEquityTransparencyDataReportV01, min=1, max=1, mutex_group=None, array=False),
		))