from . import base_types
from ._CorporateActionEventType101Choice import CorporateActionEventType101Choice
from ._SecuritiesTransactionType52Choice import SecuritiesTransactionType52Choice

class SettlementOrCorporateActionEvent32Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesTxTp", "_CorpActnEvtTp"]
	@property
	def SctiesTxTp(self):
		return self._SctiesTxTp

	@SctiesTxTp.setter
	def SctiesTxTp(self, value):
		self._SctiesTxTp = value if type(value) != base_types.auto else self.make_default("SctiesTxTp")

	@SctiesTxTp.deleter
	def SctiesTxTp(self):
		del self._SctiesTxTp
		self._SctiesTxTp = None

	@property
	def CorpActnEvtTp(self):
		return self._CorpActnEvtTp

	@CorpActnEvtTp.setter
	def CorpActnEvtTp(self, value):
		self._CorpActnEvtTp = value if type(value) != base_types.auto else self.make_default("CorpActnEvtTp")

	@CorpActnEvtTp.deleter
	def CorpActnEvtTp(self):
		del self._CorpActnEvtTp
		self._CorpActnEvtTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesTxTp', type=SecuritiesTransactionType52Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnEvtTp', type=CorporateActionEventType101Choice, min=0, max=1, mutex_group=1, array=False),
	))

