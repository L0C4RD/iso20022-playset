# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentDocumentIdentificationAndStatus1Choice
from . import CorporateActionGeneralInformation175

class AgentCANotificationStatusAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_AgtDocIdAndSts", "_CorpActnGnlInf"]
	@property
	def AgtDocIdAndSts(self):
		return self._AgtDocIdAndSts

	@AgtDocIdAndSts.setter
	def AgtDocIdAndSts(self, value):
		self._AgtDocIdAndSts = value if value is not None else base_types.UninitialisedField(self, 'AgtDocIdAndSts', AgentDocumentIdentificationAndStatus1Choice, False)

	@AgtDocIdAndSts.deleter
	def AgtDocIdAndSts(self):
		del self._AgtDocIdAndSts
		self._AgtDocIdAndSts = base_types.UninitialisedField(self, 'AgtDocIdAndSts', AgentDocumentIdentificationAndStatus1Choice, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation175, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation175, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtDocIdAndSts', type=AgentDocumentIdentificationAndStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation175, min=1, max=1, mutex_group=None, array=False),
	))