# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CountryCode
from . import FinancialInstrumentQuantity1Choice
from . import ISODate
from . import ISODateTime
from . import Jurisdiction1
from . import MICIdentifier
from . import Number
from . import Organisation38
from . import PriceValue1
from . import SecuritiesTransactionType31Choice

class Issuance5(base_types._BaseFieldType):

	__slots__ = ["_AnncmntDt", "_CtryOfIsse", "_FullIssdAmt", "_GovngLaw", "_ISINVldFr", "_IsseDt", "_IsseNmnlAmt", "_IssePlc", "_IssePric", "_IsseSz", "_IssncDstrbtn", "_IssrOrg"]
	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if value is not None else base_types.UninitialisedField(self, 'AnncmntDt', ISODateTime, False)

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = base_types.UninitialisedField(self, 'AnncmntDt', ISODateTime, False)

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, False)

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = base_types.UninitialisedField(self, 'CtryOfIsse', CountryCode, False)

	@property
	def FullIssdAmt(self):
		return self._FullIssdAmt

	@FullIssdAmt.setter
	def FullIssdAmt(self, value):
		self._FullIssdAmt = value if value is not None else base_types.UninitialisedField(self, 'FullIssdAmt', ActiveCurrencyAndAmount, False)

	@FullIssdAmt.deleter
	def FullIssdAmt(self):
		del self._FullIssdAmt
		self._FullIssdAmt = base_types.UninitialisedField(self, 'FullIssdAmt', ActiveCurrencyAndAmount, False)

	@property
	def GovngLaw(self):
		return self._GovngLaw

	@GovngLaw.setter
	def GovngLaw(self, value):
		self._GovngLaw = value if value is not None else base_types.UninitialisedField(self, 'GovngLaw', Jurisdiction1, True)

	@GovngLaw.deleter
	def GovngLaw(self):
		del self._GovngLaw
		self._GovngLaw = base_types.UninitialisedField(self, 'GovngLaw', Jurisdiction1, True)

	@property
	def ISINVldFr(self):
		return self._ISINVldFr

	@ISINVldFr.setter
	def ISINVldFr(self, value):
		self._ISINVldFr = value if value is not None else base_types.UninitialisedField(self, 'ISINVldFr', ISODate, False)

	@ISINVldFr.deleter
	def ISINVldFr(self):
		del self._ISINVldFr
		self._ISINVldFr = base_types.UninitialisedField(self, 'ISINVldFr', ISODate, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISODate, False)

	@property
	def IsseNmnlAmt(self):
		return self._IsseNmnlAmt

	@IsseNmnlAmt.setter
	def IsseNmnlAmt(self, value):
		self._IsseNmnlAmt = value if value is not None else base_types.UninitialisedField(self, 'IsseNmnlAmt', FinancialInstrumentQuantity1Choice, False)

	@IsseNmnlAmt.deleter
	def IsseNmnlAmt(self):
		del self._IsseNmnlAmt
		self._IsseNmnlAmt = base_types.UninitialisedField(self, 'IsseNmnlAmt', FinancialInstrumentQuantity1Choice, False)

	@property
	def IssePlc(self):
		return self._IssePlc

	@IssePlc.setter
	def IssePlc(self, value):
		self._IssePlc = value if value is not None else base_types.UninitialisedField(self, 'IssePlc', MICIdentifier, False)

	@IssePlc.deleter
	def IssePlc(self):
		del self._IssePlc
		self._IssePlc = base_types.UninitialisedField(self, 'IssePlc', MICIdentifier, False)

	@property
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if value is not None else base_types.UninitialisedField(self, 'IssePric', PriceValue1, False)

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = base_types.UninitialisedField(self, 'IssePric', PriceValue1, False)

	@property
	def IsseSz(self):
		return self._IsseSz

	@IsseSz.setter
	def IsseSz(self, value):
		self._IsseSz = value if value is not None else base_types.UninitialisedField(self, 'IsseSz', Number, False)

	@IsseSz.deleter
	def IsseSz(self):
		del self._IsseSz
		self._IsseSz = base_types.UninitialisedField(self, 'IsseSz', Number, False)

	@property
	def IssncDstrbtn(self):
		return self._IssncDstrbtn

	@IssncDstrbtn.setter
	def IssncDstrbtn(self, value):
		self._IssncDstrbtn = value if value is not None else base_types.UninitialisedField(self, 'IssncDstrbtn', SecuritiesTransactionType31Choice, False)

	@IssncDstrbtn.deleter
	def IssncDstrbtn(self):
		del self._IssncDstrbtn
		self._IssncDstrbtn = base_types.UninitialisedField(self, 'IssncDstrbtn', SecuritiesTransactionType31Choice, False)

	@property
	def IssrOrg(self):
		return self._IssrOrg

	@IssrOrg.setter
	def IssrOrg(self, value):
		self._IssrOrg = value if value is not None else base_types.UninitialisedField(self, 'IssrOrg', Organisation38, False)

	@IssrOrg.deleter
	def IssrOrg(self):
		del self._IssrOrg
		self._IssrOrg = base_types.UninitialisedField(self, 'IssrOrg', Organisation38, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnncmntDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullIssdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GovngLaw', type=Jurisdiction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ISINVldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseNmnlAmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePlc', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePric', type=PriceValue1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseSz', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncDstrbtn', type=SecuritiesTransactionType31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrOrg', type=Organisation38, min=0, max=1, mutex_group=None, array=False),
	))