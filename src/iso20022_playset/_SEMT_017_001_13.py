# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionPostingReportV13

class SEMT_017_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.017.001.13"
		_docname = "semt.017.001.13"

		__slots__ = ["_SctiesTxPstngRpt"]
		@property
		def SctiesTxPstngRpt(self):
			return self._SctiesTxPstngRpt

		@SctiesTxPstngRpt.setter
		def SctiesTxPstngRpt(self, value):
			self._SctiesTxPstngRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxPstngRpt', SecuritiesTransactionPostingReportV13, False)

		@SctiesTxPstngRpt.deleter
		def SctiesTxPstngRpt(self):
			del self._SctiesTxPstngRpt
			self._SctiesTxPstngRpt = base_types.UninitialisedField(self, 'SctiesTxPstngRpt', SecuritiesTransactionPostingReportV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPstngRpt', type=SecuritiesTransactionPostingReportV13, min=1, max=1, mutex_group=None, array=False),
		))