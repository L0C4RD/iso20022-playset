# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ISODate import ISODate
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max256Text import Max256Text
from ._Max70Text import Max70Text
from ._TrueFalseIndicator import TrueFalseIndicator

class ATMAccountStatement2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_CdtTx", "_LngTxt", "_ShrtTxt", "_TxDt", "_ValDt"]
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
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CdtTx(self):
		return self._CdtTx

	@CdtTx.setter
	def CdtTx(self, value):
		self._CdtTx = value if type(value) != base_types.auto else self.make_default("CdtTx")

	@CdtTx.deleter
	def CdtTx(self):
		del self._CdtTx
		self._CdtTx = None

	@property
	def LngTxt(self):
		return self._LngTxt

	@LngTxt.setter
	def LngTxt(self, value):
		self._LngTxt = value if type(value) != base_types.auto else self.make_default("LngTxt")

	@LngTxt.deleter
	def LngTxt(self):
		del self._LngTxt
		self._LngTxt = None

	@property
	def ShrtTxt(self):
		return self._ShrtTxt

	@ShrtTxt.setter
	def ShrtTxt(self, value):
		self._ShrtTxt = value if type(value) != base_types.auto else self.make_default("ShrtTxt")

	@ShrtTxt.deleter
	def ShrtTxt(self):
		del self._ShrtTxt
		self._ShrtTxt = None

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
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtTx', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LngTxt', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtTxt', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))