# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTransactionStatusQueryV07 import SecuritiesTransactionStatusQueryV07

class SESE_021_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.021.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesTxStsQry"]
		@property
		def SctiesTxStsQry(self):
			return self._SctiesTxStsQry

		@SctiesTxStsQry.setter
		def SctiesTxStsQry(self, value):
			self._SctiesTxStsQry = value if type(value) != base_types.auto else self.make_default("SctiesTxStsQry")

		@SctiesTxStsQry.deleter
		def SctiesTxStsQry(self):
			del self._SctiesTxStsQry
			self._SctiesTxStsQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxStsQry', type=SecuritiesTransactionStatusQueryV07, min=1, max=1, mutex_group=None, array=False),
		))