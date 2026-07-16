# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection5
from . import CashAccount40
from . import Max35Text
from . import Number
from . import PartyIdentification272

class MovementRecord2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Id", "_Ptcpt", "_PtcptAcct", "_Ref", "_SeqNb", "_SttlmAgt", "_SttlmAgtAcct"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountAndDirection5, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountAndDirection5, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def Ptcpt(self):
		return self._Ptcpt

	@Ptcpt.setter
	def Ptcpt(self, value):
		self._Ptcpt = value if value is not None else base_types.UninitialisedField(self, 'Ptcpt', PartyIdentification272, False)

	@Ptcpt.deleter
	def Ptcpt(self):
		del self._Ptcpt
		self._Ptcpt = base_types.UninitialisedField(self, 'Ptcpt', PartyIdentification272, False)

	@property
	def PtcptAcct(self):
		return self._PtcptAcct

	@PtcptAcct.setter
	def PtcptAcct(self, value):
		self._PtcptAcct = value if value is not None else base_types.UninitialisedField(self, 'PtcptAcct', CashAccount40, False)

	@PtcptAcct.deleter
	def PtcptAcct(self):
		del self._PtcptAcct
		self._PtcptAcct = base_types.UninitialisedField(self, 'PtcptAcct', CashAccount40, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@property
	def SttlmAgt(self):
		return self._SttlmAgt

	@SttlmAgt.setter
	def SttlmAgt(self, value):
		self._SttlmAgt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAgt', PartyIdentification272, False)

	@SttlmAgt.deleter
	def SttlmAgt(self):
		del self._SttlmAgt
		self._SttlmAgt = base_types.UninitialisedField(self, 'SttlmAgt', PartyIdentification272, False)

	@property
	def SttlmAgtAcct(self):
		return self._SttlmAgtAcct

	@SttlmAgtAcct.setter
	def SttlmAgtAcct(self, value):
		self._SttlmAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'SttlmAgtAcct', CashAccount40, False)

	@SttlmAgtAcct.deleter
	def SttlmAgtAcct(self):
		del self._SttlmAgtAcct
		self._SttlmAgtAcct = base_types.UninitialisedField(self, 'SttlmAgtAcct', CashAccount40, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountAndDirection5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ptcpt', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAgt', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))