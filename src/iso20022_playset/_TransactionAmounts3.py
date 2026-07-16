# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOne25Rate
from . import DetailedAmount22
from . import ISO3NumericCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import TypeOfAmount22Code

class TransactionAmounts3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtQlfr", "_Ccy", "_CrdhldrBllgAmt", "_CrdhldrBllgCcy", "_CrdhldrBllgFctvXchgRate", "_DtldAmt", "_RcncltnAmt", "_RcncltnCcy", "_RcncltnFctvXchgRate"]
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
	def AmtQlfr(self):
		return self._AmtQlfr

	@AmtQlfr.setter
	def AmtQlfr(self, value):
		self._AmtQlfr = value if value is not None else base_types.UninitialisedField(self, 'AmtQlfr', TypeOfAmount22Code, False)

	@AmtQlfr.deleter
	def AmtQlfr(self):
		del self._AmtQlfr
		self._AmtQlfr = base_types.UninitialisedField(self, 'AmtQlfr', TypeOfAmount22Code, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@property
	def CrdhldrBllgAmt(self):
		return self._CrdhldrBllgAmt

	@CrdhldrBllgAmt.setter
	def CrdhldrBllgAmt(self, value):
		self._CrdhldrBllgAmt = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrBllgAmt', ImpliedCurrencyAndAmount, False)

	@CrdhldrBllgAmt.deleter
	def CrdhldrBllgAmt(self):
		del self._CrdhldrBllgAmt
		self._CrdhldrBllgAmt = base_types.UninitialisedField(self, 'CrdhldrBllgAmt', ImpliedCurrencyAndAmount, False)

	@property
	def CrdhldrBllgCcy(self):
		return self._CrdhldrBllgCcy

	@CrdhldrBllgCcy.setter
	def CrdhldrBllgCcy(self, value):
		self._CrdhldrBllgCcy = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrBllgCcy', ISO3NumericCurrencyCode, False)

	@CrdhldrBllgCcy.deleter
	def CrdhldrBllgCcy(self):
		del self._CrdhldrBllgCcy
		self._CrdhldrBllgCcy = base_types.UninitialisedField(self, 'CrdhldrBllgCcy', ISO3NumericCurrencyCode, False)

	@property
	def CrdhldrBllgFctvXchgRate(self):
		return self._CrdhldrBllgFctvXchgRate

	@CrdhldrBllgFctvXchgRate.setter
	def CrdhldrBllgFctvXchgRate(self, value):
		self._CrdhldrBllgFctvXchgRate = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrBllgFctvXchgRate', BaseOne25Rate, False)

	@CrdhldrBllgFctvXchgRate.deleter
	def CrdhldrBllgFctvXchgRate(self):
		del self._CrdhldrBllgFctvXchgRate
		self._CrdhldrBllgFctvXchgRate = base_types.UninitialisedField(self, 'CrdhldrBllgFctvXchgRate', BaseOne25Rate, False)

	@property
	def DtldAmt(self):
		return self._DtldAmt

	@DtldAmt.setter
	def DtldAmt(self, value):
		self._DtldAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldAmt', DetailedAmount22, True)

	@DtldAmt.deleter
	def DtldAmt(self):
		del self._DtldAmt
		self._DtldAmt = base_types.UninitialisedField(self, 'DtldAmt', DetailedAmount22, True)

	@property
	def RcncltnAmt(self):
		return self._RcncltnAmt

	@RcncltnAmt.setter
	def RcncltnAmt(self, value):
		self._RcncltnAmt = value if value is not None else base_types.UninitialisedField(self, 'RcncltnAmt', ImpliedCurrencyAndAmount, False)

	@RcncltnAmt.deleter
	def RcncltnAmt(self):
		del self._RcncltnAmt
		self._RcncltnAmt = base_types.UninitialisedField(self, 'RcncltnAmt', ImpliedCurrencyAndAmount, False)

	@property
	def RcncltnCcy(self):
		return self._RcncltnCcy

	@RcncltnCcy.setter
	def RcncltnCcy(self, value):
		self._RcncltnCcy = value if value is not None else base_types.UninitialisedField(self, 'RcncltnCcy', ISO3NumericCurrencyCode, False)

	@RcncltnCcy.deleter
	def RcncltnCcy(self):
		del self._RcncltnCcy
		self._RcncltnCcy = base_types.UninitialisedField(self, 'RcncltnCcy', ISO3NumericCurrencyCode, False)

	@property
	def RcncltnFctvXchgRate(self):
		return self._RcncltnFctvXchgRate

	@RcncltnFctvXchgRate.setter
	def RcncltnFctvXchgRate(self, value):
		self._RcncltnFctvXchgRate = value if value is not None else base_types.UninitialisedField(self, 'RcncltnFctvXchgRate', BaseOne25Rate, False)

	@RcncltnFctvXchgRate.deleter
	def RcncltnFctvXchgRate(self):
		del self._RcncltnFctvXchgRate
		self._RcncltnFctvXchgRate = base_types.UninitialisedField(self, 'RcncltnFctvXchgRate', BaseOne25Rate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtQlfr', type=TypeOfAmount22Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgFctvXchgRate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldAmt', type=DetailedAmount22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFctvXchgRate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
	))