# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAnd13DecimalAmount
from . import AdditionalInformation15
from . import Max35Text
from . import TypeOfAmount1Choice
from . import WithdrawalReason1Choice
from . import YesNoIndicator

class BonusWithdrawal2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Amt", "_Outsdng", "_Ref", "_Rsn", "_TpOfAmt", "_UclmdAmt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@property
	def Outsdng(self):
		return self._Outsdng

	@Outsdng.setter
	def Outsdng(self, value):
		self._Outsdng = value if value is not None else base_types.UninitialisedField(self, 'Outsdng', YesNoIndicator, False)

	@Outsdng.deleter
	def Outsdng(self):
		del self._Outsdng
		self._Outsdng = base_types.UninitialisedField(self, 'Outsdng', YesNoIndicator, False)

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
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', WithdrawalReason1Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', WithdrawalReason1Choice, False)

	@property
	def TpOfAmt(self):
		return self._TpOfAmt

	@TpOfAmt.setter
	def TpOfAmt(self, value):
		self._TpOfAmt = value if value is not None else base_types.UninitialisedField(self, 'TpOfAmt', TypeOfAmount1Choice, False)

	@TpOfAmt.deleter
	def TpOfAmt(self):
		del self._TpOfAmt
		self._TpOfAmt = base_types.UninitialisedField(self, 'TpOfAmt', TypeOfAmount1Choice, False)

	@property
	def UclmdAmt(self):
		return self._UclmdAmt

	@UclmdAmt.setter
	def UclmdAmt(self, value):
		self._UclmdAmt = value if value is not None else base_types.UninitialisedField(self, 'UclmdAmt', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	@UclmdAmt.deleter
	def UclmdAmt(self):
		del self._UclmdAmt
		self._UclmdAmt = base_types.UninitialisedField(self, 'UclmdAmt', ActiveOrHistoricCurrencyAnd13DecimalAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Outsdng', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=WithdrawalReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfAmt', type=TypeOfAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UclmdAmt', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
	))