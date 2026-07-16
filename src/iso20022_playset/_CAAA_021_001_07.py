# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransactionAdviceResponseV07

class CAAA_021_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.021.001.07"
		_docname = "caaa.021.001.07"

		__slots__ = ["_TxAdvcRspn"]
		@property
		def TxAdvcRspn(self):
			return self._TxAdvcRspn

		@TxAdvcRspn.setter
		def TxAdvcRspn(self, value):
			self._TxAdvcRspn = value if value is not None else base_types.UninitialisedField(self, 'TxAdvcRspn', TransactionAdviceResponseV07, False)

		@TxAdvcRspn.deleter
		def TxAdvcRspn(self):
			del self._TxAdvcRspn
			self._TxAdvcRspn = base_types.UninitialisedField(self, 'TxAdvcRspn', TransactionAdviceResponseV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxAdvcRspn', type=TransactionAdviceResponseV07, min=1, max=1, mutex_group=None, array=False),
		))