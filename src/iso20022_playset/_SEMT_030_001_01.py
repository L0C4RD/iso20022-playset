# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementConditionsModificationRequestQueryV01 import SecuritiesSettlementConditionsModificationRequestQueryV01

class SEMT_030_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:semt.030.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesSttlmCondsModReqQry"]
		@property
		def SctiesSttlmCondsModReqQry(self):
			return self._SctiesSttlmCondsModReqQry

		@SctiesSttlmCondsModReqQry.setter
		def SctiesSttlmCondsModReqQry(self, value):
			self._SctiesSttlmCondsModReqQry = value if type(value) != base_types.auto else self.make_default("SctiesSttlmCondsModReqQry")

		@SctiesSttlmCondsModReqQry.deleter
		def SctiesSttlmCondsModReqQry(self):
			del self._SctiesSttlmCondsModReqQry
			self._SctiesSttlmCondsModReqQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondsModReqQry', type=SecuritiesSettlementConditionsModificationRequestQueryV01, min=1, max=1, mutex_group=None, array=False),
		))