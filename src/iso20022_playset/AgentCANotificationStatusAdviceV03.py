import base_types
import CorporateActionGeneralInformation175
import AgentDocumentIdentificationAndStatus1Choice

class AgentCANotificationStatusAdviceV03(base_types._BaseFieldType):

	__slots__ = ["_AgtDocIdAndSts", "_CorpActnGnlInf"]
	@property
	def AgtDocIdAndSts(self):
		return self._AgtDocIdAndSts

	@AgtDocIdAndSts.setter
	def AgtDocIdAndSts(self, value):
		self._AgtDocIdAndSts = value if type(value) != auto else self.make_default("AgtDocIdAndSts")

	@AgtDocIdAndSts.deleter
	def AgtDocIdAndSts(self):
		del self._AgtDocIdAndSts
		self._AgtDocIdAndSts = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtDocIdAndSts', type=AgentDocumentIdentificationAndStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation175, min=1, max=1, mutex_group=None, array=False),
	))

