from . import base_types
from ._Amount21 import Amount21
from ._Max35NumericText import Max35NumericText
from ._Max4NumericText import Max4NumericText
from ._RentalDetails3 import RentalDetails3
from ._RentalRate2 import RentalRate2
from ._Distance1 import Distance1
from ._LoyaltyProgramme5 import LoyaltyProgramme5
from ._ISOTime import ISOTime
from ._Tax41 import Tax41
from ._TrueFalseIndicator import TrueFalseIndicator
from ._Discount3 import Discount3
from ._Max35Text import Max35Text
from ._Address2 import Address2
from ._ISODate import ISODate

class VehicleRentalAgreement3(base_types._BaseFieldType):

	__slots__ = ["_ChckOutDt", "_RtrLctn", "_Clss", "_Insrnc", "_PckpLctn", "_RntlRate", "_ChckOutTm", "_LltyPrgrmm", "_Drtn", "_RntlDtls", "_TrvlDstnc", "_EstmtdTax", "_RntlLctn", "_AddtlAmt", "_Adjstd", "_Nb", "_RegnNb", "_DscntPrgrmm", "_Mdl", "_Make", "_ChckInTm", "_ChckInDt"]
	@property
	def ChckOutDt(self):
		return self._ChckOutDt

	@ChckOutDt.setter
	def ChckOutDt(self, value):
		self._ChckOutDt = value if type(value) != base_types.auto else self.make_default("ChckOutDt")

	@ChckOutDt.deleter
	def ChckOutDt(self):
		del self._ChckOutDt
		self._ChckOutDt = None

	@property
	def RtrLctn(self):
		return self._RtrLctn

	@RtrLctn.setter
	def RtrLctn(self, value):
		self._RtrLctn = value if type(value) != base_types.auto else self.make_default("RtrLctn")

	@RtrLctn.deleter
	def RtrLctn(self):
		del self._RtrLctn
		self._RtrLctn = None

	@property
	def Clss(self):
		return self._Clss

	@Clss.setter
	def Clss(self, value):
		self._Clss = value if type(value) != base_types.auto else self.make_default("Clss")

	@Clss.deleter
	def Clss(self):
		del self._Clss
		self._Clss = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != base_types.auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def PckpLctn(self):
		return self._PckpLctn

	@PckpLctn.setter
	def PckpLctn(self, value):
		self._PckpLctn = value if type(value) != base_types.auto else self.make_default("PckpLctn")

	@PckpLctn.deleter
	def PckpLctn(self):
		del self._PckpLctn
		self._PckpLctn = None

	@property
	def RntlRate(self):
		return self._RntlRate

	@RntlRate.setter
	def RntlRate(self, value):
		self._RntlRate = value if type(value) != base_types.auto else self.make_default("RntlRate")

	@RntlRate.deleter
	def RntlRate(self):
		del self._RntlRate
		self._RntlRate = None

	@property
	def ChckOutTm(self):
		return self._ChckOutTm

	@ChckOutTm.setter
	def ChckOutTm(self, value):
		self._ChckOutTm = value if type(value) != base_types.auto else self.make_default("ChckOutTm")

	@ChckOutTm.deleter
	def ChckOutTm(self):
		del self._ChckOutTm
		self._ChckOutTm = None

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if type(value) != base_types.auto else self.make_default("LltyPrgrmm")

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def RntlDtls(self):
		return self._RntlDtls

	@RntlDtls.setter
	def RntlDtls(self, value):
		self._RntlDtls = value if type(value) != base_types.auto else self.make_default("RntlDtls")

	@RntlDtls.deleter
	def RntlDtls(self):
		del self._RntlDtls
		self._RntlDtls = None

	@property
	def TrvlDstnc(self):
		return self._TrvlDstnc

	@TrvlDstnc.setter
	def TrvlDstnc(self, value):
		self._TrvlDstnc = value if type(value) != base_types.auto else self.make_default("TrvlDstnc")

	@TrvlDstnc.deleter
	def TrvlDstnc(self):
		del self._TrvlDstnc
		self._TrvlDstnc = None

	@property
	def EstmtdTax(self):
		return self._EstmtdTax

	@EstmtdTax.setter
	def EstmtdTax(self, value):
		self._EstmtdTax = value if type(value) != base_types.auto else self.make_default("EstmtdTax")

	@EstmtdTax.deleter
	def EstmtdTax(self):
		del self._EstmtdTax
		self._EstmtdTax = None

	@property
	def RntlLctn(self):
		return self._RntlLctn

	@RntlLctn.setter
	def RntlLctn(self, value):
		self._RntlLctn = value if type(value) != base_types.auto else self.make_default("RntlLctn")

	@RntlLctn.deleter
	def RntlLctn(self):
		del self._RntlLctn
		self._RntlLctn = None

	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if type(value) != base_types.auto else self.make_default("AddtlAmt")

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = None

	@property
	def Adjstd(self):
		return self._Adjstd

	@Adjstd.setter
	def Adjstd(self, value):
		self._Adjstd = value if type(value) != base_types.auto else self.make_default("Adjstd")

	@Adjstd.deleter
	def Adjstd(self):
		del self._Adjstd
		self._Adjstd = None

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def RegnNb(self):
		return self._RegnNb

	@RegnNb.setter
	def RegnNb(self, value):
		self._RegnNb = value if type(value) != base_types.auto else self.make_default("RegnNb")

	@RegnNb.deleter
	def RegnNb(self):
		del self._RegnNb
		self._RegnNb = None

	@property
	def DscntPrgrmm(self):
		return self._DscntPrgrmm

	@DscntPrgrmm.setter
	def DscntPrgrmm(self, value):
		self._DscntPrgrmm = value if type(value) != base_types.auto else self.make_default("DscntPrgrmm")

	@DscntPrgrmm.deleter
	def DscntPrgrmm(self):
		del self._DscntPrgrmm
		self._DscntPrgrmm = None

	@property
	def Mdl(self):
		return self._Mdl

	@Mdl.setter
	def Mdl(self, value):
		self._Mdl = value if type(value) != base_types.auto else self.make_default("Mdl")

	@Mdl.deleter
	def Mdl(self):
		del self._Mdl
		self._Mdl = None

	@property
	def Make(self):
		return self._Make

	@Make.setter
	def Make(self, value):
		self._Make = value if type(value) != base_types.auto else self.make_default("Make")

	@Make.deleter
	def Make(self):
		del self._Make
		self._Make = None

	@property
	def ChckInTm(self):
		return self._ChckInTm

	@ChckInTm.setter
	def ChckInTm(self, value):
		self._ChckInTm = value if type(value) != base_types.auto else self.make_default("ChckInTm")

	@ChckInTm.deleter
	def ChckInTm(self):
		del self._ChckInTm
		self._ChckInTm = None

	@property
	def ChckInDt(self):
		return self._ChckInDt

	@ChckInDt.setter
	def ChckInDt(self, value):
		self._ChckInDt = value if type(value) != base_types.auto else self.make_default("ChckInDt")

	@ChckInDt.deleter
	def ChckInDt(self):
		del self._ChckInDt
		self._ChckInDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChckOutDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrLctn', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clss', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PckpLctn', type=Address2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RntlRate', type=RentalRate2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChckOutTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RntlDtls', type=RentalDetails3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrvlDstnc', type=Distance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RntlLctn', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAmt', type=Amount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adjstd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntPrgrmm', type=Discount3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mdl', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Make', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

