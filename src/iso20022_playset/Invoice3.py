import base_types
import Max70Text
import TaxReclaimMethod1Code
import ISODateTime
import InvoiceLineItem3
import ContactBusiness1
import PartyIdentification285
import AdditionalData1
import Address2
import ImpliedCurrencyAndAmount
import Max35Text
import ISODate
import Max1000Text
import Tax41

class Invoice3(base_types._BaseFieldType):

	__slots__ = ["_SellrTaxRegnId", "_TaxTtl", "_BuyrTaxRegnId", "_Dt", "_BuyrId", "_SellrId", "_AddtlData", "_Nb", "_CreDtTm", "_FrghtAmt", "_BuyrCtct", "_SellrCtct", "_SummryCmmdtyId", "_SellrAdr", "_BuyrAdr", "_BuyrNm", "_LineItm", "_SellrNm", "_BuyrAddtlInf", "_TaxRclmMtd", "_SellrAddtlInf"]
	@property
	def SellrTaxRegnId(self):
		return self._SellrTaxRegnId

	@SellrTaxRegnId.setter
	def SellrTaxRegnId(self, value):
		self._SellrTaxRegnId = value if type(value) != auto else self.make_default("SellrTaxRegnId")

	@SellrTaxRegnId.deleter
	def SellrTaxRegnId(self):
		del self._SellrTaxRegnId
		self._SellrTaxRegnId = None

	@property
	def TaxTtl(self):
		return self._TaxTtl

	@TaxTtl.setter
	def TaxTtl(self, value):
		self._TaxTtl = value if type(value) != auto else self.make_default("TaxTtl")

	@TaxTtl.deleter
	def TaxTtl(self):
		del self._TaxTtl
		self._TaxTtl = None

	@property
	def BuyrTaxRegnId(self):
		return self._BuyrTaxRegnId

	@BuyrTaxRegnId.setter
	def BuyrTaxRegnId(self, value):
		self._BuyrTaxRegnId = value if type(value) != auto else self.make_default("BuyrTaxRegnId")

	@BuyrTaxRegnId.deleter
	def BuyrTaxRegnId(self):
		del self._BuyrTaxRegnId
		self._BuyrTaxRegnId = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def BuyrId(self):
		return self._BuyrId

	@BuyrId.setter
	def BuyrId(self, value):
		self._BuyrId = value if type(value) != auto else self.make_default("BuyrId")

	@BuyrId.deleter
	def BuyrId(self):
		del self._BuyrId
		self._BuyrId = None

	@property
	def SellrId(self):
		return self._SellrId

	@SellrId.setter
	def SellrId(self, value):
		self._SellrId = value if type(value) != auto else self.make_default("SellrId")

	@SellrId.deleter
	def SellrId(self):
		del self._SellrId
		self._SellrId = None

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
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def FrghtAmt(self):
		return self._FrghtAmt

	@FrghtAmt.setter
	def FrghtAmt(self, value):
		self._FrghtAmt = value if type(value) != auto else self.make_default("FrghtAmt")

	@FrghtAmt.deleter
	def FrghtAmt(self):
		del self._FrghtAmt
		self._FrghtAmt = None

	@property
	def BuyrCtct(self):
		return self._BuyrCtct

	@BuyrCtct.setter
	def BuyrCtct(self, value):
		self._BuyrCtct = value if type(value) != auto else self.make_default("BuyrCtct")

	@BuyrCtct.deleter
	def BuyrCtct(self):
		del self._BuyrCtct
		self._BuyrCtct = None

	@property
	def SellrCtct(self):
		return self._SellrCtct

	@SellrCtct.setter
	def SellrCtct(self, value):
		self._SellrCtct = value if type(value) != auto else self.make_default("SellrCtct")

	@SellrCtct.deleter
	def SellrCtct(self):
		del self._SellrCtct
		self._SellrCtct = None

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
	def SellrAdr(self):
		return self._SellrAdr

	@SellrAdr.setter
	def SellrAdr(self, value):
		self._SellrAdr = value if type(value) != auto else self.make_default("SellrAdr")

	@SellrAdr.deleter
	def SellrAdr(self):
		del self._SellrAdr
		self._SellrAdr = None

	@property
	def BuyrAdr(self):
		return self._BuyrAdr

	@BuyrAdr.setter
	def BuyrAdr(self, value):
		self._BuyrAdr = value if type(value) != auto else self.make_default("BuyrAdr")

	@BuyrAdr.deleter
	def BuyrAdr(self):
		del self._BuyrAdr
		self._BuyrAdr = None

	@property
	def BuyrNm(self):
		return self._BuyrNm

	@BuyrNm.setter
	def BuyrNm(self, value):
		self._BuyrNm = value if type(value) != auto else self.make_default("BuyrNm")

	@BuyrNm.deleter
	def BuyrNm(self):
		del self._BuyrNm
		self._BuyrNm = None

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

	@property
	def SellrNm(self):
		return self._SellrNm

	@SellrNm.setter
	def SellrNm(self, value):
		self._SellrNm = value if type(value) != auto else self.make_default("SellrNm")

	@SellrNm.deleter
	def SellrNm(self):
		del self._SellrNm
		self._SellrNm = None

	@property
	def BuyrAddtlInf(self):
		return self._BuyrAddtlInf

	@BuyrAddtlInf.setter
	def BuyrAddtlInf(self, value):
		self._BuyrAddtlInf = value if type(value) != auto else self.make_default("BuyrAddtlInf")

	@BuyrAddtlInf.deleter
	def BuyrAddtlInf(self):
		del self._BuyrAddtlInf
		self._BuyrAddtlInf = None

	@property
	def TaxRclmMtd(self):
		return self._TaxRclmMtd

	@TaxRclmMtd.setter
	def TaxRclmMtd(self, value):
		self._TaxRclmMtd = value if type(value) != auto else self.make_default("TaxRclmMtd")

	@TaxRclmMtd.deleter
	def TaxRclmMtd(self):
		del self._TaxRclmMtd
		self._TaxRclmMtd = None

	@property
	def SellrAddtlInf(self):
		return self._SellrAddtlInf

	@SellrAddtlInf.setter
	def SellrAddtlInf(self, value):
		self._SellrAddtlInf = value if type(value) != auto else self.make_default("SellrAddtlInf")

	@SellrAddtlInf.deleter
	def SellrAddtlInf(self):
		del self._SellrAddtlInf
		self._SellrAddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SellrTaxRegnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTtl', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrTaxRegnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrghtAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=InvoiceLineItem3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrAddtlInf', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmMtd', type=TaxReclaimMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrAddtlInf', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
	))

