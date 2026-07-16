# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardAccount20
from . import ContentInformationType10
from . import DetailedAmount17
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max10000Binary
from . import Max35Text
from . import RecurringTransaction3
from . import TransactionIdentifier3
from . import TrueFalseIndicator

class ATMTransaction38(base_types._BaseFieldType):

	__slots__ = ["_AcctFr", "_AcctTo", "_CdtrLabl", "_DbtrLabl", "_DtldReqdAmt", "_ICCRltdData", "_InstntTrfPrgm", "_PmtRef", "_PrtctdAcctFr", "_PrtctdAcctTo", "_RcncltnId", "_RcrngTrf", "_ReqdExctnDt", "_ReqdRct", "_TtlReqdAmt", "_TxId"]
	@property
	def AcctFr(self):
		return self._AcctFr

	@AcctFr.setter
	def AcctFr(self, value):
		self._AcctFr = value if value is not None else base_types.UninitialisedField(self, 'AcctFr', CardAccount20, False)

	@AcctFr.deleter
	def AcctFr(self):
		del self._AcctFr
		self._AcctFr = base_types.UninitialisedField(self, 'AcctFr', CardAccount20, False)

	@property
	def AcctTo(self):
		return self._AcctTo

	@AcctTo.setter
	def AcctTo(self, value):
		self._AcctTo = value if value is not None else base_types.UninitialisedField(self, 'AcctTo', CardAccount20, True)

	@AcctTo.deleter
	def AcctTo(self):
		del self._AcctTo
		self._AcctTo = base_types.UninitialisedField(self, 'AcctTo', CardAccount20, True)

	@property
	def CdtrLabl(self):
		return self._CdtrLabl

	@CdtrLabl.setter
	def CdtrLabl(self, value):
		self._CdtrLabl = value if value is not None else base_types.UninitialisedField(self, 'CdtrLabl', Max35Text, False)

	@CdtrLabl.deleter
	def CdtrLabl(self):
		del self._CdtrLabl
		self._CdtrLabl = base_types.UninitialisedField(self, 'CdtrLabl', Max35Text, False)

	@property
	def DbtrLabl(self):
		return self._DbtrLabl

	@DbtrLabl.setter
	def DbtrLabl(self, value):
		self._DbtrLabl = value if value is not None else base_types.UninitialisedField(self, 'DbtrLabl', Max35Text, False)

	@DbtrLabl.deleter
	def DbtrLabl(self):
		del self._DbtrLabl
		self._DbtrLabl = base_types.UninitialisedField(self, 'DbtrLabl', Max35Text, False)

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount17, False)

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount17, False)

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if value is not None else base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = base_types.UninitialisedField(self, 'ICCRltdData', Max10000Binary, False)

	@property
	def InstntTrfPrgm(self):
		return self._InstntTrfPrgm

	@InstntTrfPrgm.setter
	def InstntTrfPrgm(self, value):
		self._InstntTrfPrgm = value if value is not None else base_types.UninitialisedField(self, 'InstntTrfPrgm', Max35Text, False)

	@InstntTrfPrgm.deleter
	def InstntTrfPrgm(self):
		del self._InstntTrfPrgm
		self._InstntTrfPrgm = base_types.UninitialisedField(self, 'InstntTrfPrgm', Max35Text, False)

	@property
	def PmtRef(self):
		return self._PmtRef

	@PmtRef.setter
	def PmtRef(self, value):
		self._PmtRef = value if value is not None else base_types.UninitialisedField(self, 'PmtRef', Max35Text, False)

	@PmtRef.deleter
	def PmtRef(self):
		del self._PmtRef
		self._PmtRef = base_types.UninitialisedField(self, 'PmtRef', Max35Text, False)

	@property
	def PrtctdAcctFr(self):
		return self._PrtctdAcctFr

	@PrtctdAcctFr.setter
	def PrtctdAcctFr(self, value):
		self._PrtctdAcctFr = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAcctFr', ContentInformationType10, False)

	@PrtctdAcctFr.deleter
	def PrtctdAcctFr(self):
		del self._PrtctdAcctFr
		self._PrtctdAcctFr = base_types.UninitialisedField(self, 'PrtctdAcctFr', ContentInformationType10, False)

	@property
	def PrtctdAcctTo(self):
		return self._PrtctdAcctTo

	@PrtctdAcctTo.setter
	def PrtctdAcctTo(self, value):
		self._PrtctdAcctTo = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAcctTo', ContentInformationType10, False)

	@PrtctdAcctTo.deleter
	def PrtctdAcctTo(self):
		del self._PrtctdAcctTo
		self._PrtctdAcctTo = base_types.UninitialisedField(self, 'PrtctdAcctTo', ContentInformationType10, False)

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if value is not None else base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = base_types.UninitialisedField(self, 'RcncltnId', Max35Text, False)

	@property
	def RcrngTrf(self):
		return self._RcrngTrf

	@RcrngTrf.setter
	def RcrngTrf(self, value):
		self._RcrngTrf = value if value is not None else base_types.UninitialisedField(self, 'RcrngTrf', RecurringTransaction3, False)

	@RcrngTrf.deleter
	def RcrngTrf(self):
		del self._RcrngTrf
		self._RcrngTrf = base_types.UninitialisedField(self, 'RcrngTrf', RecurringTransaction3, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', ISODate, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', ISODate, False)

	@property
	def ReqdRct(self):
		return self._ReqdRct

	@ReqdRct.setter
	def ReqdRct(self, value):
		self._ReqdRct = value if value is not None else base_types.UninitialisedField(self, 'ReqdRct', TrueFalseIndicator, False)

	@ReqdRct.deleter
	def ReqdRct(self):
		del self._ReqdRct
		self._ReqdRct = base_types.UninitialisedField(self, 'ReqdRct', TrueFalseIndicator, False)

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlReqdAmt', ImpliedCurrencyAndAmount, False)

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = base_types.UninitialisedField(self, 'TtlReqdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentifier3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctFr', type=CardAccount20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTo', type=CardAccount20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstntTrfPrgm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctFr', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctTo', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrngTrf', type=RecurringTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))