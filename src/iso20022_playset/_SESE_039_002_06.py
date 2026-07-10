# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionModificationRequestStatusAdvice002V06 import SecuritiesSettlementTransactionModificationRequestStatusAdvice002V06

class SESE_039_002_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.039.002.06"
		_docname = "sese.039.002.06"

		__slots__ = ["_SctiesSttlmTxModReqStsAdvc"]
		@property
		def SctiesSttlmTxModReqStsAdvc(self):
			return self._SctiesSttlmTxModReqStsAdvc

		@SctiesSttlmTxModReqStsAdvc.setter
		def SctiesSttlmTxModReqStsAdvc(self, value):
			self._SctiesSttlmTxModReqStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxModReqStsAdvc")

		@SctiesSttlmTxModReqStsAdvc.deleter
		def SctiesSttlmTxModReqStsAdvc(self):
			del self._SctiesSttlmTxModReqStsAdvc
			self._SctiesSttlmTxModReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxModReqStsAdvc', type=SecuritiesSettlementTransactionModificationRequestStatusAdvice002V06, min=1, max=1, mutex_group=None, array=False),
		))