# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementAllegementRemovalAdviceV07 import SecuritiesSettlementAllegementRemovalAdviceV07

class SESE_029_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.029.001.07"
		_docname = "sese.029.001.07"

		__slots__ = ["_SctiesSttlmAllgmtRmvlAdvc"]
		@property
		def SctiesSttlmAllgmtRmvlAdvc(self):
			return self._SctiesSttlmAllgmtRmvlAdvc

		@SctiesSttlmAllgmtRmvlAdvc.setter
		def SctiesSttlmAllgmtRmvlAdvc(self, value):
			self._SctiesSttlmAllgmtRmvlAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmAllgmtRmvlAdvc")

		@SctiesSttlmAllgmtRmvlAdvc.deleter
		def SctiesSttlmAllgmtRmvlAdvc(self):
			del self._SctiesSttlmAllgmtRmvlAdvc
			self._SctiesSttlmAllgmtRmvlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmAllgmtRmvlAdvc', type=SecuritiesSettlementAllegementRemovalAdviceV07, min=1, max=1, mutex_group=None, array=False),
		))