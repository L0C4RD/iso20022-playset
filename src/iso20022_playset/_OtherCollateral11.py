# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BaseOneRate
from . import BlockChainAddressWallet3
from . import DateFormat14Choice
from . import ISODate
from . import Max35Text
from . import OtherTypeOfCollateral3
from . import PartyIdentification178Choice
from . import PercentageRate
from . import SafekeepingPlaceFormat29Choice
from . import SecuritiesAccount19
from . import YesNoIndicator

class OtherCollateral11(base_types._BaseFieldType):

	__slots__ = ["_AsstNb", "_BlckChainAdrOrWllt", "_CollId", "_CollVal", "_GrntAmt", "_Hrcut", "_IsseDt", "_Issr", "_LtdCvrgInd", "_LttrOfCdtAmt", "_LttrOfCdtId", "_MktVal", "_OthrTpOfColl", "_SfkpgAcct", "_SfkpgPlc", "_ValDt", "_XchgRate", "_XpryDt"]
	@property
	def AsstNb(self):
		return self._AsstNb

	@AsstNb.setter
	def AsstNb(self, value):
		self._AsstNb = value if value is not None else base_types.UninitialisedField(self, 'AsstNb', Max35Text, False)

	@AsstNb.deleter
	def AsstNb(self):
		del self._AsstNb
		self._AsstNb = base_types.UninitialisedField(self, 'AsstNb', Max35Text, False)

	@property
	def BlckChainAdrOrWllt(self):
		return self._BlckChainAdrOrWllt

	@BlckChainAdrOrWllt.setter
	def BlckChainAdrOrWllt(self, value):
		self._BlckChainAdrOrWllt = value if value is not None else base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@BlckChainAdrOrWllt.deleter
	def BlckChainAdrOrWllt(self):
		del self._BlckChainAdrOrWllt
		self._BlckChainAdrOrWllt = base_types.UninitialisedField(self, 'BlckChainAdrOrWllt', BlockChainAddressWallet3, False)

	@property
	def CollId(self):
		return self._CollId

	@CollId.setter
	def CollId(self, value):
		self._CollId = value if value is not None else base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@CollId.deleter
	def CollId(self):
		del self._CollId
		self._CollId = base_types.UninitialisedField(self, 'CollId', Max35Text, False)

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if value is not None else base_types.UninitialisedField(self, 'CollVal', ActiveCurrencyAndAmount, False)

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = base_types.UninitialisedField(self, 'CollVal', ActiveCurrencyAndAmount, False)

	@property
	def GrntAmt(self):
		return self._GrntAmt

	@GrntAmt.setter
	def GrntAmt(self, value):
		self._GrntAmt = value if value is not None else base_types.UninitialisedField(self, 'GrntAmt', ActiveCurrencyAndAmount, False)

	@GrntAmt.deleter
	def GrntAmt(self):
		del self._GrntAmt
		self._GrntAmt = base_types.UninitialisedField(self, 'GrntAmt', ActiveCurrencyAndAmount, False)

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if value is not None else base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', DateFormat14Choice, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', DateFormat14Choice, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification178Choice, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification178Choice, False)

	@property
	def LtdCvrgInd(self):
		return self._LtdCvrgInd

	@LtdCvrgInd.setter
	def LtdCvrgInd(self, value):
		self._LtdCvrgInd = value if value is not None else base_types.UninitialisedField(self, 'LtdCvrgInd', YesNoIndicator, False)

	@LtdCvrgInd.deleter
	def LtdCvrgInd(self):
		del self._LtdCvrgInd
		self._LtdCvrgInd = base_types.UninitialisedField(self, 'LtdCvrgInd', YesNoIndicator, False)

	@property
	def LttrOfCdtAmt(self):
		return self._LttrOfCdtAmt

	@LttrOfCdtAmt.setter
	def LttrOfCdtAmt(self, value):
		self._LttrOfCdtAmt = value if value is not None else base_types.UninitialisedField(self, 'LttrOfCdtAmt', ActiveCurrencyAndAmount, False)

	@LttrOfCdtAmt.deleter
	def LttrOfCdtAmt(self):
		del self._LttrOfCdtAmt
		self._LttrOfCdtAmt = base_types.UninitialisedField(self, 'LttrOfCdtAmt', ActiveCurrencyAndAmount, False)

	@property
	def LttrOfCdtId(self):
		return self._LttrOfCdtId

	@LttrOfCdtId.setter
	def LttrOfCdtId(self, value):
		self._LttrOfCdtId = value if value is not None else base_types.UninitialisedField(self, 'LttrOfCdtId', Max35Text, False)

	@LttrOfCdtId.deleter
	def LttrOfCdtId(self):
		del self._LttrOfCdtId
		self._LttrOfCdtId = base_types.UninitialisedField(self, 'LttrOfCdtId', Max35Text, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', ActiveCurrencyAndAmount, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', ActiveCurrencyAndAmount, False)

	@property
	def OthrTpOfColl(self):
		return self._OthrTpOfColl

	@OthrTpOfColl.setter
	def OthrTpOfColl(self, value):
		self._OthrTpOfColl = value if value is not None else base_types.UninitialisedField(self, 'OthrTpOfColl', OtherTypeOfCollateral3, False)

	@OthrTpOfColl.deleter
	def OthrTpOfColl(self):
		del self._OthrTpOfColl
		self._OthrTpOfColl = base_types.UninitialisedField(self, 'OthrTpOfColl', OtherTypeOfCollateral3, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat29Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat29Choice, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', ISODate, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', DateFormat14Choice, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', DateFormat14Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckChainAdrOrWllt', type=BlockChainAddressWallet3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=DateFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdCvrgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfCdtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrOfCdtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTpOfColl', type=OtherTypeOfCollateral3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateFormat14Choice, min=0, max=1, mutex_group=None, array=False),
	))