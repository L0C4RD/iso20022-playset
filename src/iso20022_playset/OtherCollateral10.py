import base_types
import OtherTypeOfCollateral3
import BaseOneRate
import CollateralOwnership3
import PercentageRate
import BlockChainAddressWallet3
import SafekeepingPlaceFormat29Choice
import PartyIdentification178Choice
import ActiveCurrencyAndAmount
import FinancialInstrumentQuantity33Choice
import SecuritiesAccount19
import DateFormat14Choice
import YesNoIndicator
import Max35Text
import ISODate

class OtherCollateral10(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_CollOwnrsh", "_ValDt", "_XchgRate", "_OthrTpOfColl", "_LtdCvrgInd", "_XpryDt", "_Hrcut", "_GrntAmt", "_CollVal", "_MktVal", "_BlckChainAdrOrWllt", "_IsseDt", "_SfkpgPlc", "_LttrOfCdtId", "_LttrOfCdtAmt", "_AsstNb", "_SfkpgAcct", "_BlckdQty"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def CollOwnrsh(self):
		return self._CollOwnrsh

	@CollOwnrsh.setter
	def CollOwnrsh(self, value):
		self._CollOwnrsh = value if type(value) != auto else self.make_default("CollOwnrsh")

	@CollOwnrsh.deleter
	def CollOwnrsh(self):
		del self._CollOwnrsh
		self._CollOwnrsh = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	@property
	def OthrTpOfColl(self):
		return self._OthrTpOfColl

	@OthrTpOfColl.setter
	def OthrTpOfColl(self, value):
		self._OthrTpOfColl = value if type(value) != auto else self.make_default("OthrTpOfColl")

	@OthrTpOfColl.deleter
	def OthrTpOfColl(self):
		del self._OthrTpOfColl
		self._OthrTpOfColl = None

	@property
	def LtdCvrgInd(self):
		return self._LtdCvrgInd

	@LtdCvrgInd.setter
	def LtdCvrgInd(self, value):
		self._LtdCvrgInd = value if type(value) != auto else self.make_default("LtdCvrgInd")

	@LtdCvrgInd.deleter
	def LtdCvrgInd(self):
		del self._LtdCvrgInd
		self._LtdCvrgInd = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	@property
	def GrntAmt(self):
		return self._GrntAmt

	@GrntAmt.setter
	def GrntAmt(self, value):
		self._GrntAmt = value if type(value) != auto else self.make_default("GrntAmt")

	@GrntAmt.deleter
	def GrntAmt(self):
		del self._GrntAmt
		self._GrntAmt = None

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if type(value) != auto else self.make_default("CollVal")

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

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
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def LttrOfCdtId(self):
		return self._LttrOfCdtId

	@LttrOfCdtId.setter
	def LttrOfCdtId(self, value):
		self._LttrOfCdtId = value if type(value) != auto else self.make_default("LttrOfCdtId")

	@LttrOfCdtId.deleter
	def LttrOfCdtId(self):
		del self._LttrOfCdtId
		self._LttrOfCdtId = None

	@property
	def LttrOfCdtAmt(self):
		return self._LttrOfCdtAmt

	@LttrOfCdtAmt.setter
	def LttrOfCdtAmt(self, value):
		self._LttrOfCdtAmt = value if type(value) != auto else self.make_default("LttrOfCdtAmt")

	@LttrOfCdtAmt.deleter
	def LttrOfCdtAmt(self):
		del self._LttrOfCdtAmt
		self._LttrOfCdtAmt = None

	@property
	def AsstNb(self):
		return self._AsstNb

	@AsstNb.setter
	def AsstNb(self, value):
		self._AsstNb = value if type(value) != auto else self.make_default("AsstNb")

	@AsstNb.deleter
	def AsstNb(self):
		del self._AsstNb
		self._AsstNb = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def BlckdQty(self):
		return self._BlckdQty

	@BlckdQty.setter
	def BlckdQty(self, value):
		self._BlckdQty = value if type(value) != auto else self.make_default("BlckdQty")

	@BlckdQty.deleter
	def BlckdQty(self):
		del self._BlckdQty
		self._BlckdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollOwnrsh', type=CollateralOwnership3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTpOfColl', type=OtherTypeOfCollateral3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdCvrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=DateFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfCdtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfCdtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckdQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
	))

