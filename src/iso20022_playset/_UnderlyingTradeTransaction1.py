# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODate
from . import Max2000Text
from . import Max35Text
from . import PercentageRate
from . import UnderlyingTradeTransactionType1Choice

class UnderlyingTradeTransaction1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CtrctAmtPctg", "_Id", "_TndrClsgDt", "_Tp", "_TxAmt", "_TxDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def CtrctAmtPctg(self):
		return self._CtrctAmtPctg

	@CtrctAmtPctg.setter
	def CtrctAmtPctg(self, value):
		self._CtrctAmtPctg = value if value is not None else base_types.UninitialisedField(self, 'CtrctAmtPctg', PercentageRate, False)

	@CtrctAmtPctg.deleter
	def CtrctAmtPctg(self):
		del self._CtrctAmtPctg
		self._CtrctAmtPctg = base_types.UninitialisedField(self, 'CtrctAmtPctg', PercentageRate, False)

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
	def TndrClsgDt(self):
		return self._TndrClsgDt

	@TndrClsgDt.setter
	def TndrClsgDt(self, value):
		self._TndrClsgDt = value if value is not None else base_types.UninitialisedField(self, 'TndrClsgDt', ISODate, False)

	@TndrClsgDt.deleter
	def TndrClsgDt(self):
		del self._TndrClsgDt
		self._TndrClsgDt = base_types.UninitialisedField(self, 'TndrClsgDt', ISODate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', UnderlyingTradeTransactionType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', UnderlyingTradeTransactionType1Choice, False)

	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if value is not None else base_types.UninitialisedField(self, 'TxAmt', ActiveCurrencyAndAmount, False)

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = base_types.UninitialisedField(self, 'TxAmt', ActiveCurrencyAndAmount, False)

	@property
	def TxDt(self):
		return self._TxDt

	@TxDt.setter
	def TxDt(self, value):
		self._TxDt = value if value is not None else base_types.UninitialisedField(self, 'TxDt', ISODate, False)

	@TxDt.deleter
	def TxDt(self):
		del self._TxDt
		self._TxDt = base_types.UninitialisedField(self, 'TxDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctAmtPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TndrClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=UnderlyingTradeTransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))