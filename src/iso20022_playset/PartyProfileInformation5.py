import base_types
import CertificationType1Choice
import KYCCheckType1Choice
import Max140Text
import RiskLevel2Choice
import EventFrequency1Code
import DataBaseCheck1
import YesNoIndicator
import CustomerConductClassification1Choice
import Max35Text
import ISODate

class PartyProfileInformation5(base_types._BaseFieldType):

	__slots__ = ["_CertfctnInd", "_KnowYourCstmrChckTp", "_SlryRg", "_ChckngDt", "_ChckngFrqcy", "_SrcOfWlth", "_RskLvl", "_ChckngPty", "_KnowYourCstmrDBChck", "_CertTp", "_NxtRvsnDt", "_VldtngPty", "_CstmrCndctClssfctn", "_RspnsblPty"]
	@property
	def CertfctnInd(self):
		return self._CertfctnInd

	@CertfctnInd.setter
	def CertfctnInd(self, value):
		self._CertfctnInd = value if type(value) != auto else self.make_default("CertfctnInd")

	@CertfctnInd.deleter
	def CertfctnInd(self):
		del self._CertfctnInd
		self._CertfctnInd = None

	@property
	def KnowYourCstmrChckTp(self):
		return self._KnowYourCstmrChckTp

	@KnowYourCstmrChckTp.setter
	def KnowYourCstmrChckTp(self, value):
		self._KnowYourCstmrChckTp = value if type(value) != auto else self.make_default("KnowYourCstmrChckTp")

	@KnowYourCstmrChckTp.deleter
	def KnowYourCstmrChckTp(self):
		del self._KnowYourCstmrChckTp
		self._KnowYourCstmrChckTp = None

	@property
	def SlryRg(self):
		return self._SlryRg

	@SlryRg.setter
	def SlryRg(self, value):
		self._SlryRg = value if type(value) != auto else self.make_default("SlryRg")

	@SlryRg.deleter
	def SlryRg(self):
		del self._SlryRg
		self._SlryRg = None

	@property
	def ChckngDt(self):
		return self._ChckngDt

	@ChckngDt.setter
	def ChckngDt(self, value):
		self._ChckngDt = value if type(value) != auto else self.make_default("ChckngDt")

	@ChckngDt.deleter
	def ChckngDt(self):
		del self._ChckngDt
		self._ChckngDt = None

	@property
	def ChckngFrqcy(self):
		return self._ChckngFrqcy

	@ChckngFrqcy.setter
	def ChckngFrqcy(self, value):
		self._ChckngFrqcy = value if type(value) != auto else self.make_default("ChckngFrqcy")

	@ChckngFrqcy.deleter
	def ChckngFrqcy(self):
		del self._ChckngFrqcy
		self._ChckngFrqcy = None

	@property
	def SrcOfWlth(self):
		return self._SrcOfWlth

	@SrcOfWlth.setter
	def SrcOfWlth(self, value):
		self._SrcOfWlth = value if type(value) != auto else self.make_default("SrcOfWlth")

	@SrcOfWlth.deleter
	def SrcOfWlth(self):
		del self._SrcOfWlth
		self._SrcOfWlth = None

	@property
	def RskLvl(self):
		return self._RskLvl

	@RskLvl.setter
	def RskLvl(self, value):
		self._RskLvl = value if type(value) != auto else self.make_default("RskLvl")

	@RskLvl.deleter
	def RskLvl(self):
		del self._RskLvl
		self._RskLvl = None

	@property
	def ChckngPty(self):
		return self._ChckngPty

	@ChckngPty.setter
	def ChckngPty(self, value):
		self._ChckngPty = value if type(value) != auto else self.make_default("ChckngPty")

	@ChckngPty.deleter
	def ChckngPty(self):
		del self._ChckngPty
		self._ChckngPty = None

	@property
	def KnowYourCstmrDBChck(self):
		return self._KnowYourCstmrDBChck

	@KnowYourCstmrDBChck.setter
	def KnowYourCstmrDBChck(self, value):
		self._KnowYourCstmrDBChck = value if type(value) != auto else self.make_default("KnowYourCstmrDBChck")

	@KnowYourCstmrDBChck.deleter
	def KnowYourCstmrDBChck(self):
		del self._KnowYourCstmrDBChck
		self._KnowYourCstmrDBChck = None

	@property
	def CertTp(self):
		return self._CertTp

	@CertTp.setter
	def CertTp(self, value):
		self._CertTp = value if type(value) != auto else self.make_default("CertTp")

	@CertTp.deleter
	def CertTp(self):
		del self._CertTp
		self._CertTp = None

	@property
	def NxtRvsnDt(self):
		return self._NxtRvsnDt

	@NxtRvsnDt.setter
	def NxtRvsnDt(self, value):
		self._NxtRvsnDt = value if type(value) != auto else self.make_default("NxtRvsnDt")

	@NxtRvsnDt.deleter
	def NxtRvsnDt(self):
		del self._NxtRvsnDt
		self._NxtRvsnDt = None

	@property
	def VldtngPty(self):
		return self._VldtngPty

	@VldtngPty.setter
	def VldtngPty(self, value):
		self._VldtngPty = value if type(value) != auto else self.make_default("VldtngPty")

	@VldtngPty.deleter
	def VldtngPty(self):
		del self._VldtngPty
		self._VldtngPty = None

	@property
	def CstmrCndctClssfctn(self):
		return self._CstmrCndctClssfctn

	@CstmrCndctClssfctn.setter
	def CstmrCndctClssfctn(self, value):
		self._CstmrCndctClssfctn = value if type(value) != auto else self.make_default("CstmrCndctClssfctn")

	@CstmrCndctClssfctn.deleter
	def CstmrCndctClssfctn(self):
		del self._CstmrCndctClssfctn
		self._CstmrCndctClssfctn = None

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if type(value) != auto else self.make_default("RspnsblPty")

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertfctnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KnowYourCstmrChckTp', type=KYCCheckType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlryRg', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckngFrqcy', type=EventFrequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfWlth', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskLvl', type=RiskLevel2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckngPty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KnowYourCstmrDBChck', type=DataBaseCheck1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertTp', type=CertificationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtRvsnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtngPty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

