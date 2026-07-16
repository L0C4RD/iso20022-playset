# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max256Text
from . import Max70Text
from . import TrueFalseIndicator

class ATMAccountStatement2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_CdtTx", "_LngTxt", "_ShrtTxt", "_TxDt", "_ValDt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CdtTx(self):
		return self._CdtTx

	@CdtTx.setter
	def CdtTx(self, value):
		self._CdtTx = value if value is not None else base_types.UninitialisedField(self, 'CdtTx', TrueFalseIndicator, False)

	@CdtTx.deleter
	def CdtTx(self):
		del self._CdtTx
		self._CdtTx = base_types.UninitialisedField(self, 'CdtTx', TrueFalseIndicator, False)

	@property
	def LngTxt(self):
		return self._LngTxt

	@LngTxt.setter
	def LngTxt(self, value):
		self._LngTxt = value if value is not None else base_types.UninitialisedField(self, 'LngTxt', Max256Text, False)

	@LngTxt.deleter
	def LngTxt(self):
		del self._LngTxt
		self._LngTxt = base_types.UninitialisedField(self, 'LngTxt', Max256Text, False)

	@property
	def ShrtTxt(self):
		return self._ShrtTxt

	@ShrtTxt.setter
	def ShrtTxt(self, value):
		self._ShrtTxt = value if value is not None else base_types.UninitialisedField(self, 'ShrtTxt', Max70Text, False)

	@ShrtTxt.deleter
	def ShrtTxt(self):
		del self._ShrtTxt
		self._ShrtTxt = base_types.UninitialisedField(self, 'ShrtTxt', Max70Text, False)

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

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LngTxt', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtTxt', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))