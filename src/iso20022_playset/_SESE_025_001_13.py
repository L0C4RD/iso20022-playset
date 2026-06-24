# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionConfirmationV13 import SecuritiesSettlementTransactionConfirmationV13

class SESE_025_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.025.001.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmTxConf"]
		@property
		def SctiesSttlmTxConf(self):
			return self._SctiesSttlmTxConf

		@SctiesSttlmTxConf.setter
		def SctiesSttlmTxConf(self, value):
			self._SctiesSttlmTxConf = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxConf")

		@SctiesSttlmTxConf.deleter
		def SctiesSttlmTxConf(self):
			del self._SctiesSttlmTxConf
			self._SctiesSttlmTxConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxConf', type=SecuritiesSettlementTransactionConfirmationV13, min=1, max=1, mutex_group=None, array=False),
		))