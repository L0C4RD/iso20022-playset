# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._ContactBusiness1 import ContactBusiness1
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._InvoiceLineItem4 import InvoiceLineItem4
from ._LocalData20 import LocalData20
from ._Max1000Text import Max1000Text
from ._Max105Text import Max105Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._Max99Text import Max99Text
from ._Tax44 import Tax44
from ._TaxReclaimMethod1Code import TaxReclaimMethod1Code

class Invoice4(base_types._BaseFieldType):

	__slots__ = ["_BuyrAddtlInf", "_BuyrAdr", "_BuyrBizNm", "_BuyrCtct", "_BuyrId", "_BuyrLclData", "_BuyrLglCorpNm", "_BuyrNm", "_BuyrTaxRegnId", "_CreDtTm", "_Dt", "_FrghtAmt", "_LineItm", "_Nb", "_NtlData", "_PrvtData", "_SellrAddtlInf", "_SellrAdr", "_SellrBizNm", "_SellrCtct", "_SellrId", "_SellrLclData", "_SellrLglCorpNm", "_SellrNm", "_SellrTaxRegnId", "_SummryCmmdtyId", "_TaxRclmMtd", "_TaxTtl"]
	@property
	def BuyrAddtlInf(self):
		return self._BuyrAddtlInf

	@BuyrAddtlInf.setter
	def BuyrAddtlInf(self, value):
		self._BuyrAddtlInf = value if type(value) != base_types.auto else self.make_default("BuyrAddtlInf")

	@BuyrAddtlInf.deleter
	def BuyrAddtlInf(self):
		del self._BuyrAddtlInf
		self._BuyrAddtlInf = None

	@property
	def BuyrAdr(self):
		return self._BuyrAdr

	@BuyrAdr.setter
	def BuyrAdr(self, value):
		self._BuyrAdr = value if type(value) != base_types.auto else self.make_default("BuyrAdr")

	@BuyrAdr.deleter
	def BuyrAdr(self):
		del self._BuyrAdr
		self._BuyrAdr = None

	@property
	def BuyrBizNm(self):
		return self._BuyrBizNm

	@BuyrBizNm.setter
	def BuyrBizNm(self, value):
		self._BuyrBizNm = value if type(value) != base_types.auto else self.make_default("BuyrBizNm")

	@BuyrBizNm.deleter
	def BuyrBizNm(self):
		del self._BuyrBizNm
		self._BuyrBizNm = None

	@property
	def BuyrCtct(self):
		return self._BuyrCtct

	@BuyrCtct.setter
	def BuyrCtct(self, value):
		self._BuyrCtct = value if type(value) != base_types.auto else self.make_default("BuyrCtct")

	@BuyrCtct.deleter
	def BuyrCtct(self):
		del self._BuyrCtct
		self._BuyrCtct = None

	@property
	def BuyrId(self):
		return self._BuyrId

	@BuyrId.setter
	def BuyrId(self, value):
		self._BuyrId = value if type(value) != base_types.auto else self.make_default("BuyrId")

	@BuyrId.deleter
	def BuyrId(self):
		del self._BuyrId
		self._BuyrId = None

	@property
	def BuyrLclData(self):
		return self._BuyrLclData

	@BuyrLclData.setter
	def BuyrLclData(self, value):
		self._BuyrLclData = value if type(value) != base_types.auto else self.make_default("BuyrLclData")

	@BuyrLclData.deleter
	def BuyrLclData(self):
		del self._BuyrLclData
		self._BuyrLclData = None

	@property
	def BuyrLglCorpNm(self):
		return self._BuyrLglCorpNm

	@BuyrLglCorpNm.setter
	def BuyrLglCorpNm(self, value):
		self._BuyrLglCorpNm = value if type(value) != base_types.auto else self.make_default("BuyrLglCorpNm")

	@BuyrLglCorpNm.deleter
	def BuyrLglCorpNm(self):
		del self._BuyrLglCorpNm
		self._BuyrLglCorpNm = None

	@property
	def BuyrNm(self):
		return self._BuyrNm

	@BuyrNm.setter
	def BuyrNm(self, value):
		self._BuyrNm = value if type(value) != base_types.auto else self.make_default("BuyrNm")

	@BuyrNm.deleter
	def BuyrNm(self):
		del self._BuyrNm
		self._BuyrNm = None

	@property
	def BuyrTaxRegnId(self):
		return self._BuyrTaxRegnId

	@BuyrTaxRegnId.setter
	def BuyrTaxRegnId(self, value):
		self._BuyrTaxRegnId = value if type(value) != base_types.auto else self.make_default("BuyrTaxRegnId")

	@BuyrTaxRegnId.deleter
	def BuyrTaxRegnId(self):
		del self._BuyrTaxRegnId
		self._BuyrTaxRegnId = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def FrghtAmt(self):
		return self._FrghtAmt

	@FrghtAmt.setter
	def FrghtAmt(self, value):
		self._FrghtAmt = value if type(value) != base_types.auto else self.make_default("FrghtAmt")

	@FrghtAmt.deleter
	def FrghtAmt(self):
		del self._FrghtAmt
		self._FrghtAmt = None

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != base_types.auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def SellrAddtlInf(self):
		return self._SellrAddtlInf

	@SellrAddtlInf.setter
	def SellrAddtlInf(self, value):
		self._SellrAddtlInf = value if type(value) != base_types.auto else self.make_default("SellrAddtlInf")

	@SellrAddtlInf.deleter
	def SellrAddtlInf(self):
		del self._SellrAddtlInf
		self._SellrAddtlInf = None

	@property
	def SellrAdr(self):
		return self._SellrAdr

	@SellrAdr.setter
	def SellrAdr(self, value):
		self._SellrAdr = value if type(value) != base_types.auto else self.make_default("SellrAdr")

	@SellrAdr.deleter
	def SellrAdr(self):
		del self._SellrAdr
		self._SellrAdr = None

	@property
	def SellrBizNm(self):
		return self._SellrBizNm

	@SellrBizNm.setter
	def SellrBizNm(self, value):
		self._SellrBizNm = value if type(value) != base_types.auto else self.make_default("SellrBizNm")

	@SellrBizNm.deleter
	def SellrBizNm(self):
		del self._SellrBizNm
		self._SellrBizNm = None

	@property
	def SellrCtct(self):
		return self._SellrCtct

	@SellrCtct.setter
	def SellrCtct(self, value):
		self._SellrCtct = value if type(value) != base_types.auto else self.make_default("SellrCtct")

	@SellrCtct.deleter
	def SellrCtct(self):
		del self._SellrCtct
		self._SellrCtct = None

	@property
	def SellrId(self):
		return self._SellrId

	@SellrId.setter
	def SellrId(self, value):
		self._SellrId = value if type(value) != base_types.auto else self.make_default("SellrId")

	@SellrId.deleter
	def SellrId(self):
		del self._SellrId
		self._SellrId = None

	@property
	def SellrLclData(self):
		return self._SellrLclData

	@SellrLclData.setter
	def SellrLclData(self, value):
		self._SellrLclData = value if type(value) != base_types.auto else self.make_default("SellrLclData")

	@SellrLclData.deleter
	def SellrLclData(self):
		del self._SellrLclData
		self._SellrLclData = None

	@property
	def SellrLglCorpNm(self):
		return self._SellrLglCorpNm

	@SellrLglCorpNm.setter
	def SellrLglCorpNm(self, value):
		self._SellrLglCorpNm = value if type(value) != base_types.auto else self.make_default("SellrLglCorpNm")

	@SellrLglCorpNm.deleter
	def SellrLglCorpNm(self):
		del self._SellrLglCorpNm
		self._SellrLglCorpNm = None

	@property
	def SellrNm(self):
		return self._SellrNm

	@SellrNm.setter
	def SellrNm(self, value):
		self._SellrNm = value if type(value) != base_types.auto else self.make_default("SellrNm")

	@SellrNm.deleter
	def SellrNm(self):
		del self._SellrNm
		self._SellrNm = None

	@property
	def SellrTaxRegnId(self):
		return self._SellrTaxRegnId

	@SellrTaxRegnId.setter
	def SellrTaxRegnId(self, value):
		self._SellrTaxRegnId = value if type(value) != base_types.auto else self.make_default("SellrTaxRegnId")

	@SellrTaxRegnId.deleter
	def SellrTaxRegnId(self):
		del self._SellrTaxRegnId
		self._SellrTaxRegnId = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != base_types.auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def TaxRclmMtd(self):
		return self._TaxRclmMtd

	@TaxRclmMtd.setter
	def TaxRclmMtd(self, value):
		self._TaxRclmMtd = value if type(value) != base_types.auto else self.make_default("TaxRclmMtd")

	@TaxRclmMtd.deleter
	def TaxRclmMtd(self):
		del self._TaxRclmMtd
		self._TaxRclmMtd = None

	@property
	def TaxTtl(self):
		return self._TaxTtl

	@TaxTtl.setter
	def TaxTtl(self, value):
		self._TaxTtl = value if type(value) != base_types.auto else self.make_default("TaxTtl")

	@TaxTtl.deleter
	def TaxTtl(self):
		del self._TaxTtl
		self._TaxTtl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyrAddtlInf', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrLclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrLglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrNm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrTaxRegnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrghtAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=InvoiceLineItem4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrAddtlInf', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrLclData', type=LocalData20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrLglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrNm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrTaxRegnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmMtd', type=TaxReclaimMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTtl', type=Tax44, min=0, max=None, mutex_group=None, array=True),
	))