# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BaseOne25Rate import BaseOne25Rate
from ._DetailedAmount22 import DetailedAmount22
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._TypeOfAmount22Code import TypeOfAmount22Code

class TransactionAmounts4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtQlfr", "_Ccy", "_CrdhldrBllgAmt", "_CrdhldrBllgCcy", "_CrdhldrBllgFctvXchgRate", "_DtldAmt", "_RcncltnAmt", "_RcncltnCcy", "_RcncltnFctvXchgRate"]
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
	def AmtQlfr(self):
		return self._AmtQlfr

	@AmtQlfr.setter
	def AmtQlfr(self, value):
		self._AmtQlfr = value if type(value) != base_types.auto else self.make_default("AmtQlfr")

	@AmtQlfr.deleter
	def AmtQlfr(self):
		del self._AmtQlfr
		self._AmtQlfr = None

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
	def CrdhldrBllgAmt(self):
		return self._CrdhldrBllgAmt

	@CrdhldrBllgAmt.setter
	def CrdhldrBllgAmt(self, value):
		self._CrdhldrBllgAmt = value if type(value) != base_types.auto else self.make_default("CrdhldrBllgAmt")

	@CrdhldrBllgAmt.deleter
	def CrdhldrBllgAmt(self):
		del self._CrdhldrBllgAmt
		self._CrdhldrBllgAmt = None

	@property
	def CrdhldrBllgCcy(self):
		return self._CrdhldrBllgCcy

	@CrdhldrBllgCcy.setter
	def CrdhldrBllgCcy(self, value):
		self._CrdhldrBllgCcy = value if type(value) != base_types.auto else self.make_default("CrdhldrBllgCcy")

	@CrdhldrBllgCcy.deleter
	def CrdhldrBllgCcy(self):
		del self._CrdhldrBllgCcy
		self._CrdhldrBllgCcy = None

	@property
	def CrdhldrBllgFctvXchgRate(self):
		return self._CrdhldrBllgFctvXchgRate

	@CrdhldrBllgFctvXchgRate.setter
	def CrdhldrBllgFctvXchgRate(self, value):
		self._CrdhldrBllgFctvXchgRate = value if type(value) != base_types.auto else self.make_default("CrdhldrBllgFctvXchgRate")

	@CrdhldrBllgFctvXchgRate.deleter
	def CrdhldrBllgFctvXchgRate(self):
		del self._CrdhldrBllgFctvXchgRate
		self._CrdhldrBllgFctvXchgRate = None

	@property
	def DtldAmt(self):
		return self._DtldAmt

	@DtldAmt.setter
	def DtldAmt(self, value):
		self._DtldAmt = value if type(value) != base_types.auto else self.make_default("DtldAmt")

	@DtldAmt.deleter
	def DtldAmt(self):
		del self._DtldAmt
		self._DtldAmt = None

	@property
	def RcncltnAmt(self):
		return self._RcncltnAmt

	@RcncltnAmt.setter
	def RcncltnAmt(self, value):
		self._RcncltnAmt = value if type(value) != base_types.auto else self.make_default("RcncltnAmt")

	@RcncltnAmt.deleter
	def RcncltnAmt(self):
		del self._RcncltnAmt
		self._RcncltnAmt = None

	@property
	def RcncltnCcy(self):
		return self._RcncltnCcy

	@RcncltnCcy.setter
	def RcncltnCcy(self, value):
		self._RcncltnCcy = value if type(value) != base_types.auto else self.make_default("RcncltnCcy")

	@RcncltnCcy.deleter
	def RcncltnCcy(self):
		del self._RcncltnCcy
		self._RcncltnCcy = None

	@property
	def RcncltnFctvXchgRate(self):
		return self._RcncltnFctvXchgRate

	@RcncltnFctvXchgRate.setter
	def RcncltnFctvXchgRate(self, value):
		self._RcncltnFctvXchgRate = value if type(value) != base_types.auto else self.make_default("RcncltnFctvXchgRate")

	@RcncltnFctvXchgRate.deleter
	def RcncltnFctvXchgRate(self):
		del self._RcncltnFctvXchgRate
		self._RcncltnFctvXchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtQlfr', type=TypeOfAmount22Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgFctvXchgRate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldAmt', type=DetailedAmount22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcncltnAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFctvXchgRate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
	))