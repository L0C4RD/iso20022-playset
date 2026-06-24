# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementConditionsModificationRequestReportV01 import SecuritiesSettlementConditionsModificationRequestReportV01

class SEMT_031_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.031.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SctiesSttlmCondsModReqRpt"]
		@property
		def SctiesSttlmCondsModReqRpt(self):
			return self._SctiesSttlmCondsModReqRpt

		@SctiesSttlmCondsModReqRpt.setter
		def SctiesSttlmCondsModReqRpt(self, value):
			self._SctiesSttlmCondsModReqRpt = value if type(value) != base_types.auto else self.make_default("SctiesSttlmCondsModReqRpt")

		@SctiesSttlmCondsModReqRpt.deleter
		def SctiesSttlmCondsModReqRpt(self):
			del self._SctiesSttlmCondsModReqRpt
			self._SctiesSttlmCondsModReqRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondsModReqRpt', type=SecuritiesSettlementConditionsModificationRequestReportV01, min=1, max=1, mutex_group=None, array=False),
		))