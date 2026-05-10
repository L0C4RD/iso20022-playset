from . import base_types
from .SecuritiesTransactionType44Choice import SecuritiesTransactionType44Choice
from .CorporateActionEventType110Choice import CorporateActionEventType110Choice

class SettlementOrCorporateActionEvent34Choice(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtTp", "_SctiesTxTp"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtTp', type=CorporateActionEventType110Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesTxTp', type=SecuritiesTransactionType44Choice, min=0, max=1, mutex_group=1, array=False),
	))

