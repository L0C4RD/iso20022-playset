# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import Amount21
from . import Discount3
from . import Distance1
from . import ISODate
from . import ISOTime
from . import LoyaltyProgramme5
from . import Max35NumericText
from . import Max35Text
from . import Max4NumericText
from . import RentalDetails3
from . import RentalRate2
from . import Tax41
from . import TrueFalseIndicator

class VehicleRentalAgreement3(base_types._BaseFieldType):

	__slots__ = ["_AddtlAmt", "_Adjstd", "_ChckInDt", "_ChckInTm", "_ChckOutDt", "_ChckOutTm", "_Clss", "_Drtn", "_DscntPrgrmm", "_EstmtdTax", "_Insrnc", "_LltyPrgrmm", "_Make", "_Mdl", "_Nb", "_PckpLctn", "_RegnNb", "_RntlDtls", "_RntlLctn", "_RntlRate", "_RtrLctn", "_TrvlDstnc"]
	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlAmt', Amount21, True)

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = base_types.UninitialisedField(self, 'AddtlAmt', Amount21, True)

	@property
	def Adjstd(self):
		return self._Adjstd

	@Adjstd.setter
	def Adjstd(self, value):
		self._Adjstd = value if value is not None else base_types.UninitialisedField(self, 'Adjstd', TrueFalseIndicator, False)

	@Adjstd.deleter
	def Adjstd(self):
		del self._Adjstd
		self._Adjstd = base_types.UninitialisedField(self, 'Adjstd', TrueFalseIndicator, False)

	@property
	def ChckInDt(self):
		return self._ChckInDt

	@ChckInDt.setter
	def ChckInDt(self, value):
		self._ChckInDt = value if value is not None else base_types.UninitialisedField(self, 'ChckInDt', ISODate, False)

	@ChckInDt.deleter
	def ChckInDt(self):
		del self._ChckInDt
		self._ChckInDt = base_types.UninitialisedField(self, 'ChckInDt', ISODate, False)

	@property
	def ChckInTm(self):
		return self._ChckInTm

	@ChckInTm.setter
	def ChckInTm(self, value):
		self._ChckInTm = value if value is not None else base_types.UninitialisedField(self, 'ChckInTm', ISOTime, False)

	@ChckInTm.deleter
	def ChckInTm(self):
		del self._ChckInTm
		self._ChckInTm = base_types.UninitialisedField(self, 'ChckInTm', ISOTime, False)

	@property
	def ChckOutDt(self):
		return self._ChckOutDt

	@ChckOutDt.setter
	def ChckOutDt(self, value):
		self._ChckOutDt = value if value is not None else base_types.UninitialisedField(self, 'ChckOutDt', ISODate, False)

	@ChckOutDt.deleter
	def ChckOutDt(self):
		del self._ChckOutDt
		self._ChckOutDt = base_types.UninitialisedField(self, 'ChckOutDt', ISODate, False)

	@property
	def ChckOutTm(self):
		return self._ChckOutTm

	@ChckOutTm.setter
	def ChckOutTm(self, value):
		self._ChckOutTm = value if value is not None else base_types.UninitialisedField(self, 'ChckOutTm', ISOTime, False)

	@ChckOutTm.deleter
	def ChckOutTm(self):
		del self._ChckOutTm
		self._ChckOutTm = base_types.UninitialisedField(self, 'ChckOutTm', ISOTime, False)

	@property
	def Clss(self):
		return self._Clss

	@Clss.setter
	def Clss(self, value):
		self._Clss = value if value is not None else base_types.UninitialisedField(self, 'Clss', Max35Text, False)

	@Clss.deleter
	def Clss(self):
		del self._Clss
		self._Clss = base_types.UninitialisedField(self, 'Clss', Max35Text, False)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@property
	def DscntPrgrmm(self):
		return self._DscntPrgrmm

	@DscntPrgrmm.setter
	def DscntPrgrmm(self, value):
		self._DscntPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'DscntPrgrmm', Discount3, True)

	@DscntPrgrmm.deleter
	def DscntPrgrmm(self):
		del self._DscntPrgrmm
		self._DscntPrgrmm = base_types.UninitialisedField(self, 'DscntPrgrmm', Discount3, True)

	@property
	def EstmtdTax(self):
		return self._EstmtdTax

	@EstmtdTax.setter
	def EstmtdTax(self, value):
		self._EstmtdTax = value if value is not None else base_types.UninitialisedField(self, 'EstmtdTax', Tax41, True)

	@EstmtdTax.deleter
	def EstmtdTax(self):
		del self._EstmtdTax
		self._EstmtdTax = base_types.UninitialisedField(self, 'EstmtdTax', Tax41, True)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme5, True)

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme5, True)

	@property
	def Make(self):
		return self._Make

	@Make.setter
	def Make(self, value):
		self._Make = value if value is not None else base_types.UninitialisedField(self, 'Make', Max35NumericText, False)

	@Make.deleter
	def Make(self):
		del self._Make
		self._Make = base_types.UninitialisedField(self, 'Make', Max35NumericText, False)

	@property
	def Mdl(self):
		return self._Mdl

	@Mdl.setter
	def Mdl(self, value):
		self._Mdl = value if value is not None else base_types.UninitialisedField(self, 'Mdl', Max35NumericText, False)

	@Mdl.deleter
	def Mdl(self):
		del self._Mdl
		self._Mdl = base_types.UninitialisedField(self, 'Mdl', Max35NumericText, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max35Text, False)

	@property
	def PckpLctn(self):
		return self._PckpLctn

	@PckpLctn.setter
	def PckpLctn(self, value):
		self._PckpLctn = value if value is not None else base_types.UninitialisedField(self, 'PckpLctn', Address2, True)

	@PckpLctn.deleter
	def PckpLctn(self):
		del self._PckpLctn
		self._PckpLctn = base_types.UninitialisedField(self, 'PckpLctn', Address2, True)

	@property
	def RegnNb(self):
		return self._RegnNb

	@RegnNb.setter
	def RegnNb(self, value):
		self._RegnNb = value if value is not None else base_types.UninitialisedField(self, 'RegnNb', Max35Text, False)

	@RegnNb.deleter
	def RegnNb(self):
		del self._RegnNb
		self._RegnNb = base_types.UninitialisedField(self, 'RegnNb', Max35Text, False)

	@property
	def RntlDtls(self):
		return self._RntlDtls

	@RntlDtls.setter
	def RntlDtls(self, value):
		self._RntlDtls = value if value is not None else base_types.UninitialisedField(self, 'RntlDtls', RentalDetails3, False)

	@RntlDtls.deleter
	def RntlDtls(self):
		del self._RntlDtls
		self._RntlDtls = base_types.UninitialisedField(self, 'RntlDtls', RentalDetails3, False)

	@property
	def RntlLctn(self):
		return self._RntlLctn

	@RntlLctn.setter
	def RntlLctn(self, value):
		self._RntlLctn = value if value is not None else base_types.UninitialisedField(self, 'RntlLctn', Address2, False)

	@RntlLctn.deleter
	def RntlLctn(self):
		del self._RntlLctn
		self._RntlLctn = base_types.UninitialisedField(self, 'RntlLctn', Address2, False)

	@property
	def RntlRate(self):
		return self._RntlRate

	@RntlRate.setter
	def RntlRate(self, value):
		self._RntlRate = value if value is not None else base_types.UninitialisedField(self, 'RntlRate', RentalRate2, True)

	@RntlRate.deleter
	def RntlRate(self):
		del self._RntlRate
		self._RntlRate = base_types.UninitialisedField(self, 'RntlRate', RentalRate2, True)

	@property
	def RtrLctn(self):
		return self._RtrLctn

	@RtrLctn.setter
	def RtrLctn(self, value):
		self._RtrLctn = value if value is not None else base_types.UninitialisedField(self, 'RtrLctn', Address2, False)

	@RtrLctn.deleter
	def RtrLctn(self):
		del self._RtrLctn
		self._RtrLctn = base_types.UninitialisedField(self, 'RtrLctn', Address2, False)

	@property
	def TrvlDstnc(self):
		return self._TrvlDstnc

	@TrvlDstnc.setter
	def TrvlDstnc(self, value):
		self._TrvlDstnc = value if value is not None else base_types.UninitialisedField(self, 'TrvlDstnc', Distance1, False)

	@TrvlDstnc.deleter
	def TrvlDstnc(self):
		del self._TrvlDstnc
		self._TrvlDstnc = base_types.UninitialisedField(self, 'TrvlDstnc', Distance1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAmt', type=Amount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adjstd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckOutDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckOutTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clss', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntPrgrmm', type=Discount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdTax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Make', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdl', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PckpLctn', type=Address2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlDtls', type=RentalDetails3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlLctn', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlRate', type=RentalRate2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtrLctn', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrvlDstnc', type=Distance1, min=0, max=1, mutex_group=None, array=False),
	))