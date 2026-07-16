# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOne25Rate
from . import CreditDebit3Code
from . import ISO3NumericCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Max140Text
from . import Max35Text
from . import PartyType32Code
from . import TypeOfAmount21Code

class AdditionalFee3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Assgnr", "_Ccy", "_CdtDbt", "_Desc", "_Dscrptr", "_OthrAssgnr", "_OthrTp", "_Prgm", "_RcncltnAmt", "_RcncltnCcy", "_RcncltnFctvXchgRate", "_Tp"]
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
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', PartyType32Code, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', PartyType32Code, False)

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
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def Dscrptr(self):
		return self._Dscrptr

	@Dscrptr.setter
	def Dscrptr(self, value):
		self._Dscrptr = value if value is not None else base_types.UninitialisedField(self, 'Dscrptr', Max35Text, False)

	@Dscrptr.deleter
	def Dscrptr(self):
		del self._Dscrptr
		self._Dscrptr = base_types.UninitialisedField(self, 'Dscrptr', Max35Text, False)

	@property
	def OthrAssgnr(self):
		return self._OthrAssgnr

	@OthrAssgnr.setter
	def OthrAssgnr(self, value):
		self._OthrAssgnr = value if value is not None else base_types.UninitialisedField(self, 'OthrAssgnr', Max35Text, False)

	@OthrAssgnr.deleter
	def OthrAssgnr(self):
		del self._OthrAssgnr
		self._OthrAssgnr = base_types.UninitialisedField(self, 'OthrAssgnr', Max35Text, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def Prgm(self):
		return self._Prgm

	@Prgm.setter
	def Prgm(self, value):
		self._Prgm = value if value is not None else base_types.UninitialisedField(self, 'Prgm', Max35Text, False)

	@Prgm.deleter
	def Prgm(self):
		del self._Prgm
		self._Prgm = base_types.UninitialisedField(self, 'Prgm', Max35Text, False)

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

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeOfAmount21Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeOfAmount21Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=PartyType32Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dscrptr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prgm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnFctvXchgRate', type=BaseOne25Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeOfAmount21Code, min=1, max=1, mutex_group=None, array=False),
	))