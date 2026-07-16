# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionPenaltiesReportV01

class SEMT_044_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.044.001.01"
		_docname = "semt.044.001.01"

		__slots__ = ["_SctiesTxPnltiesRpt"]
		@property
		def SctiesTxPnltiesRpt(self):
			return self._SctiesTxPnltiesRpt

		@SctiesTxPnltiesRpt.setter
		def SctiesTxPnltiesRpt(self, value):
			self._SctiesTxPnltiesRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxPnltiesRpt', SecuritiesTransactionPenaltiesReportV01, False)

		@SctiesTxPnltiesRpt.deleter
		def SctiesTxPnltiesRpt(self):
			del self._SctiesTxPnltiesRpt
			self._SctiesTxPnltiesRpt = base_types.UninitialisedField(self, 'SctiesTxPnltiesRpt', SecuritiesTransactionPenaltiesReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPnltiesRpt', type=SecuritiesTransactionPenaltiesReportV01, min=1, max=1, mutex_group=None, array=False),
		))