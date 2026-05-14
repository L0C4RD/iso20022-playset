# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesSettlementConditionModificationStatusAdviceV11 import SecuritiesSettlementConditionModificationStatusAdviceV11

class SESE_031_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmCondModStsAdvc"]
		@property
		def SctiesSttlmCondModStsAdvc(self):
			return self._SctiesSttlmCondModStsAdvc

		@SctiesSttlmCondModStsAdvc.setter
		def SctiesSttlmCondModStsAdvc(self, value):
			self._SctiesSttlmCondModStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesSttlmCondModStsAdvc")

		@SctiesSttlmCondModStsAdvc.deleter
		def SctiesSttlmCondModStsAdvc(self):
			del self._SctiesSttlmCondModStsAdvc
			self._SctiesSttlmCondModStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondModStsAdvc', type=SecuritiesSettlementConditionModificationStatusAdviceV11, min=1, max=1, mutex_group=None, array=False),
		))