from . import base_types
import TimeHorizon2Choice
import OtherInvestmentNeed1
import TargetMarket1Code
import InvestmentNeed2Choice
import SustainabilityPreferences2Code

class InvestorRequirements4(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_SstnbltyPrefs", "_OthrSpcfcInvstmtNeed", "_RtrPrflIncm", "_RtrPrflPrsrvtn", "_RtrPrflHdgg", "_MinHldgPrd", "_RtrPrflGrwth", "_RtrPrflPnsnSchmeDE", "_OptnOrLvrgdRtrPrfl"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def SstnbltyPrefs(self):
		return self._SstnbltyPrefs

	@SstnbltyPrefs.setter
	def SstnbltyPrefs(self, value):
		self._SstnbltyPrefs = value if type(value) != auto else self.make_default("SstnbltyPrefs")

	@SstnbltyPrefs.deleter
	def SstnbltyPrefs(self):
		del self._SstnbltyPrefs
		self._SstnbltyPrefs = None

	@property
	def OthrSpcfcInvstmtNeed(self):
		return self._OthrSpcfcInvstmtNeed

	@OthrSpcfcInvstmtNeed.setter
	def OthrSpcfcInvstmtNeed(self, value):
		self._OthrSpcfcInvstmtNeed = value if type(value) != auto else self.make_default("OthrSpcfcInvstmtNeed")

	@OthrSpcfcInvstmtNeed.deleter
	def OthrSpcfcInvstmtNeed(self):
		del self._OthrSpcfcInvstmtNeed
		self._OthrSpcfcInvstmtNeed = None

	@property
	def RtrPrflIncm(self):
		return self._RtrPrflIncm

	@RtrPrflIncm.setter
	def RtrPrflIncm(self, value):
		self._RtrPrflIncm = value if type(value) != auto else self.make_default("RtrPrflIncm")

	@RtrPrflIncm.deleter
	def RtrPrflIncm(self):
		del self._RtrPrflIncm
		self._RtrPrflIncm = None

	@property
	def RtrPrflPrsrvtn(self):
		return self._RtrPrflPrsrvtn

	@RtrPrflPrsrvtn.setter
	def RtrPrflPrsrvtn(self, value):
		self._RtrPrflPrsrvtn = value if type(value) != auto else self.make_default("RtrPrflPrsrvtn")

	@RtrPrflPrsrvtn.deleter
	def RtrPrflPrsrvtn(self):
		del self._RtrPrflPrsrvtn
		self._RtrPrflPrsrvtn = None

	@property
	def RtrPrflHdgg(self):
		return self._RtrPrflHdgg

	@RtrPrflHdgg.setter
	def RtrPrflHdgg(self, value):
		self._RtrPrflHdgg = value if type(value) != auto else self.make_default("RtrPrflHdgg")

	@RtrPrflHdgg.deleter
	def RtrPrflHdgg(self):
		del self._RtrPrflHdgg
		self._RtrPrflHdgg = None

	@property
	def MinHldgPrd(self):
		return self._MinHldgPrd

	@MinHldgPrd.setter
	def MinHldgPrd(self, value):
		self._MinHldgPrd = value if type(value) != auto else self.make_default("MinHldgPrd")

	@MinHldgPrd.deleter
	def MinHldgPrd(self):
		del self._MinHldgPrd
		self._MinHldgPrd = None

	@property
	def RtrPrflGrwth(self):
		return self._RtrPrflGrwth

	@RtrPrflGrwth.setter
	def RtrPrflGrwth(self, value):
		self._RtrPrflGrwth = value if type(value) != auto else self.make_default("RtrPrflGrwth")

	@RtrPrflGrwth.deleter
	def RtrPrflGrwth(self):
		del self._RtrPrflGrwth
		self._RtrPrflGrwth = None

	@property
	def RtrPrflPnsnSchmeDE(self):
		return self._RtrPrflPnsnSchmeDE

	@RtrPrflPnsnSchmeDE.setter
	def RtrPrflPnsnSchmeDE(self, value):
		self._RtrPrflPnsnSchmeDE = value if type(value) != auto else self.make_default("RtrPrflPnsnSchmeDE")

	@RtrPrflPnsnSchmeDE.deleter
	def RtrPrflPnsnSchmeDE(self):
		del self._RtrPrflPnsnSchmeDE
		self._RtrPrflPnsnSchmeDE = None

	@property
	def OptnOrLvrgdRtrPrfl(self):
		return self._OptnOrLvrgdRtrPrfl

	@OptnOrLvrgdRtrPrfl.setter
	def OptnOrLvrgdRtrPrfl(self, value):
		self._OptnOrLvrgdRtrPrfl = value if type(value) != auto else self.make_default("OptnOrLvrgdRtrPrfl")

	@OptnOrLvrgdRtrPrfl.deleter
	def OptnOrLvrgdRtrPrfl(self):
		del self._OptnOrLvrgdRtrPrfl
		self._OptnOrLvrgdRtrPrfl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=OtherInvestmentNeed1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SstnbltyPrefs', type=SustainabilityPreferences2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrSpcfcInvstmtNeed', type=InvestmentNeed2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflIncm', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflPrsrvtn', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflHdgg', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinHldgPrd', type=TimeHorizon2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflGrwth', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflPnsnSchmeDE', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnOrLvrgdRtrPrfl', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
	))

