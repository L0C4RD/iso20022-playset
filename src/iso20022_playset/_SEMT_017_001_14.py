# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionPostingReportV14 import SecuritiesTransactionPostingReportV14

class SEMT_017_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.017.001.14"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesTxPstngRpt"]
		@property
		def SctiesTxPstngRpt(self):
			return self._SctiesTxPstngRpt

		@SctiesTxPstngRpt.setter
		def SctiesTxPstngRpt(self, value):
			self._SctiesTxPstngRpt = value if type(value) != base_types.auto else self.make_default("SctiesTxPstngRpt")

		@SctiesTxPstngRpt.deleter
		def SctiesTxPstngRpt(self):
			del self._SctiesTxPstngRpt
			self._SctiesTxPstngRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxPstngRpt', type=SecuritiesTransactionPostingReportV14, min=1, max=1, mutex_group=None, array=False),
		))