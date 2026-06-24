# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementConditionsModificationRequest002V09 import SecuritiesSettlementConditionsModificationRequest002V09

class SESE_030_002_09():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.030.002.09"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmCondsModReq"]
		@property
		def SctiesSttlmCondsModReq(self):
			return self._SctiesSttlmCondsModReq

		@SctiesSttlmCondsModReq.setter
		def SctiesSttlmCondsModReq(self, value):
			self._SctiesSttlmCondsModReq = value if type(value) != base_types.auto else self.make_default("SctiesSttlmCondsModReq")

		@SctiesSttlmCondsModReq.deleter
		def SctiesSttlmCondsModReq(self):
			del self._SctiesSttlmCondsModReq
			self._SctiesSttlmCondsModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondsModReq', type=SecuritiesSettlementConditionsModificationRequest002V09, min=1, max=1, mutex_group=None, array=False),
		))