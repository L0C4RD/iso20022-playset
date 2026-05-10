from . import base_types
from .SecuritiesSettlementConditionModificationStatusAdviceV10 import SecuritiesSettlementConditionModificationStatusAdviceV10

class SESE_031_001_10():

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
			base_types.FieldEntry(name='SctiesSttlmCondModStsAdvc', type=SecuritiesSettlementConditionModificationStatusAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))

