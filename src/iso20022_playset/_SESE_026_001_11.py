# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionReversalAdviceV11 import SecuritiesSettlementTransactionReversalAdviceV11

class SESE_026_001_11():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.026.001.11"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmTxRvslAdvc"]
		@property
		def SctiesSttlmTxRvslAdvc(self):
			return self._SctiesSttlmTxRvslAdvc

		@SctiesSttlmTxRvslAdvc.setter
		def SctiesSttlmTxRvslAdvc(self, value):
			self._SctiesSttlmTxRvslAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxRvslAdvc")

		@SctiesSttlmTxRvslAdvc.deleter
		def SctiesSttlmTxRvslAdvc(self):
			del self._SctiesSttlmTxRvslAdvc
			self._SctiesSttlmTxRvslAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxRvslAdvc', type=SecuritiesSettlementTransactionReversalAdviceV11, min=1, max=1, mutex_group=None, array=False),
		))