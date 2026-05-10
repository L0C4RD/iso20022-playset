from . import base_types
from .FormOfSecurity1Code import FormOfSecurity1Code
from .CountryCode import CountryCode
from .Max35Text import Max35Text
from .RestrictedFINXMax140Text import RestrictedFINXMax140Text
from .ActiveCurrencyCode import ActiveCurrencyCode
from .DistributionPolicy1Code import DistributionPolicy1Code
from .YesNoIndicator import YesNoIndicator
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class FinancialInstrument22(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_DstrbtnPlcy", "_RegdDstrbtnCtry", "_DualFndInd", "_BaseCcy", "_PdctGrp", "_DnmtnCcy", "_SctiesForm", "_UmbrllNm", "_ReqdNAVCcy", "_CtryOfDmcl"]
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
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if type(value) != base_types.auto else self.make_default("DstrbtnPlcy")

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = None

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
	def DualFndInd(self):
		return self._DualFndInd

	@DualFndInd.setter
	def DualFndInd(self, value):
		self._DualFndInd = value if type(value) != base_types.auto else self.make_default("DualFndInd")

	@DualFndInd.deleter
	def DualFndInd(self):
		del self._DualFndInd
		self._DualFndInd = None

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
	def PdctGrp(self):
		return self._PdctGrp

	@PdctGrp.setter
	def PdctGrp(self, value):
		self._PdctGrp = value if type(value) != base_types.auto else self.make_default("PdctGrp")

	@PdctGrp.deleter
	def PdctGrp(self):
		del self._PdctGrp
		self._PdctGrp = None

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if type(value) != base_types.auto else self.make_default("DnmtnCcy")

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = None

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if type(value) != base_types.auto else self.make_default("SctiesForm")

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = None

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
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if type(value) != base_types.auto else self.make_default("ReqdNAVCcy")

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdDstrbtnCtry', type=CountryCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DualFndInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctGrp', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UmbrllNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfDmcl', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

