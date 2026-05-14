# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingTransactionQueryV02 import SecuritiesFinancingReportingTransactionQueryV02

class AUTH_094_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgTxQry"]
		@property
		def SctiesFincgRptgTxQry(self):
			return self._SctiesFincgRptgTxQry

		@SctiesFincgRptgTxQry.setter
		def SctiesFincgRptgTxQry(self, value):
			self._SctiesFincgRptgTxQry = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgTxQry")

		@SctiesFincgRptgTxQry.deleter
		def SctiesFincgRptgTxQry(self):
			del self._SctiesFincgRptgTxQry
			self._SctiesFincgRptgTxQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxQry', type=SecuritiesFinancingReportingTransactionQueryV02, min=1, max=1, mutex_group=None, array=False),
		))