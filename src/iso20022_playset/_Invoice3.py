# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Address2
from . import ContactBusiness1
from . import ISODate
from . import ISODateTime
from . import ImpliedCurrencyAndAmount
from . import InvoiceLineItem3
from . import Max1000Text
from . import Max35Text
from . import Max70Text
from . import PartyIdentification285
from . import Tax41
from . import TaxReclaimMethod1Code

class Invoice3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_BuyrAddtlInf", "_BuyrAdr", "_BuyrCtct", "_BuyrId", "_BuyrNm", "_BuyrTaxRegnId", "_CreDtTm", "_Dt", "_FrghtAmt", "_LineItm", "_Nb", "_SellrAddtlInf", "_SellrAdr", "_SellrCtct", "_SellrId", "_SellrNm", "_SellrTaxRegnId", "_SummryCmmdtyId", "_TaxRclmMtd", "_TaxTtl"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def BuyrAddtlInf(self):
		return self._BuyrAddtlInf

	@BuyrAddtlInf.setter
	def BuyrAddtlInf(self, value):
		self._BuyrAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'BuyrAddtlInf', Max1000Text, False)

	@BuyrAddtlInf.deleter
	def BuyrAddtlInf(self):
		del self._BuyrAddtlInf
		self._BuyrAddtlInf = base_types.UninitialisedField(self, 'BuyrAddtlInf', Max1000Text, False)

	@property
	def BuyrAdr(self):
		return self._BuyrAdr

	@BuyrAdr.setter
	def BuyrAdr(self, value):
		self._BuyrAdr = value if value is not None else base_types.UninitialisedField(self, 'BuyrAdr', Address2, False)

	@BuyrAdr.deleter
	def BuyrAdr(self):
		del self._BuyrAdr
		self._BuyrAdr = base_types.UninitialisedField(self, 'BuyrAdr', Address2, False)

	@property
	def BuyrCtct(self):
		return self._BuyrCtct

	@BuyrCtct.setter
	def BuyrCtct(self, value):
		self._BuyrCtct = value if value is not None else base_types.UninitialisedField(self, 'BuyrCtct', ContactBusiness1, False)

	@BuyrCtct.deleter
	def BuyrCtct(self):
		del self._BuyrCtct
		self._BuyrCtct = base_types.UninitialisedField(self, 'BuyrCtct', ContactBusiness1, False)

	@property
	def BuyrId(self):
		return self._BuyrId

	@BuyrId.setter
	def BuyrId(self, value):
		self._BuyrId = value if value is not None else base_types.UninitialisedField(self, 'BuyrId', PartyIdentification285, False)

	@BuyrId.deleter
	def BuyrId(self):
		del self._BuyrId
		self._BuyrId = base_types.UninitialisedField(self, 'BuyrId', PartyIdentification285, False)

	@property
	def BuyrNm(self):
		return self._BuyrNm

	@BuyrNm.setter
	def BuyrNm(self, value):
		self._BuyrNm = value if value is not None else base_types.UninitialisedField(self, 'BuyrNm', Max70Text, False)

	@BuyrNm.deleter
	def BuyrNm(self):
		del self._BuyrNm
		self._BuyrNm = base_types.UninitialisedField(self, 'BuyrNm', Max70Text, False)

	@property
	def BuyrTaxRegnId(self):
		return self._BuyrTaxRegnId

	@BuyrTaxRegnId.setter
	def BuyrTaxRegnId(self, value):
		self._BuyrTaxRegnId = value if value is not None else base_types.UninitialisedField(self, 'BuyrTaxRegnId', Max70Text, False)

	@BuyrTaxRegnId.deleter
	def BuyrTaxRegnId(self):
		del self._BuyrTaxRegnId
		self._BuyrTaxRegnId = base_types.UninitialisedField(self, 'BuyrTaxRegnId', Max70Text, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def FrghtAmt(self):
		return self._FrghtAmt

	@FrghtAmt.setter
	def FrghtAmt(self, value):
		self._FrghtAmt = value if value is not None else base_types.UninitialisedField(self, 'FrghtAmt', ImpliedCurrencyAndAmount, False)

	@FrghtAmt.deleter
	def FrghtAmt(self):
		del self._FrghtAmt
		self._FrghtAmt = base_types.UninitialisedField(self, 'FrghtAmt', ImpliedCurrencyAndAmount, False)

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', InvoiceLineItem3, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', InvoiceLineItem3, True)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Max70Text, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Max70Text, False)

	@property
	def SellrAddtlInf(self):
		return self._SellrAddtlInf

	@SellrAddtlInf.setter
	def SellrAddtlInf(self, value):
		self._SellrAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'SellrAddtlInf', Max1000Text, False)

	@SellrAddtlInf.deleter
	def SellrAddtlInf(self):
		del self._SellrAddtlInf
		self._SellrAddtlInf = base_types.UninitialisedField(self, 'SellrAddtlInf', Max1000Text, False)

	@property
	def SellrAdr(self):
		return self._SellrAdr

	@SellrAdr.setter
	def SellrAdr(self, value):
		self._SellrAdr = value if value is not None else base_types.UninitialisedField(self, 'SellrAdr', Address2, False)

	@SellrAdr.deleter
	def SellrAdr(self):
		del self._SellrAdr
		self._SellrAdr = base_types.UninitialisedField(self, 'SellrAdr', Address2, False)

	@property
	def SellrCtct(self):
		return self._SellrCtct

	@SellrCtct.setter
	def SellrCtct(self, value):
		self._SellrCtct = value if value is not None else base_types.UninitialisedField(self, 'SellrCtct', ContactBusiness1, False)

	@SellrCtct.deleter
	def SellrCtct(self):
		del self._SellrCtct
		self._SellrCtct = base_types.UninitialisedField(self, 'SellrCtct', ContactBusiness1, False)

	@property
	def SellrId(self):
		return self._SellrId

	@SellrId.setter
	def SellrId(self, value):
		self._SellrId = value if value is not None else base_types.UninitialisedField(self, 'SellrId', PartyIdentification285, False)

	@SellrId.deleter
	def SellrId(self):
		del self._SellrId
		self._SellrId = base_types.UninitialisedField(self, 'SellrId', PartyIdentification285, False)

	@property
	def SellrNm(self):
		return self._SellrNm

	@SellrNm.setter
	def SellrNm(self, value):
		self._SellrNm = value if value is not None else base_types.UninitialisedField(self, 'SellrNm', Max70Text, False)

	@SellrNm.deleter
	def SellrNm(self):
		del self._SellrNm
		self._SellrNm = base_types.UninitialisedField(self, 'SellrNm', Max70Text, False)

	@property
	def SellrTaxRegnId(self):
		return self._SellrTaxRegnId

	@SellrTaxRegnId.setter
	def SellrTaxRegnId(self, value):
		self._SellrTaxRegnId = value if value is not None else base_types.UninitialisedField(self, 'SellrTaxRegnId', Max70Text, False)

	@SellrTaxRegnId.deleter
	def SellrTaxRegnId(self):
		del self._SellrTaxRegnId
		self._SellrTaxRegnId = base_types.UninitialisedField(self, 'SellrTaxRegnId', Max70Text, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def TaxRclmMtd(self):
		return self._TaxRclmMtd

	@TaxRclmMtd.setter
	def TaxRclmMtd(self, value):
		self._TaxRclmMtd = value if value is not None else base_types.UninitialisedField(self, 'TaxRclmMtd', TaxReclaimMethod1Code, False)

	@TaxRclmMtd.deleter
	def TaxRclmMtd(self):
		del self._TaxRclmMtd
		self._TaxRclmMtd = base_types.UninitialisedField(self, 'TaxRclmMtd', TaxReclaimMethod1Code, False)

	@property
	def TaxTtl(self):
		return self._TaxTtl

	@TaxTtl.setter
	def TaxTtl(self, value):
		self._TaxTtl = value if value is not None else base_types.UninitialisedField(self, 'TaxTtl', Tax41, True)

	@TaxTtl.deleter
	def TaxTtl(self):
		del self._TaxTtl
		self._TaxTtl = base_types.UninitialisedField(self, 'TaxTtl', Tax41, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrAddtlInf', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrTaxRegnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrghtAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=InvoiceLineItem3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrAddtlInf', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrTaxRegnId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRclmMtd', type=TaxReclaimMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTtl', type=Tax41, min=0, max=None, mutex_group=None, array=True),
	))