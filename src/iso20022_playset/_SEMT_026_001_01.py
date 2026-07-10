# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionQueryV01 import SecuritiesSettlementTransactionQueryV01

class SEMT_026_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.026.001.01"
		_docname = "semt.026.001.01"

		__slots__ = ["_SctiesSttlmTxQry"]
		@property
		def SctiesSttlmTxQry(self):
			return self._SctiesSttlmTxQry

		@SctiesSttlmTxQry.setter
		def SctiesSttlmTxQry(self, value):
			self._SctiesSttlmTxQry = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxQry")

		@SctiesSttlmTxQry.deleter
		def SctiesSttlmTxQry(self):
			del self._SctiesSttlmTxQry
			self._SctiesSttlmTxQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxQry', type=SecuritiesSettlementTransactionQueryV01, min=1, max=1, mutex_group=None, array=False),
		))