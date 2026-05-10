import base_types
import CollateralAccount3
import AmountAndDirection20
import PercentageRate
import BlockChainAddressWallet5
import ActiveCurrencyAndAmount
import Number
import ISODate

class InterestCalculation5(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_NbOfDays", "_CollAcctId", "_Sprd", "_FctvPrncplAmt", "_BlckChainAdrOrWllt", "_ClctnDt", "_IntrstRate", "_AggtdIntrstAmt", "_PrncplAmt", "_MvmntAmt", "_FctvRate"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if type(value) != auto else self.make_default("NbOfDays")

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = None

	@property
	def CollAcctId(self):
		return self._CollAcctId

	@CollAcctId.setter
	def CollAcctId(self, value):
		self._CollAcctId = value if type(value) != auto else self.make_default("CollAcctId")

	@CollAcctId.deleter
	def CollAcctId(self):
		del self._CollAcctId
		self._CollAcctId = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def FctvPrncplAmt(self):
		return self._FctvPrncplAmt

	@FctvPrncplAmt.setter
	def FctvPrncplAmt(self, value):
		self._FctvPrncplAmt = value if type(value) != auto else self.make_default("FctvPrncplAmt")

	@FctvPrncplAmt.deleter
	def FctvPrncplAmt(self):
		del self._FctvPrncplAmt
		self._FctvPrncplAmt = None

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if type(value) != auto else self.make_default("BlckChainAdrOrWllt")

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = None

	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if type(value) != auto else self.make_default("ClctnDt")

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def AggtdIntrstAmt(self):
		return self._AggtdIntrstAmt

	@AggtdIntrstAmt.setter
	def AggtdIntrstAmt(self, value):
		self._AggtdIntrstAmt = value if type(value) != auto else self.make_default("AggtdIntrstAmt")

	@AggtdIntrstAmt.deleter
	def AggtdIntrstAmt(self):
		del self._AggtdIntrstAmt
		self._AggtdIntrstAmt = None

	@property
	def PrncplAmt(self):
		return self._PrncplAmt

	@PrncplAmt.setter
	def PrncplAmt(self, value):
		self._PrncplAmt = value if type(value) != auto else self.make_default("PrncplAmt")

	@PrncplAmt.deleter
	def PrncplAmt(self):
		del self._PrncplAmt
		self._PrncplAmt = None

	@property
	def MvmntAmt(self):
		return self._MvmntAmt

	@MvmntAmt.setter
	def MvmntAmt(self, value):
		self._MvmntAmt = value if type(value) != auto else self.make_default("MvmntAmt")

	@MvmntAmt.deleter
	def MvmntAmt(self):
		del self._MvmntAmt
		self._MvmntAmt = None

	@property
	def FctvRate(self):
		return self._FctvRate

	@FctvRate.setter
	def FctvRate(self, value):
		self._FctvRate = value if type(value) != auto else self.make_default("FctvRate")

	@FctvRate.deleter
	def FctvRate(self):
		del self._FctvRate
		self._FctvRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctId', type=CollateralAccount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvPrncplAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdIntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrncplAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntAmt', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))

