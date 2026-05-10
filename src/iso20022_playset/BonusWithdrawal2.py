from . import base_types
from .WithdrawalReason1Choice import WithdrawalReason1Choice
from .YesNoIndicator import YesNoIndicator
from .ActiveOrHistoricCurrencyAnd13DecimalAmount import ActiveOrHistoricCurrencyAnd13DecimalAmount
from .AdditionalInformation15 import AdditionalInformation15
from .TypeOfAmount1Choice import TypeOfAmount1Choice
from .Max35Text import Max35Text

class BonusWithdrawal2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Rsn", "_UclmdAmt", "_TpOfAmt", "_Outsdng", "_Ref", "_AddtlInf"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def UclmdAmt(self):
		return self._UclmdAmt

	@UclmdAmt.setter
	def UclmdAmt(self, value):
		self._UclmdAmt = value if type(value) != base_types.auto else self.make_default("UclmdAmt")

	@UclmdAmt.deleter
	def UclmdAmt(self):
		del self._UclmdAmt
		self._UclmdAmt = None

	@property
	def TpOfAmt(self):
		return self._TpOfAmt

	@TpOfAmt.setter
	def TpOfAmt(self, value):
		self._TpOfAmt = value if type(value) != base_types.auto else self.make_default("TpOfAmt")

	@TpOfAmt.deleter
	def TpOfAmt(self):
		del self._TpOfAmt
		self._TpOfAmt = None

	@property
	def Outsdng(self):
		return self._Outsdng

	@Outsdng.setter
	def Outsdng(self, value):
		self._Outsdng = value if type(value) != base_types.auto else self.make_default("Outsdng")

	@Outsdng.deleter
	def Outsdng(self):
		del self._Outsdng
		self._Outsdng = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=WithdrawalReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UclmdAmt', type=ActiveOrHistoricCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfAmt', type=TypeOfAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Outsdng', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

