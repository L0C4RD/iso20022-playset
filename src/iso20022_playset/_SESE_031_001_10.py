# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementConditionModificationStatusAdviceV10

class SESE_031_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.031.001.10"
		_docname = "sese.031.001.10"

		__slots__ = ["_SctiesSttlmCondModStsAdvc"]
		@property
		def SctiesSttlmCondModStsAdvc(self):
			return self._SctiesSttlmCondModStsAdvc

		@SctiesSttlmCondModStsAdvc.setter
		def SctiesSttlmCondModStsAdvc(self, value):
			self._SctiesSttlmCondModStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmCondModStsAdvc', SecuritiesSettlementConditionModificationStatusAdviceV10, False)

		@SctiesSttlmCondModStsAdvc.deleter
		def SctiesSttlmCondModStsAdvc(self):
			del self._SctiesSttlmCondModStsAdvc
			self._SctiesSttlmCondModStsAdvc = base_types.UninitialisedField(self, 'SctiesSttlmCondModStsAdvc', SecuritiesSettlementConditionModificationStatusAdviceV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondModStsAdvc', type=SecuritiesSettlementConditionModificationStatusAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))