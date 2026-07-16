# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesTransactionStatusQueryV08

class SESE_021_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.021.001.08"
		_docname = "sese.021.001.08"

		__slots__ = ["_SctiesTxStsQry"]
		@property
		def SctiesTxStsQry(self):
			return self._SctiesTxStsQry

		@SctiesTxStsQry.setter
		def SctiesTxStsQry(self, value):
			self._SctiesTxStsQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxStsQry', SecuritiesTransactionStatusQueryV08, False)

		@SctiesTxStsQry.deleter
		def SctiesTxStsQry(self):
			del self._SctiesTxStsQry
			self._SctiesTxStsQry = base_types.UninitialisedField(self, 'SctiesTxStsQry', SecuritiesTransactionStatusQueryV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTxStsQry', type=SecuritiesTransactionStatusQueryV08, min=1, max=1, mutex_group=None, array=False),
		))