# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditorReferenceInformation2
from . import CurrencyAndAmount
from . import CurrencyReference3
from . import EarlyPayment1
from . import ISODate
from . import Max4Text
from . import Max500Text
from . import Period2
from . import SettlementSubTotalCalculatedTax2

class TradeSettlement2(base_types._BaseFieldType):

	__slots__ = ["_BllgPrd", "_DlvryDt", "_DueDt", "_DuePyblAmt", "_EarlyPmts", "_InvcCcyXchg", "_PmtRef", "_SubTtlClctdTax", "_TaxTtlAmt", "_XmptnRsn", "_XmptnRsnCd"]
	@property
	def BllgPrd(self):
		return self._BllgPrd

	@BllgPrd.setter
	def BllgPrd(self, value):
		self._BllgPrd = value if value is not None else base_types.UninitialisedField(self, 'BllgPrd', Period2, False)

	@BllgPrd.deleter
	def BllgPrd(self):
		del self._BllgPrd
		self._BllgPrd = base_types.UninitialisedField(self, 'BllgPrd', Period2, False)

	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if value is not None else base_types.UninitialisedField(self, 'DlvryDt', ISODate, False)

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = base_types.UninitialisedField(self, 'DlvryDt', ISODate, False)

	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if value is not None else base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = base_types.UninitialisedField(self, 'DueDt', ISODate, False)

	@property
	def DuePyblAmt(self):
		return self._DuePyblAmt

	@DuePyblAmt.setter
	def DuePyblAmt(self, value):
		self._DuePyblAmt = value if value is not None else base_types.UninitialisedField(self, 'DuePyblAmt', CurrencyAndAmount, False)

	@DuePyblAmt.deleter
	def DuePyblAmt(self):
		del self._DuePyblAmt
		self._DuePyblAmt = base_types.UninitialisedField(self, 'DuePyblAmt', CurrencyAndAmount, False)

	@property
	def EarlyPmts(self):
		return self._EarlyPmts

	@EarlyPmts.setter
	def EarlyPmts(self, value):
		self._EarlyPmts = value if value is not None else base_types.UninitialisedField(self, 'EarlyPmts', EarlyPayment1, True)

	@EarlyPmts.deleter
	def EarlyPmts(self):
		del self._EarlyPmts
		self._EarlyPmts = base_types.UninitialisedField(self, 'EarlyPmts', EarlyPayment1, True)

	@property
	def InvcCcyXchg(self):
		return self._InvcCcyXchg

	@InvcCcyXchg.setter
	def InvcCcyXchg(self, value):
		self._InvcCcyXchg = value if value is not None else base_types.UninitialisedField(self, 'InvcCcyXchg', CurrencyReference3, False)

	@InvcCcyXchg.deleter
	def InvcCcyXchg(self):
		del self._InvcCcyXchg
		self._InvcCcyXchg = base_types.UninitialisedField(self, 'InvcCcyXchg', CurrencyReference3, False)

	@property
	def PmtRef(self):
		return self._PmtRef

	@PmtRef.setter
	def PmtRef(self, value):
		self._PmtRef = value if value is not None else base_types.UninitialisedField(self, 'PmtRef', CreditorReferenceInformation2, False)

	@PmtRef.deleter
	def PmtRef(self):
		del self._PmtRef
		self._PmtRef = base_types.UninitialisedField(self, 'PmtRef', CreditorReferenceInformation2, False)

	@property
	def SubTtlClctdTax(self):
		return self._SubTtlClctdTax

	@SubTtlClctdTax.setter
	def SubTtlClctdTax(self, value):
		self._SubTtlClctdTax = value if value is not None else base_types.UninitialisedField(self, 'SubTtlClctdTax', SettlementSubTotalCalculatedTax2, True)

	@SubTtlClctdTax.deleter
	def SubTtlClctdTax(self):
		del self._SubTtlClctdTax
		self._SubTtlClctdTax = base_types.UninitialisedField(self, 'SubTtlClctdTax', SettlementSubTotalCalculatedTax2, True)

	@property
	def TaxTtlAmt(self):
		return self._TaxTtlAmt

	@TaxTtlAmt.setter
	def TaxTtlAmt(self, value):
		self._TaxTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxTtlAmt', CurrencyAndAmount, False)

	@TaxTtlAmt.deleter
	def TaxTtlAmt(self):
		del self._TaxTtlAmt
		self._TaxTtlAmt = base_types.UninitialisedField(self, 'TaxTtlAmt', CurrencyAndAmount, False)

	@property
	def XmptnRsn(self):
		return self._XmptnRsn

	@XmptnRsn.setter
	def XmptnRsn(self, value):
		self._XmptnRsn = value if value is not None else base_types.UninitialisedField(self, 'XmptnRsn', Max500Text, False)

	@XmptnRsn.deleter
	def XmptnRsn(self):
		del self._XmptnRsn
		self._XmptnRsn = base_types.UninitialisedField(self, 'XmptnRsn', Max500Text, False)

	@property
	def XmptnRsnCd(self):
		return self._XmptnRsnCd

	@XmptnRsnCd.setter
	def XmptnRsnCd(self, value):
		self._XmptnRsnCd = value if value is not None else base_types.UninitialisedField(self, 'XmptnRsnCd', Max4Text, False)

	@XmptnRsnCd.deleter
	def XmptnRsnCd(self):
		del self._XmptnRsnCd
		self._XmptnRsnCd = base_types.UninitialisedField(self, 'XmptnRsnCd', Max4Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgPrd', type=Period2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DuePyblAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmts', type=EarlyPayment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvcCcyXchg', type=CurrencyReference3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRef', type=CreditorReferenceInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTtlClctdTax', type=SettlementSubTotalCalculatedTax2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsn', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsnCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
	))