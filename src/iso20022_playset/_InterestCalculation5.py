# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection20
from . import BlockChainAddressWallet5
from . import CollateralAccount3
from . import ISODate
from . import Number
from . import PercentageRate

class InterestCalculation5(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_AggtdIntrstAmt", "_BlckChainAdrOrWllt", "_ClctnDt", "_CollAcctId", "_FctvPrncplAmt", "_FctvRate", "_IntrstRate", "_MvmntAmt", "_NbOfDays", "_PrncplAmt", "_Sprd"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection20, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', AmountAndDirection20, False)

	@property
	def AggtdIntrstAmt(self):
		return self._AggtdIntrstAmt

	@AggtdIntrstAmt.setter
	def AggtdIntrstAmt(self, value):
		self._AggtdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AggtdIntrstAmt', ActiveCurrencyAndAmount, False)

	@AggtdIntrstAmt.deleter
	def AggtdIntrstAmt(self):
		del self._AggtdIntrstAmt
		self._AggtdIntrstAmt = base_types.UninitialisedField(self, 'AggtdIntrstAmt', ActiveCurrencyAndAmount, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet5, False)

	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if value is not None else base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if value is not None else base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = base_types.UninitialisedField(self, 'CollAcctId', CollateralAccount3, False)

	@property
	def FctvPrncplAmt(self):
		return self._FctvPrncplAmt

	@FctvPrncplAmt.setter
	def FctvPrncplAmt(self, value):
		self._FctvPrncplAmt = value if value is not None else base_types.UninitialisedField(self, 'FctvPrncplAmt', AmountAndDirection20, False)

	@FctvPrncplAmt.deleter
	def FctvPrncplAmt(self):
		del self._FctvPrncplAmt
		self._FctvPrncplAmt = base_types.UninitialisedField(self, 'FctvPrncplAmt', AmountAndDirection20, False)

	@property
	def FctvRate(self):
		return self._FctvRate

	@FctvRate.setter
	def FctvRate(self, value):
		self._FctvRate = value if value is not None else base_types.UninitialisedField(self, 'FctvRate', PercentageRate, False)

	@FctvRate.deleter
	def FctvRate(self):
		del self._FctvRate
		self._FctvRate = base_types.UninitialisedField(self, 'FctvRate', PercentageRate, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@property
	def MvmntAmt(self):
		return self._MvmntAmt

	@MvmntAmt.setter
	def MvmntAmt(self, value):
		self._MvmntAmt = value if value is not None else base_types.UninitialisedField(self, 'MvmntAmt', AmountAndDirection20, False)

	@MvmntAmt.deleter
	def MvmntAmt(self):
		del self._MvmntAmt
		self._MvmntAmt = base_types.UninitialisedField(self, 'MvmntAmt', AmountAndDirection20, False)

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if value is not None else base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	@property
	def PrncplAmt(self):
		return self._PrncplAmt

	@PrncplAmt.setter
	def PrncplAmt(self, value):
		self._PrncplAmt = value if value is not None else base_types.UninitialisedField(self, 'PrncplAmt', AmountAndDirection20, False)

	@PrncplAmt.deleter
	def PrncplAmt(self):
		del self._PrncplAmt
		self._PrncplAmt = base_types.UninitialisedField(self, 'PrncplAmt', AmountAndDirection20, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', PercentageRate, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdIntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvPrncplAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))