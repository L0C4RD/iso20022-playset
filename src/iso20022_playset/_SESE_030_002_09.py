# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementConditionsModificationRequest002V09

class SESE_030_002_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.030.002.09"
		_docname = "sese.030.002.09"

		__slots__ = ["_SctiesSttlmCondsModReq"]
		@property
		def SctiesSttlmCondsModReq(self):
			return self._SctiesSttlmCondsModReq

		@SctiesSttlmCondsModReq.setter
		def SctiesSttlmCondsModReq(self, value):
			self._SctiesSttlmCondsModReq = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmCondsModReq', SecuritiesSettlementConditionsModificationRequest002V09, False)

		@SctiesSttlmCondsModReq.deleter
		def SctiesSttlmCondsModReq(self):
			del self._SctiesSttlmCondsModReq
			self._SctiesSttlmCondsModReq = base_types.UninitialisedField(self, 'SctiesSttlmCondsModReq', SecuritiesSettlementConditionsModificationRequest002V09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondsModReq', type=SecuritiesSettlementConditionsModificationRequest002V09, min=1, max=1, mutex_group=None, array=False),
		))