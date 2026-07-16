# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertificationType1Choice
from . import CustomerConductClassification1Choice
from . import DataBaseCheck1
from . import EventFrequency1Code
from . import ISODate
from . import KYCCheckType1Choice
from . import Max140Text
from . import Max35Text
from . import RiskLevel2Choice
from . import YesNoIndicator

class PartyProfileInformation5(base_types._BaseFieldType):

	__slots__ = ["_CertTp", "_CertfctnInd", "_ChckngDt", "_ChckngFrqcy", "_ChckngPty", "_CstmrCndctClssfctn", "_KnowYourCstmrChckTp", "_KnowYourCstmrDBChck", "_NxtRvsnDt", "_RskLvl", "_RspnsblPty", "_SlryRg", "_SrcOfWlth", "_VldtngPty"]
	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if value is not None else base_types.UninitialisedField(self, 'CertTp', CertificationType1Choice, False)

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = base_types.UninitialisedField(self, 'CertTp', CertificationType1Choice, False)

	@property
	def CertfctnInd(self):
		return self._CertfctnInd

	@CertfctnInd.setter
	def CertfctnInd(self, value):
		self._CertfctnInd = value if value is not None else base_types.UninitialisedField(self, 'CertfctnInd', YesNoIndicator, False)

	@CertfctnInd.deleter
	def CertfctnInd(self):
		del self._CertfctnInd
		self._CertfctnInd = base_types.UninitialisedField(self, 'CertfctnInd', YesNoIndicator, False)

	@property
	def ChckngDt(self):
		return self._ChckngDt

	@ChckngDt.setter
	def ChckngDt(self, value):
		self._ChckngDt = value if value is not None else base_types.UninitialisedField(self, 'ChckngDt', ISODate, False)

	@ChckngDt.deleter
	def ChckngDt(self):
		del self._ChckngDt
		self._ChckngDt = base_types.UninitialisedField(self, 'ChckngDt', ISODate, False)

	@property
	def ChckngFrqcy(self):
		return self._ChckngFrqcy

	@ChckngFrqcy.setter
	def ChckngFrqcy(self, value):
		self._ChckngFrqcy = value if value is not None else base_types.UninitialisedField(self, 'ChckngFrqcy', EventFrequency1Code, False)

	@ChckngFrqcy.deleter
	def ChckngFrqcy(self):
		del self._ChckngFrqcy
		self._ChckngFrqcy = base_types.UninitialisedField(self, 'ChckngFrqcy', EventFrequency1Code, False)

	@property
	def ChckngPty(self):
		return self._ChckngPty

	@ChckngPty.setter
	def ChckngPty(self, value):
		self._ChckngPty = value if value is not None else base_types.UninitialisedField(self, 'ChckngPty', Max140Text, False)

	@ChckngPty.deleter
	def ChckngPty(self):
		del self._ChckngPty
		self._ChckngPty = base_types.UninitialisedField(self, 'ChckngPty', Max140Text, False)

	@property
	def CstmrCndctClssfctn(self):
		return self._CstmrCndctClssfctn

	@CstmrCndctClssfctn.setter
	def CstmrCndctClssfctn(self, value):
		self._CstmrCndctClssfctn = value if value is not None else base_types.UninitialisedField(self, 'CstmrCndctClssfctn', CustomerConductClassification1Choice, False)

	@CstmrCndctClssfctn.deleter
	def CstmrCndctClssfctn(self):
		del self._CstmrCndctClssfctn
		self._CstmrCndctClssfctn = base_types.UninitialisedField(self, 'CstmrCndctClssfctn', CustomerConductClassification1Choice, False)

	@property
	def KnowYourCstmrChckTp(self):
		return self._KnowYourCstmrChckTp

	@KnowYourCstmrChckTp.setter
	def KnowYourCstmrChckTp(self, value):
		self._KnowYourCstmrChckTp = value if value is not None else base_types.UninitialisedField(self, 'KnowYourCstmrChckTp', KYCCheckType1Choice, False)

	@KnowYourCstmrChckTp.deleter
	def KnowYourCstmrChckTp(self):
		del self._KnowYourCstmrChckTp
		self._KnowYourCstmrChckTp = base_types.UninitialisedField(self, 'KnowYourCstmrChckTp', KYCCheckType1Choice, False)

	@property
	def KnowYourCstmrDBChck(self):
		return self._KnowYourCstmrDBChck

	@KnowYourCstmrDBChck.setter
	def KnowYourCstmrDBChck(self, value):
		self._KnowYourCstmrDBChck = value if value is not None else base_types.UninitialisedField(self, 'KnowYourCstmrDBChck', DataBaseCheck1, False)

	@KnowYourCstmrDBChck.deleter
	def KnowYourCstmrDBChck(self):
		del self._KnowYourCstmrDBChck
		self._KnowYourCstmrDBChck = base_types.UninitialisedField(self, 'KnowYourCstmrDBChck', DataBaseCheck1, False)

	@property
	def NxtRvsnDt(self):
		return self._NxtRvsnDt

	@NxtRvsnDt.setter
	def NxtRvsnDt(self, value):
		self._NxtRvsnDt = value if value is not None else base_types.UninitialisedField(self, 'NxtRvsnDt', ISODate, False)

	@NxtRvsnDt.deleter
	def NxtRvsnDt(self):
		del self._NxtRvsnDt
		self._NxtRvsnDt = base_types.UninitialisedField(self, 'NxtRvsnDt', ISODate, False)

	@property
	def RskLvl(self):
		return self._RskLvl

	@RskLvl.setter
	def RskLvl(self, value):
		self._RskLvl = value if value is not None else base_types.UninitialisedField(self, 'RskLvl', RiskLevel2Choice, False)

	@RskLvl.deleter
	def RskLvl(self):
		del self._RskLvl
		self._RskLvl = base_types.UninitialisedField(self, 'RskLvl', RiskLevel2Choice, False)

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPty', Max140Text, False)

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = base_types.UninitialisedField(self, 'RspnsblPty', Max140Text, False)

	@property
	def SlryRg(self):
		return self._SlryRg

	@SlryRg.setter
	def SlryRg(self, value):
		self._SlryRg = value if value is not None else base_types.UninitialisedField(self, 'SlryRg', Max35Text, False)

	@SlryRg.deleter
	def SlryRg(self):
		del self._SlryRg
		self._SlryRg = base_types.UninitialisedField(self, 'SlryRg', Max35Text, False)

	@property
	def SrcOfWlth(self):
		return self._SrcOfWlth

	@SrcOfWlth.setter
	def SrcOfWlth(self, value):
		self._SrcOfWlth = value if value is not None else base_types.UninitialisedField(self, 'SrcOfWlth', Max140Text, False)

	@SrcOfWlth.deleter
	def SrcOfWlth(self):
		del self._SrcOfWlth
		self._SrcOfWlth = base_types.UninitialisedField(self, 'SrcOfWlth', Max140Text, False)

	@property
	def VldtngPty(self):
		return self._VldtngPty

	@VldtngPty.setter
	def VldtngPty(self, value):
		self._VldtngPty = value if value is not None else base_types.UninitialisedField(self, 'VldtngPty', Max140Text, False)

	@VldtngPty.deleter
	def VldtngPty(self):
		del self._VldtngPty
		self._VldtngPty = base_types.UninitialisedField(self, 'VldtngPty', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertTp', type=CertificationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckngFrqcy', type=EventFrequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckngPty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KnowYourCstmrChckTp', type=KYCCheckType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KnowYourCstmrDBChck', type=DataBaseCheck1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtRvsnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskLvl', type=RiskLevel2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlryRg', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfWlth', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtngPty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))