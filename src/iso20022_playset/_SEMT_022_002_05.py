# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementTransactionAuditTrailReport002V05 import SecuritiesSettlementTransactionAuditTrailReport002V05

class SEMT_022_002_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.022.002.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmTxAudtTrlRpt"]
		@property
		def SctiesSttlmTxAudtTrlRpt(self):
			return self._SctiesSttlmTxAudtTrlRpt

		@SctiesSttlmTxAudtTrlRpt.setter
		def SctiesSttlmTxAudtTrlRpt(self, value):
			self._SctiesSttlmTxAudtTrlRpt = value if type(value) != base_types.auto else self.make_default("SctiesSttlmTxAudtTrlRpt")

		@SctiesSttlmTxAudtTrlRpt.deleter
		def SctiesSttlmTxAudtTrlRpt(self):
			del self._SctiesSttlmTxAudtTrlRpt
			self._SctiesSttlmTxAudtTrlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmTxAudtTrlRpt', type=SecuritiesSettlementTransactionAuditTrailReport002V05, min=1, max=1, mutex_group=None, array=False),
		))