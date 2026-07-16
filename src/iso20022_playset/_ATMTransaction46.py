# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMMediaMix1
from . import AmountAndCurrency1
from . import CardAccount20
from . import ContentInformationType10
from . import CurrencyConversion32
from . import DetailedAmount12
from . import Max10000Binary
from . import Max35Text
from . import TransactionIdentifier3
from . import TrueFalseIndicator

class ATMTransaction46(base_types._BaseFieldType):

	__slots__ = ["_AcctData", "_CcyConvsRslt", "_CshDspnsd", "_DtldReqdAmt", "_ICCRltdData", "_PrtctdAcctData", "_RcncltnId", "_ReqdRct", "_SelctdMix", "_SelctdMixTp", "_TtlReqdAmt", "_TxId"]
	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if value is not None else base_types.UninitialisedField(self, 'AcctData', CardAccount20, False)

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = base_types.UninitialisedField(self, 'AcctData', CardAccount20, False)

	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion32, False)

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = base_types.UninitialisedField(self, 'CcyConvsRslt', CurrencyConversion32, False)

	@property
	def CshDspnsd(self):
		return self._CshDspnsd

	@CshDspnsd.setter
	def CshDspnsd(self, value):
		self._CshDspnsd = value if value is not None else base_types.UninitialisedField(self, 'CshDspnsd', TrueFalseIndicator, False)

	@CshDspnsd.deleter
	def CshDspnsd(self):
		del self._CshDspnsd
		self._CshDspnsd = base_types.UninitialisedField(self, 'CshDspnsd', TrueFalseIndicator, False)

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount12, False)

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = base_types.UninitialisedField(self, 'DtldReqdAmt', DetailedAmount12, False)

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
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdAcctData', ContentInformationType10, False)

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = base_types.UninitialisedField(self, 'PrtctdAcctData', ContentInformationType10, False)

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
	def SelctdMix(self):
		return self._SelctdMix

	@SelctdMix.setter
	def SelctdMix(self, value):
		self._SelctdMix = value if value is not None else base_types.UninitialisedField(self, 'SelctdMix', ATMMediaMix1, True)

	@SelctdMix.deleter
	def SelctdMix(self):
		del self._SelctdMix
		self._SelctdMix = base_types.UninitialisedField(self, 'SelctdMix', ATMMediaMix1, True)

	@property
	def SelctdMixTp(self):
		return self._SelctdMixTp

	@SelctdMixTp.setter
	def SelctdMixTp(self, value):
		self._SelctdMixTp = value if value is not None else base_types.UninitialisedField(self, 'SelctdMixTp', Max35Text, False)

	@SelctdMixTp.deleter
	def SelctdMixTp(self):
		del self._SelctdMixTp
		self._SelctdMixTp = base_types.UninitialisedField(self, 'SelctdMixTp', Max35Text, False)

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlReqdAmt', AmountAndCurrency1, False)

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = base_types.UninitialisedField(self, 'TtlReqdAmt', AmountAndCurrency1, False)

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
		base_types.FieldEntry(name='AcctData', type=CardAccount20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsRslt', type=CurrencyConversion32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshDspnsd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldReqdAmt', type=DetailedAmount12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAcctData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRct', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SelctdMix', type=ATMMediaMix1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SelctdMixTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlReqdAmt', type=AmountAndCurrency1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
	))