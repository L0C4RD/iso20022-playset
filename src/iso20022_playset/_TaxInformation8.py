# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ISODate
from . import Max140Text
from . import Max35Text
from . import Number
from . import TaxParty1
from . import TaxParty2
from . import TaxRecord2

class TaxInformation8(base_types._BaseFieldType):

	__slots__ = ["_AdmstnZone", "_Cdtr", "_Dbtr", "_Dt", "_Mtd", "_Rcrd", "_RefNb", "_SeqNb", "_TtlTaxAmt", "_TtlTaxblBaseAmt"]
	@property
	def AdmstnZone(self):
		return self._AdmstnZone

	@AdmstnZone.setter
	def AdmstnZone(self, value):
		self._AdmstnZone = value if value is not None else base_types.UninitialisedField(self, 'AdmstnZone', Max35Text, False)

	@AdmstnZone.deleter
	def AdmstnZone(self):
		del self._AdmstnZone
		self._AdmstnZone = base_types.UninitialisedField(self, 'AdmstnZone', Max35Text, False)

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', TaxParty1, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', TaxParty1, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', TaxParty2, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', TaxParty2, False)

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
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if value is not None else base_types.UninitialisedField(self, 'Mtd', Max35Text, False)

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = base_types.UninitialisedField(self, 'Mtd', Max35Text, False)

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if value is not None else base_types.UninitialisedField(self, 'Rcrd', TaxRecord2, True)

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = base_types.UninitialisedField(self, 'Rcrd', TaxRecord2, True)

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if value is not None else base_types.UninitialisedField(self, 'RefNb', Max140Text, False)

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = base_types.UninitialisedField(self, 'RefNb', Max140Text, False)

	@property
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if value is not None else base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = base_types.UninitialisedField(self, 'SeqNb', Number, False)

	@property
	def TtlTaxAmt(self):
		return self._TtlTaxAmt

	@TtlTaxAmt.setter
	def TtlTaxAmt(self, value):
		self._TtlTaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlTaxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlTaxAmt.deleter
	def TtlTaxAmt(self):
		del self._TtlTaxAmt
		self._TtlTaxAmt = base_types.UninitialisedField(self, 'TtlTaxAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlTaxblBaseAmt(self):
		return self._TtlTaxblBaseAmt

	@TtlTaxblBaseAmt.setter
	def TtlTaxblBaseAmt(self, value):
		self._TtlTaxblBaseAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlTaxblBaseAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlTaxblBaseAmt.deleter
	def TtlTaxblBaseAmt(self):
		del self._TtlTaxblBaseAmt
		self._TtlTaxblBaseAmt = base_types.UninitialisedField(self, 'TtlTaxblBaseAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdmstnZone', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=TaxParty1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=TaxParty2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=TaxRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefNb', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTaxblBaseAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))