# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingMarginDataTransactionStateReportV02 import SecuritiesFinancingReportingMarginDataTransactionStateReportV02

class AUTH_085_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.085.001.02"
		_docname = "auth.085.001.02"

		__slots__ = ["_SctiesFincgRptgMrgnDataTxStatRpt"]
		@property
		def SctiesFincgRptgMrgnDataTxStatRpt(self):
			return self._SctiesFincgRptgMrgnDataTxStatRpt

		@SctiesFincgRptgMrgnDataTxStatRpt.setter
		def SctiesFincgRptgMrgnDataTxStatRpt(self, value):
			self._SctiesFincgRptgMrgnDataTxStatRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgMrgnDataTxStatRpt")

		@SctiesFincgRptgMrgnDataTxStatRpt.deleter
		def SctiesFincgRptgMrgnDataTxStatRpt(self):
			del self._SctiesFincgRptgMrgnDataTxStatRpt
			self._SctiesFincgRptgMrgnDataTxStatRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgMrgnDataTxStatRpt', type=SecuritiesFinancingReportingMarginDataTransactionStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))