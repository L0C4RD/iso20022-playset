# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import ISODateTime
from . import Max15NumericText
from . import Max35Text
from . import SettlementInstruction14

class GroupHeader104(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_CtrlSum", "_MsgId", "_NbOfSttlmReqs", "_SttlmInf"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if value is not None else base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def NbOfSttlmReqs(self):
		return self._NbOfSttlmReqs

	@NbOfSttlmReqs.setter
	def NbOfSttlmReqs(self, value):
		self._NbOfSttlmReqs = value if value is not None else base_types.UninitialisedField(self, 'NbOfSttlmReqs', Max15NumericText, False)

	@NbOfSttlmReqs.deleter
	def NbOfSttlmReqs(self):
		del self._NbOfSttlmReqs
		self._NbOfSttlmReqs = base_types.UninitialisedField(self, 'NbOfSttlmReqs', Max15NumericText, False)

	@property
	def SttlmInf(self):
		return self._SttlmInf

	@SttlmInf.setter
	def SttlmInf(self, value):
		self._SttlmInf = value if value is not None else base_types.UninitialisedField(self, 'SttlmInf', SettlementInstruction14, False)

	@SttlmInf.deleter
	def SttlmInf(self):
		del self._SttlmInf
		self._SttlmInf = base_types.UninitialisedField(self, 'SttlmInf', SettlementInstruction14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfSttlmReqs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInf', type=SettlementInstruction14, min=0, max=1, mutex_group=None, array=False),
	))