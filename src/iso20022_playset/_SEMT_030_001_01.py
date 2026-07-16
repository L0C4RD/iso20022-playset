# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementConditionsModificationRequestQueryV01

class SEMT_030_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.030.001.01"
		_docname = "semt.030.001.01"

		__slots__ = ["_SctiesSttlmCondsModReqQry"]
		@property
		def SctiesSttlmCondsModReqQry(self):
			return self._SctiesSttlmCondsModReqQry

		@SctiesSttlmCondsModReqQry.setter
		def SctiesSttlmCondsModReqQry(self, value):
			self._SctiesSttlmCondsModReqQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmCondsModReqQry', SecuritiesSettlementConditionsModificationRequestQueryV01, False)

		@SctiesSttlmCondsModReqQry.deleter
		def SctiesSttlmCondsModReqQry(self):
			del self._SctiesSttlmCondsModReqQry
			self._SctiesSttlmCondsModReqQry = base_types.UninitialisedField(self, 'SctiesSttlmCondsModReqQry', SecuritiesSettlementConditionsModificationRequestQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondsModReqQry', type=SecuritiesSettlementConditionsModificationRequestQueryV01, min=1, max=1, mutex_group=None, array=False),
		))