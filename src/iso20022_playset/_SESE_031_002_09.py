# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementConditionModificationStatusAdvice002V09

class SESE_031_002_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.031.002.09"
		_docname = "sese.031.002.09"

		__slots__ = ["_SctiesSttlmCondModStsAdvc"]
		@property
		def SctiesSttlmCondModStsAdvc(self):
			return self._SctiesSttlmCondModStsAdvc

		@SctiesSttlmCondModStsAdvc.setter
		def SctiesSttlmCondModStsAdvc(self, value):
			self._SctiesSttlmCondModStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'SctiesSttlmCondModStsAdvc', SecuritiesSettlementConditionModificationStatusAdvice002V09, False)

		@SctiesSttlmCondModStsAdvc.deleter
		def SctiesSttlmCondModStsAdvc(self):
			del self._SctiesSttlmCondModStsAdvc
			self._SctiesSttlmCondModStsAdvc = base_types.UninitialisedField(self, 'SctiesSttlmCondModStsAdvc', SecuritiesSettlementConditionModificationStatusAdvice002V09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondModStsAdvc', type=SecuritiesSettlementConditionModificationStatusAdvice002V09, min=1, max=1, mutex_group=None, array=False),
		))