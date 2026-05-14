# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionPenaltiesReportV01 import SecuritiesTransactionPenaltiesReportV01

class SEMT_044_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTxPnltiesRpt"]
		@property
		def SctiesTxPnltiesRpt(self):
			return self._SctiesTxPnltiesRpt

		@SctiesTxPnltiesRpt.setter
		def SctiesTxPnltiesRpt(self, value):
			self._SctiesTxPnltiesRpt = value if type(value) != base_types.auto else self.make_default("SctiesTxPnltiesRpt")

		@SctiesTxPnltiesRpt.deleter
		def SctiesTxPnltiesRpt(self):
			del self._SctiesTxPnltiesRpt
			self._SctiesTxPnltiesRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPnltiesRpt', type=SecuritiesTransactionPenaltiesReportV01, min=1, max=1, mutex_group=None, array=False),
		))