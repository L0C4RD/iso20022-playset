# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AdditionalInformation15
from . import ContactAttributes5
from . import CountryCode
from . import ExPostCostCalculationBasis1Choice
from . import GovernanceProcess1Choice
from . import Max140Text
from . import Max350Text
from . import Max35Text
from . import NotionalOrUnitBased1Choice
from . import ProductStructure1Choice
from . import QuotationType1Choice
from . import SecurityClassificationType2Choice
from . import SecurityIdentification40
from . import YesNoIndicator

class SecurityIdentification47(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_BaseCcy", "_ClssTp", "_ClssfctnTp", "_CtryOfDmcl", "_ExPstCostClctnBsis", "_Id", "_Issr", "_IssrPdctGovncPrc", "_LvrgdOrCntngntLblty", "_NewUmbrll", "_Nm", "_NoRtrcssnInd", "_NtnlOrUnitBased", "_PdctCtgy", "_PdctCtgyDE", "_PdctTp", "_QtnTp", "_RegdDstrbtnCtry", "_ShrtNm", "_UmbrllNm"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if value is not None else base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = base_types.UninitialisedField(self, 'BaseCcy', ActiveCurrencyCode, False)

	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if value is not None else base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = base_types.UninitialisedField(self, 'ClssTp', Max35Text, False)

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', SecurityClassificationType2Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', SecurityClassificationType2Choice, False)

	@property
	def CtryOfDmcl(self):
		return self._CtryOfDmcl

	@CtryOfDmcl.setter
	def CtryOfDmcl(self, value):
		self._CtryOfDmcl = value if value is not None else base_types.UninitialisedField(self, 'CtryOfDmcl', CountryCode, False)

	@CtryOfDmcl.deleter
	def CtryOfDmcl(self):
		del self._CtryOfDmcl
		self._CtryOfDmcl = base_types.UninitialisedField(self, 'CtryOfDmcl', CountryCode, False)

	@property
	def ExPstCostClctnBsis(self):
		return self._ExPstCostClctnBsis

	@ExPstCostClctnBsis.setter
	def ExPstCostClctnBsis(self, value):
		self._ExPstCostClctnBsis = value if value is not None else base_types.UninitialisedField(self, 'ExPstCostClctnBsis', ExPostCostCalculationBasis1Choice, False)

	@ExPstCostClctnBsis.deleter
	def ExPstCostClctnBsis(self):
		del self._ExPstCostClctnBsis
		self._ExPstCostClctnBsis = base_types.UninitialisedField(self, 'ExPstCostClctnBsis', ExPostCostCalculationBasis1Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentification40, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentification40, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', ContactAttributes5, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', ContactAttributes5, False)

	@property
	def IssrPdctGovncPrc(self):
		return self._IssrPdctGovncPrc

	@IssrPdctGovncPrc.setter
	def IssrPdctGovncPrc(self, value):
		self._IssrPdctGovncPrc = value if value is not None else base_types.UninitialisedField(self, 'IssrPdctGovncPrc', GovernanceProcess1Choice, False)

	@IssrPdctGovncPrc.deleter
	def IssrPdctGovncPrc(self):
		del self._IssrPdctGovncPrc
		self._IssrPdctGovncPrc = base_types.UninitialisedField(self, 'IssrPdctGovncPrc', GovernanceProcess1Choice, False)

	@property
	def LvrgdOrCntngntLblty(self):
		return self._LvrgdOrCntngntLblty

	@LvrgdOrCntngntLblty.setter
	def LvrgdOrCntngntLblty(self, value):
		self._LvrgdOrCntngntLblty = value if value is not None else base_types.UninitialisedField(self, 'LvrgdOrCntngntLblty', YesNoIndicator, False)

	@LvrgdOrCntngntLblty.deleter
	def LvrgdOrCntngntLblty(self):
		del self._LvrgdOrCntngntLblty
		self._LvrgdOrCntngntLblty = base_types.UninitialisedField(self, 'LvrgdOrCntngntLblty', YesNoIndicator, False)

	@property
	def NewUmbrll(self):
		return self._NewUmbrll

	@NewUmbrll.setter
	def NewUmbrll(self, value):
		self._NewUmbrll = value if value is not None else base_types.UninitialisedField(self, 'NewUmbrll', YesNoIndicator, False)

	@NewUmbrll.deleter
	def NewUmbrll(self):
		del self._NewUmbrll
		self._NewUmbrll = base_types.UninitialisedField(self, 'NewUmbrll', YesNoIndicator, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def NoRtrcssnInd(self):
		return self._NoRtrcssnInd

	@NoRtrcssnInd.setter
	def NoRtrcssnInd(self, value):
		self._NoRtrcssnInd = value if value is not None else base_types.UninitialisedField(self, 'NoRtrcssnInd', YesNoIndicator, False)

	@NoRtrcssnInd.deleter
	def NoRtrcssnInd(self):
		del self._NoRtrcssnInd
		self._NoRtrcssnInd = base_types.UninitialisedField(self, 'NoRtrcssnInd', YesNoIndicator, False)

	@property
	def NtnlOrUnitBased(self):
		return self._NtnlOrUnitBased

	@NtnlOrUnitBased.setter
	def NtnlOrUnitBased(self, value):
		self._NtnlOrUnitBased = value if value is not None else base_types.UninitialisedField(self, 'NtnlOrUnitBased', NotionalOrUnitBased1Choice, False)

	@NtnlOrUnitBased.deleter
	def NtnlOrUnitBased(self):
		del self._NtnlOrUnitBased
		self._NtnlOrUnitBased = base_types.UninitialisedField(self, 'NtnlOrUnitBased', NotionalOrUnitBased1Choice, False)

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if value is not None else base_types.UninitialisedField(self, 'PdctCtgy', Max140Text, False)

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = base_types.UninitialisedField(self, 'PdctCtgy', Max140Text, False)

	@property
	def PdctCtgyDE(self):
		return self._PdctCtgyDE

	@PdctCtgyDE.setter
	def PdctCtgyDE(self, value):
		self._PdctCtgyDE = value if value is not None else base_types.UninitialisedField(self, 'PdctCtgyDE', Max140Text, False)

	@PdctCtgyDE.deleter
	def PdctCtgyDE(self):
		del self._PdctCtgyDE
		self._PdctCtgyDE = base_types.UninitialisedField(self, 'PdctCtgyDE', Max140Text, False)

	@property
	def PdctTp(self):
		return self._PdctTp

	@PdctTp.setter
	def PdctTp(self, value):
		self._PdctTp = value if value is not None else base_types.UninitialisedField(self, 'PdctTp', ProductStructure1Choice, False)

	@PdctTp.deleter
	def PdctTp(self):
		del self._PdctTp
		self._PdctTp = base_types.UninitialisedField(self, 'PdctTp', ProductStructure1Choice, False)

	@property
	def QtnTp(self):
		return self._QtnTp

	@QtnTp.setter
	def QtnTp(self, value):
		self._QtnTp = value if value is not None else base_types.UninitialisedField(self, 'QtnTp', QuotationType1Choice, False)

	@QtnTp.deleter
	def QtnTp(self):
		del self._QtnTp
		self._QtnTp = base_types.UninitialisedField(self, 'QtnTp', QuotationType1Choice, False)

	@property
	def RegdDstrbtnCtry(self):
		return self._RegdDstrbtnCtry

	@RegdDstrbtnCtry.setter
	def RegdDstrbtnCtry(self, value):
		self._RegdDstrbtnCtry = value if value is not None else base_types.UninitialisedField(self, 'RegdDstrbtnCtry', CountryCode, True)

	@RegdDstrbtnCtry.deleter
	def RegdDstrbtnCtry(self):
		del self._RegdDstrbtnCtry
		self._RegdDstrbtnCtry = base_types.UninitialisedField(self, 'RegdDstrbtnCtry', CountryCode, True)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@property
	def UmbrllNm(self):
		return self._UmbrllNm

	@UmbrllNm.setter
	def UmbrllNm(self, value):
		self._UmbrllNm = value if value is not None else base_types.UninitialisedField(self, 'UmbrllNm', Max35Text, False)

	@UmbrllNm.deleter
	def UmbrllNm(self):
		del self._UmbrllNm
		self._UmbrllNm = base_types.UninitialisedField(self, 'UmbrllNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnTp', type=SecurityClassificationType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfDmcl', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExPstCostClctnBsis', type=ExPostCostCalculationBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrPdctGovncPrc', type=GovernanceProcess1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LvrgdOrCntngntLblty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewUmbrll', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoRtrcssnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlOrUnitBased', type=NotionalOrUnitBased1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCtgy', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCtgyDE', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctTp', type=ProductStructure1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnTp', type=QuotationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdDstrbtnCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UmbrllNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))