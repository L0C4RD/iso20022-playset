import base_types
import ISODate
import SettlementTerms3
import BreakDown1Choice

class IntentToPay2(base_types._BaseFieldType):

	__slots__ = ["_XpctdPmtDt", "_Brkdwn", "_SttlmTerms"]
	@property
	def XpctdPmtDt(self):
		return self._XpctdPmtDt

	@XpctdPmtDt.setter
	def XpctdPmtDt(self, value):
		self._XpctdPmtDt = value if type(value) != auto else self.make_default("XpctdPmtDt")

	@XpctdPmtDt.deleter
	def XpctdPmtDt(self):
		del self._XpctdPmtDt
		self._XpctdPmtDt = None

	@property
	def Brkdwn(self):
		return self._Brkdwn

	@Brkdwn.setter
	def Brkdwn(self, value):
		self._Brkdwn = value if type(value) != auto else self.make_default("Brkdwn")

	@Brkdwn.deleter
	def Brkdwn(self):
		del self._Brkdwn
		self._Brkdwn = None

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if type(value) != auto else self.make_default("SttlmTerms")

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XpctdPmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brkdwn', type=BreakDown1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=0, max=1, mutex_group=None, array=False),
	))

