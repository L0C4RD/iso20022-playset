from . import base_types
import Max40Text
import TrueFalseIndicator
import Max6NumericText
import ISODateTime
import Max35Text
import ShippingPackage3
import Tax41
import ImpliedCurrencyAndAmount
import AdditionalData1
import Max70Text

class ShippingData3(base_types._BaseFieldType):

	__slots__ = ["_InvcNb", "_InvcCreDtTm", "_Tax", "_SvcDscrptrCd", "_SummryCmmdtyId", "_Insrnc", "_NetAmt", "_Packg", "_MiscExpnss", "_AddtlData", "_InsrncAmt", "_IncntivAmt", "_NbOfPackgs"]
	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if type(value) != auto else self.make_default("InvcNb")

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = None

	@property
	def InvcCreDtTm(self):
		return self._InvcCreDtTm

	@InvcCreDtTm.setter
	def InvcCreDtTm(self, value):
		self._InvcCreDtTm = value if type(value) != auto else self.make_default("InvcCreDtTm")

	@InvcCreDtTm.deleter
	def InvcCreDtTm(self):
		del self._InvcCreDtTm
		self._InvcCreDtTm = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def SvcDscrptrCd(self):
		return self._SvcDscrptrCd

	@SvcDscrptrCd.setter
	def SvcDscrptrCd(self, value):
		self._SvcDscrptrCd = value if type(value) != auto else self.make_default("SvcDscrptrCd")

	@SvcDscrptrCd.deleter
	def SvcDscrptrCd(self):
		del self._SvcDscrptrCd
		self._SvcDscrptrCd = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if type(value) != auto else self.make_default("Packg")

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = None

	@property
	def MiscExpnss(self):
		return self._MiscExpnss

	@MiscExpnss.setter
	def MiscExpnss(self, value):
		self._MiscExpnss = value if type(value) != auto else self.make_default("MiscExpnss")

	@MiscExpnss.deleter
	def MiscExpnss(self):
		del self._MiscExpnss
		self._MiscExpnss = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if type(value) != auto else self.make_default("InsrncAmt")

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = None

	@property
	def IncntivAmt(self):
		return self._IncntivAmt

	@IncntivAmt.setter
	def IncntivAmt(self, value):
		self._IncntivAmt = value if type(value) != auto else self.make_default("IncntivAmt")

	@IncntivAmt.deleter
	def IncntivAmt(self):
		del self._IncntivAmt
		self._IncntivAmt = None

	@property
	def NbOfPackgs(self):
		return self._NbOfPackgs

	@NbOfPackgs.setter
	def NbOfPackgs(self, value):
		self._NbOfPackgs = value if type(value) != auto else self.make_default("NbOfPackgs")

	@NbOfPackgs.deleter
	def NbOfPackgs(self):
		del self._NbOfPackgs
		self._NbOfPackgs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvcNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcCreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcDscrptrCd', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Packg', type=ShippingPackage3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MiscExpnss', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncntivAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfPackgs', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
	))

