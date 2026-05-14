# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMMediaMix1 import ATMMediaMix1
from ._AmountAndCurrency1 import AmountAndCurrency1
from ._CardAccount20 import CardAccount20
from ._ContentInformationType10 import ContentInformationType10
from ._CurrencyConversion32 import CurrencyConversion32
from ._DetailedAmount12 import DetailedAmount12
from ._Max10000Binary import Max10000Binary
from ._Max35Text import Max35Text
from ._TransactionIdentifier3 import TransactionIdentifier3
from ._TrueFalseIndicator import TrueFalseIndicator

class ATMTransaction46(base_types._BaseFieldType):

	__slots__ = ["_AcctData", "_CcyConvsRslt", "_CshDspnsd", "_DtldReqdAmt", "_ICCRltdData", "_PrtctdAcctData", "_RcncltnId", "_ReqdRct", "_SelctdMix", "_SelctdMixTp", "_TtlReqdAmt", "_TxId"]
	@property
	def AcctData(self):
		return self._AcctData

	@AcctData.setter
	def AcctData(self, value):
		self._AcctData = value if type(value) != base_types.auto else self.make_default("AcctData")

	@AcctData.deleter
	def AcctData(self):
		del self._AcctData
		self._AcctData = None

	@property
	def CcyConvsRslt(self):
		return self._CcyConvsRslt

	@CcyConvsRslt.setter
	def CcyConvsRslt(self, value):
		self._CcyConvsRslt = value if type(value) != base_types.auto else self.make_default("CcyConvsRslt")

	@CcyConvsRslt.deleter
	def CcyConvsRslt(self):
		del self._CcyConvsRslt
		self._CcyConvsRslt = None

	@property
	def CshDspnsd(self):
		return self._CshDspnsd

	@CshDspnsd.setter
	def CshDspnsd(self, value):
		self._CshDspnsd = value if type(value) != base_types.auto else self.make_default("CshDspnsd")

	@CshDspnsd.deleter
	def CshDspnsd(self):
		del self._CshDspnsd
		self._CshDspnsd = None

	@property
	def DtldReqdAmt(self):
		return self._DtldReqdAmt

	@DtldReqdAmt.setter
	def DtldReqdAmt(self, value):
		self._DtldReqdAmt = value if type(value) != base_types.auto else self.make_default("DtldReqdAmt")

	@DtldReqdAmt.deleter
	def DtldReqdAmt(self):
		del self._DtldReqdAmt
		self._DtldReqdAmt = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != base_types.auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def PrtctdAcctData(self):
		return self._PrtctdAcctData

	@PrtctdAcctData.setter
	def PrtctdAcctData(self, value):
		self._PrtctdAcctData = value if type(value) != base_types.auto else self.make_default("PrtctdAcctData")

	@PrtctdAcctData.deleter
	def PrtctdAcctData(self):
		del self._PrtctdAcctData
		self._PrtctdAcctData = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != base_types.auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def ReqdRct(self):
		return self._ReqdRct

	@ReqdRct.setter
	def ReqdRct(self, value):
		self._ReqdRct = value if type(value) != base_types.auto else self.make_default("ReqdRct")

	@ReqdRct.deleter
	def ReqdRct(self):
		del self._ReqdRct
		self._ReqdRct = None

	@property
	def SelctdMix(self):
		return self._SelctdMix

	@SelctdMix.setter
	def SelctdMix(self, value):
		self._SelctdMix = value if type(value) != base_types.auto else self.make_default("SelctdMix")

	@SelctdMix.deleter
	def SelctdMix(self):
		del self._SelctdMix
		self._SelctdMix = None

	@property
	def SelctdMixTp(self):
		return self._SelctdMixTp

	@SelctdMixTp.setter
	def SelctdMixTp(self, value):
		self._SelctdMixTp = value if type(value) != base_types.auto else self.make_default("SelctdMixTp")

	@SelctdMixTp.deleter
	def SelctdMixTp(self):
		del self._SelctdMixTp
		self._SelctdMixTp = None

	@property
	def TtlReqdAmt(self):
		return self._TtlReqdAmt

	@TtlReqdAmt.setter
	def TtlReqdAmt(self, value):
		self._TtlReqdAmt = value if type(value) != base_types.auto else self.make_default("TtlReqdAmt")

	@TtlReqdAmt.deleter
	def TtlReqdAmt(self):
		del self._TtlReqdAmt
		self._TtlReqdAmt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

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