# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BlockChainAddressWallet3 import BlockChainAddressWallet3
from ._CollateralOwnership3 import CollateralOwnership3
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate
from ._Price7 import Price7
from ._SafekeepingPlaceFormat29Choice import SafekeepingPlaceFormat29Choice
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._SecurityIdentification19 import SecurityIdentification19
from ._YesNoIndicator import YesNoIndicator

class SecuritiesCollateral13(base_types._BaseFieldType):

	__slots__ = ["_AsstNb", "_BlckChainAdrOrWllt", "_BlckdQty", "_CollOwnrsh", "_CollVal", "_Hrcut", "_LtdCvrgInd", "_MktVal", "_MtrtyDt", "_Pric", "_Qty", "_SctyId", "_SfkpgAcct", "_SfkpgPlc", "_ValDt"]
	@property
	def AsstNb(self):
		return self._AsstNb

	@AsstNb.setter
	def AsstNb(self, value):
		self._AsstNb = value if type(value) != base_types.auto else self.make_default("AsstNb")

	@AsstNb.deleter
	def AsstNb(self):
		del self._AsstNb
		self._AsstNb = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != base_types.auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def BlckdQty(self):
		return self._BlckdQty

	@BlckdQty.setter
	def BlckdQty(self, value):
		self._BlckdQty = value if type(value) != base_types.auto else self.make_default("BlckdQty")

	@BlckdQty.deleter
	def BlckdQty(self):
		del self._BlckdQty
		self._BlckdQty = None

	@property
	def CollOwnrsh(self):
		return self._CollOwnrsh

	@CollOwnrsh.setter
	def CollOwnrsh(self, value):
		self._CollOwnrsh = value if type(value) != base_types.auto else self.make_default("CollOwnrsh")

	@CollOwnrsh.deleter
	def CollOwnrsh(self):
		del self._CollOwnrsh
		self._CollOwnrsh = None

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if type(value) != base_types.auto else self.make_default("CollVal")

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = None

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != base_types.auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	@property
	def LtdCvrgInd(self):
		return self._LtdCvrgInd

	@LtdCvrgInd.setter
	def LtdCvrgInd(self, value):
		self._LtdCvrgInd = value if type(value) != base_types.auto else self.make_default("LtdCvrgInd")

	@LtdCvrgInd.deleter
	def LtdCvrgInd(self):
		del self._LtdCvrgInd
		self._LtdCvrgInd = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOwnrsh', type=CollateralOwnership3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdCvrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=Price7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat29Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))