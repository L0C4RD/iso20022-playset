# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BreakDown1Choice
from . import ISODate
from . import SettlementTerms3

class IntentToPay2(base_types._BaseFieldType):

	__slots__ = ["_Brkdwn", "_SttlmTerms", "_XpctdPmtDt"]
	@property
	def Brkdwn(self):
		return self._Brkdwn

	@Brkdwn.setter
	def Brkdwn(self, value):
		self._Brkdwn = value if value is not None else base_types.UninitialisedField(self, 'Brkdwn', BreakDown1Choice, False)

	@Brkdwn.deleter
	def Brkdwn(self):
		del self._Brkdwn
		self._Brkdwn = base_types.UninitialisedField(self, 'Brkdwn', BreakDown1Choice, False)

	@property
	def SttlmTerms(self):
		return self._SttlmTerms

	@SttlmTerms.setter
	def SttlmTerms(self, value):
		self._SttlmTerms = value if value is not None else base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	@SttlmTerms.deleter
	def SttlmTerms(self):
		del self._SttlmTerms
		self._SttlmTerms = base_types.UninitialisedField(self, 'SttlmTerms', SettlementTerms3, False)

	@property
	def XpctdPmtDt(self):
		return self._XpctdPmtDt

	@XpctdPmtDt.setter
	def XpctdPmtDt(self, value):
		self._XpctdPmtDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdPmtDt', ISODate, False)

	@XpctdPmtDt.deleter
	def XpctdPmtDt(self):
		del self._XpctdPmtDt
		self._XpctdPmtDt = base_types.UninitialisedField(self, 'XpctdPmtDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brkdwn', type=BreakDown1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTerms', type=SettlementTerms3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdPmtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))