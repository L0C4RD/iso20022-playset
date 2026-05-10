from . import base_types
from ._Max140Text import Max140Text
from ._NotionalOrUnitBased1Choice import NotionalOrUnitBased1Choice
from ._Max350Text import Max350Text
from ._QuotationType1Choice import QuotationType1Choice
from ._SecurityClassificationType2Choice import SecurityClassificationType2Choice
from ._ProductStructure1Choice import ProductStructure1Choice
from ._SecurityIdentification40 import SecurityIdentification40
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._GovernanceProcess1Choice import GovernanceProcess1Choice
from ._CountryCode import CountryCode
from ._Max35Text import Max35Text
from ._YesNoIndicator import YesNoIndicator
from ._ExPostCostCalculationBasis1Choice import ExPostCostCalculationBasis1Choice
from ._ContactAttributes5 import ContactAttributes5
from ._AdditionalInformation15 import AdditionalInformation15

class SecurityIdentification47(base_types._BaseFieldType):

	__slots__ = ["_PdctCtgy", "_PdctCtgyDE", "_Issr", "_RegdDstrbtnCtry", "_UmbrllNm", "_ClssTp", "_Id", "_NoRtrcssnInd", "_PdctTp", "_Nm", "_ShrtNm", "_ClssfctnTp", "_BaseCcy", "_ExPstCostClctnBsis", "_NtnlOrUnitBased", "_LvrgdOrCntngntLblty", "_AddtlInf", "_NewUmbrll", "_IssrPdctGovncPrc", "_CtryOfDmcl", "_QtnTp"]
	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if type(value) != base_types.auto else self.make_default("PdctCtgy")

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = None

	@property
	def PdctCtgyDE(self):
		return self._PdctCtgyDE

	@PdctCtgyDE.setter
	def PdctCtgyDE(self, value):
		self._PdctCtgyDE = value if type(value) != base_types.auto else self.make_default("PdctCtgyDE")

	@PdctCtgyDE.deleter
	def PdctCtgyDE(self):
		del self._PdctCtgyDE
		self._PdctCtgyDE = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def RegdDstrbtnCtry(self):
		return self._RegdDstrbtnCtry

	@RegdDstrbtnCtry.setter
	def RegdDstrbtnCtry(self, value):
		self._RegdDstrbtnCtry = value if type(value) != base_types.auto else self.make_default("RegdDstrbtnCtry")

	@RegdDstrbtnCtry.deleter
	def RegdDstrbtnCtry(self):
		del self._RegdDstrbtnCtry
		self._RegdDstrbtnCtry = None

	@property
	def UmbrllNm(self):
		return self._UmbrllNm

	@UmbrllNm.setter
	def UmbrllNm(self, value):
		self._UmbrllNm = value if type(value) != base_types.auto else self.make_default("UmbrllNm")

	@UmbrllNm.deleter
	def UmbrllNm(self):
		del self._UmbrllNm
		self._UmbrllNm = None

	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if type(value) != base_types.auto else self.make_default("ClssTp")

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def NoRtrcssnInd(self):
		return self._NoRtrcssnInd

	@NoRtrcssnInd.setter
	def NoRtrcssnInd(self, value):
		self._NoRtrcssnInd = value if type(value) != base_types.auto else self.make_default("NoRtrcssnInd")

	@NoRtrcssnInd.deleter
	def NoRtrcssnInd(self):
		del self._NoRtrcssnInd
		self._NoRtrcssnInd = None

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if type(value) != base_types.auto else self.make_default("PdctTp")

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != base_types.auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if type(value) != base_types.auto else self.make_default("BaseCcy")

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = None

	@property
	def ExPstCostClctnBsis(self):
		return self._ExPstCostClctnBsis

	@ExPstCostClctnBsis.setter
	def ExPstCostClctnBsis(self, value):
		self._ExPstCostClctnBsis = value if type(value) != base_types.auto else self.make_default("ExPstCostClctnBsis")

	@ExPstCostClctnBsis.deleter
	def ExPstCostClctnBsis(self):
		del self._ExPstCostClctnBsis
		self._ExPstCostClctnBsis = None

	@property
	def NtnlOrUnitBased(self):
		return self._NtnlOrUnitBased

	@NtnlOrUnitBased.setter
	def NtnlOrUnitBased(self, value):
		self._NtnlOrUnitBased = value if type(value) != base_types.auto else self.make_default("NtnlOrUnitBased")

	@NtnlOrUnitBased.deleter
	def NtnlOrUnitBased(self):
		del self._NtnlOrUnitBased
		self._NtnlOrUnitBased = None

	@property
	def LvrgdOrCntngntLblty(self):
		return self._LvrgdOrCntngntLblty

	@LvrgdOrCntngntLblty.setter
	def LvrgdOrCntngntLblty(self, value):
		self._LvrgdOrCntngntLblty = value if type(value) != base_types.auto else self.make_default("LvrgdOrCntngntLblty")

	@LvrgdOrCntngntLblty.deleter
	def LvrgdOrCntngntLblty(self):
		del self._LvrgdOrCntngntLblty
		self._LvrgdOrCntngntLblty = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def NewUmbrll(self):
		return self._NewUmbrll

	@NewUmbrll.setter
	def NewUmbrll(self, value):
		self._NewUmbrll = value if type(value) != base_types.auto else self.make_default("NewUmbrll")

	@NewUmbrll.deleter
	def NewUmbrll(self):
		del self._NewUmbrll
		self._NewUmbrll = None

	@property
	def IssrPdctGovncPrc(self):
		return self._IssrPdctGovncPrc

	@IssrPdctGovncPrc.setter
	def IssrPdctGovncPrc(self, value):
		self._IssrPdctGovncPrc = value if type(value) != base_types.auto else self.make_default("IssrPdctGovncPrc")

	@IssrPdctGovncPrc.deleter
	def IssrPdctGovncPrc(self):
		del self._IssrPdctGovncPrc
		self._IssrPdctGovncPrc = None

	@property
	def CtryOfDmcl(self):
		return self._CtryOfDmcl

	@CtryOfDmcl.setter
	def CtryOfDmcl(self, value):
		self._CtryOfDmcl = value if type(value) != base_types.auto else self.make_default("CtryOfDmcl")

	@CtryOfDmcl.deleter
	def CtryOfDmcl(self):
		del self._CtryOfDmcl
		self._CtryOfDmcl = None

	@property
	def QtnTp(self):
		return self._QtnTp

	@QtnTp.setter
	def QtnTp(self, value):
		self._QtnTp = value if type(value) != base_types.auto else self.make_default("QtnTp")

	@QtnTp.deleter
	def QtnTp(self):
		del self._QtnTp
		self._QtnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdctCtgy', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCtgyDE', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdDstrbtnCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UmbrllNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoRtrcssnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=ProductStructure1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=SecurityClassificationType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExPstCostClctnBsis', type=ExPostCostCalculationBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlOrUnitBased', type=NotionalOrUnitBased1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LvrgdOrCntngntLblty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewUmbrll', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrPdctGovncPrc', type=GovernanceProcess1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfDmcl', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnTp', type=QuotationType1Choice, min=0, max=1, mutex_group=None, array=False),
	))

