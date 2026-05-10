from . import base_types
from .Number import Number
from .Jurisdiction1 import Jurisdiction1
from .ISODateTime import ISODateTime
from .Organisation38 import Organisation38
from .MICIdentifier import MICIdentifier
from .SecuritiesTransactionType31Choice import SecuritiesTransactionType31Choice
from .PriceValue1 import PriceValue1
from .FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from .ISODate import ISODate
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .CountryCode import CountryCode

class Issuance5(base_types._BaseFieldType):

	__slots__ = ["_IsseSz", "_FullIssdAmt", "_IssncDstrbtn", "_ISINVldFr", "_IssrOrg", "_CtryOfIsse", "_GovngLaw", "_AnncmntDt", "_IssePric", "_IssePlc", "_IsseDt", "_IsseNmnlAmt"]
	@property
	def IsseSz(self):
		return self._IsseSz

	@IsseSz.setter
	def IsseSz(self, value):
		self._IsseSz = value if type(value) != base_types.auto else self.make_default("IsseSz")

	@IsseSz.deleter
	def IsseSz(self):
		del self._IsseSz
		self._IsseSz = None

	@property
	def FullIssdAmt(self):
		return self._FullIssdAmt

	@FullIssdAmt.setter
	def FullIssdAmt(self, value):
		self._FullIssdAmt = value if type(value) != base_types.auto else self.make_default("FullIssdAmt")

	@FullIssdAmt.deleter
	def FullIssdAmt(self):
		del self._FullIssdAmt
		self._FullIssdAmt = None

	@property
	def IssncDstrbtn(self):
		return self._IssncDstrbtn

	@IssncDstrbtn.setter
	def IssncDstrbtn(self, value):
		self._IssncDstrbtn = value if type(value) != base_types.auto else self.make_default("IssncDstrbtn")

	@IssncDstrbtn.deleter
	def IssncDstrbtn(self):
		del self._IssncDstrbtn
		self._IssncDstrbtn = None

	@property
	def ISINVldFr(self):
		return self._ISINVldFr

	@ISINVldFr.setter
	def ISINVldFr(self, value):
		self._ISINVldFr = value if type(value) != base_types.auto else self.make_default("ISINVldFr")

	@ISINVldFr.deleter
	def ISINVldFr(self):
		del self._ISINVldFr
		self._ISINVldFr = None

	@property
	def IssrOrg(self):
		return self._IssrOrg

	@IssrOrg.setter
	def IssrOrg(self, value):
		self._IssrOrg = value if type(value) != base_types.auto else self.make_default("IssrOrg")

	@IssrOrg.deleter
	def IssrOrg(self):
		del self._IssrOrg
		self._IssrOrg = None

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if type(value) != base_types.auto else self.make_default("CtryOfIsse")

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = None

	@property
	def GovngLaw(self):
		return self._GovngLaw

	@GovngLaw.setter
	def GovngLaw(self, value):
		self._GovngLaw = value if type(value) != base_types.auto else self.make_default("GovngLaw")

	@GovngLaw.deleter
	def GovngLaw(self):
		del self._GovngLaw
		self._GovngLaw = None

	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if type(value) != base_types.auto else self.make_default("AnncmntDt")

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = None

	@property
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if type(value) != base_types.auto else self.make_default("IssePric")

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = None

	@property
	def IssePlc(self):
		return self._IssePlc

	@IssePlc.setter
	def IssePlc(self, value):
		self._IssePlc = value if type(value) != base_types.auto else self.make_default("IssePlc")

	@IssePlc.deleter
	def IssePlc(self):
		del self._IssePlc
		self._IssePlc = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def IsseNmnlAmt(self):
		return self._IsseNmnlAmt

	@IsseNmnlAmt.setter
	def IsseNmnlAmt(self, value):
		self._IsseNmnlAmt = value if type(value) != base_types.auto else self.make_default("IsseNmnlAmt")

	@IsseNmnlAmt.deleter
	def IsseNmnlAmt(self):
		del self._IsseNmnlAmt
		self._IsseNmnlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsseSz', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullIssdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncDstrbtn', type=SecuritiesTransactionType31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISINVldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOrg', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovngLaw', type=Jurisdiction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AnncmntDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePric', type=PriceValue1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePlc', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseNmnlAmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
	))

