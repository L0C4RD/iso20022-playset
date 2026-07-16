# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventType73Choice
from . import SecuritiesTransactionType48Choice

class SettlementOrCorporateActionEvent26Choice(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtTp", "_SctiesTxTp"]
	@property
	def CorpActnEvtTp(self):
		return self._CorpActnEvtTp

	@CorpActnEvtTp.setter
	def CorpActnEvtTp(self, value):
		self._CorpActnEvtTp = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtTp', CorporateActionEventType73Choice, False)

	@CorpActnEvtTp.deleter
	def CorpActnEvtTp(self):
		del self._CorpActnEvtTp
		self._CorpActnEvtTp = base_types.UninitialisedField(self, 'CorpActnEvtTp', CorporateActionEventType73Choice, False)

	@property
	def SctiesTxTp(self):
		return self._SctiesTxTp

	@SctiesTxTp.setter
	def SctiesTxTp(self, value):
		self._SctiesTxTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxTp', SecuritiesTransactionType48Choice, False)

	@SctiesTxTp.deleter
	def SctiesTxTp(self):
		del self._SctiesTxTp
		self._SctiesTxTp = base_types.UninitialisedField(self, 'SctiesTxTp', SecuritiesTransactionType48Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtTp', type=CorporateActionEventType73Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesTxTp', type=SecuritiesTransactionType48Choice, min=0, max=1, mutex_group=1, array=False),
	))