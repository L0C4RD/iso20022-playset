from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._UnderlyingTradeTransactionType1Choice import UnderlyingTradeTransactionType1Choice
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate
from ._Max2000Text import Max2000Text

class UnderlyingTradeTransaction1(base_types._BaseFieldType):

	__slots__ = ["_CtrctAmtPctg", "_Tp", "_TxDt", "_Id", "_TxAmt", "_TndrClsgDt", "_AddtlInf"]
	@property
	def CtrctAmtPctg(self):
		return self._CtrctAmtPctg

	@CtrctAmtPctg.setter
	def CtrctAmtPctg(self, value):
		self._CtrctAmtPctg = value if type(value) != base_types.auto else self.make_default("CtrctAmtPctg")

	@CtrctAmtPctg.deleter
	def CtrctAmtPctg(self):
		del self._CtrctAmtPctg
		self._CtrctAmtPctg = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def TxDt(self):
		return self._TxDt

	@TxDt.setter
	def TxDt(self, value):
		self._TxDt = value if type(value) != base_types.auto else self.make_default("TxDt")

	@TxDt.deleter
	def TxDt(self):
		del self._TxDt
		self._TxDt = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if type(value) != base_types.auto else self.make_default("TxAmt")

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = None

	@property
	def TndrClsgDt(self):
		return self._TndrClsgDt

	@TndrClsgDt.setter
	def TndrClsgDt(self, value):
		self._TndrClsgDt = value if type(value) != base_types.auto else self.make_default("TndrClsgDt")

	@TndrClsgDt.deleter
	def TndrClsgDt(self):
		del self._TndrClsgDt
		self._TndrClsgDt = None

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
		base_types.FieldEntry(name='CtrctAmtPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=UnderlyingTradeTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TndrClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

