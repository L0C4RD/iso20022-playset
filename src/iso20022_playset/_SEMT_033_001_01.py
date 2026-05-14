# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionCancellationRequestReportV01 import SecuritiesTransactionCancellationRequestReportV01

class SEMT_033_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxCxlReqRpt"]
		@property
		def SctiesTxCxlReqRpt(self):
			return self._SctiesTxCxlReqRpt

		@SctiesTxCxlReqRpt.setter
		def SctiesTxCxlReqRpt(self, value):
			self._SctiesTxCxlReqRpt = value if type(value) != base_types.auto else self.make_default("SctiesTxCxlReqRpt")

		@SctiesTxCxlReqRpt.deleter
		def SctiesTxCxlReqRpt(self):
			del self._SctiesTxCxlReqRpt
			self._SctiesTxCxlReqRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxCxlReqRpt', type=SecuritiesTransactionCancellationRequestReportV01, min=1, max=1, mutex_group=None, array=False),
		))