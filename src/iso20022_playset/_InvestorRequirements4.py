# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestmentNeed2Choice
from . import OtherInvestmentNeed1
from . import SustainabilityPreferences2Code
from . import TargetMarket1Code
from . import TimeHorizon2Choice

class InvestorRequirements4(base_types._BaseFieldType):

	__slots__ = ["_MinHldgPrd", "_OptnOrLvrgdRtrPrfl", "_Othr", "_OthrSpcfcInvstmtNeed", "_RtrPrflGrwth", "_RtrPrflHdgg", "_RtrPrflIncm", "_RtrPrflPnsnSchmeDE", "_RtrPrflPrsrvtn", "_SstnbltyPrefs"]
	@property
	def MinHldgPrd(self):
		return self._MinHldgPrd

	@MinHldgPrd.setter
	def MinHldgPrd(self, value):
		self._MinHldgPrd = value if value is not None else base_types.UninitialisedField(self, 'MinHldgPrd', TimeHorizon2Choice, False)

	@MinHldgPrd.deleter
	def MinHldgPrd(self):
		del self._MinHldgPrd
		self._MinHldgPrd = base_types.UninitialisedField(self, 'MinHldgPrd', TimeHorizon2Choice, False)

	@property
	def OptnOrLvrgdRtrPrfl(self):
		return self._OptnOrLvrgdRtrPrfl

	@OptnOrLvrgdRtrPrfl.setter
	def OptnOrLvrgdRtrPrfl(self, value):
		self._OptnOrLvrgdRtrPrfl = value if value is not None else base_types.UninitialisedField(self, 'OptnOrLvrgdRtrPrfl', TargetMarket1Code, False)

	@OptnOrLvrgdRtrPrfl.deleter
	def OptnOrLvrgdRtrPrfl(self):
		del self._OptnOrLvrgdRtrPrfl
		self._OptnOrLvrgdRtrPrfl = base_types.UninitialisedField(self, 'OptnOrLvrgdRtrPrfl', TargetMarket1Code, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherInvestmentNeed1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherInvestmentNeed1, True)

	@property
	def OthrSpcfcInvstmtNeed(self):
		return self._OthrSpcfcInvstmtNeed

	@OthrSpcfcInvstmtNeed.setter
	def OthrSpcfcInvstmtNeed(self, value):
		self._OthrSpcfcInvstmtNeed = value if value is not None else base_types.UninitialisedField(self, 'OthrSpcfcInvstmtNeed', InvestmentNeed2Choice, False)

	@OthrSpcfcInvstmtNeed.deleter
	def OthrSpcfcInvstmtNeed(self):
		del self._OthrSpcfcInvstmtNeed
		self._OthrSpcfcInvstmtNeed = base_types.UninitialisedField(self, 'OthrSpcfcInvstmtNeed', InvestmentNeed2Choice, False)

	@property
	def RtrPrflGrwth(self):
		return self._RtrPrflGrwth

	@RtrPrflGrwth.setter
	def RtrPrflGrwth(self, value):
		self._RtrPrflGrwth = value if value is not None else base_types.UninitialisedField(self, 'RtrPrflGrwth', TargetMarket1Code, False)

	@RtrPrflGrwth.deleter
	def RtrPrflGrwth(self):
		del self._RtrPrflGrwth
		self._RtrPrflGrwth = base_types.UninitialisedField(self, 'RtrPrflGrwth', TargetMarket1Code, False)

	@property
	def RtrPrflHdgg(self):
		return self._RtrPrflHdgg

	@RtrPrflHdgg.setter
	def RtrPrflHdgg(self, value):
		self._RtrPrflHdgg = value if value is not None else base_types.UninitialisedField(self, 'RtrPrflHdgg', TargetMarket1Code, False)

	@RtrPrflHdgg.deleter
	def RtrPrflHdgg(self):
		del self._RtrPrflHdgg
		self._RtrPrflHdgg = base_types.UninitialisedField(self, 'RtrPrflHdgg', TargetMarket1Code, False)

	@property
	def RtrPrflIncm(self):
		return self._RtrPrflIncm

	@RtrPrflIncm.setter
	def RtrPrflIncm(self, value):
		self._RtrPrflIncm = value if value is not None else base_types.UninitialisedField(self, 'RtrPrflIncm', TargetMarket1Code, False)

	@RtrPrflIncm.deleter
	def RtrPrflIncm(self):
		del self._RtrPrflIncm
		self._RtrPrflIncm = base_types.UninitialisedField(self, 'RtrPrflIncm', TargetMarket1Code, False)

	@property
	def RtrPrflPnsnSchmeDE(self):
		return self._RtrPrflPnsnSchmeDE

	@RtrPrflPnsnSchmeDE.setter
	def RtrPrflPnsnSchmeDE(self, value):
		self._RtrPrflPnsnSchmeDE = value if value is not None else base_types.UninitialisedField(self, 'RtrPrflPnsnSchmeDE', TargetMarket1Code, False)

	@RtrPrflPnsnSchmeDE.deleter
	def RtrPrflPnsnSchmeDE(self):
		del self._RtrPrflPnsnSchmeDE
		self._RtrPrflPnsnSchmeDE = base_types.UninitialisedField(self, 'RtrPrflPnsnSchmeDE', TargetMarket1Code, False)

	@property
	def RtrPrflPrsrvtn(self):
		return self._RtrPrflPrsrvtn

	@RtrPrflPrsrvtn.setter
	def RtrPrflPrsrvtn(self, value):
		self._RtrPrflPrsrvtn = value if value is not None else base_types.UninitialisedField(self, 'RtrPrflPrsrvtn', TargetMarket1Code, False)

	@RtrPrflPrsrvtn.deleter
	def RtrPrflPrsrvtn(self):
		del self._RtrPrflPrsrvtn
		self._RtrPrflPrsrvtn = base_types.UninitialisedField(self, 'RtrPrflPrsrvtn', TargetMarket1Code, False)

	@property
	def SstnbltyPrefs(self):
		return self._SstnbltyPrefs

	@SstnbltyPrefs.setter
	def SstnbltyPrefs(self, value):
		self._SstnbltyPrefs = value if value is not None else base_types.UninitialisedField(self, 'SstnbltyPrefs', SustainabilityPreferences2Code, False)

	@SstnbltyPrefs.deleter
	def SstnbltyPrefs(self):
		del self._SstnbltyPrefs
		self._SstnbltyPrefs = base_types.UninitialisedField(self, 'SstnbltyPrefs', SustainabilityPreferences2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinHldgPrd', type=TimeHorizon2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnOrLvrgdRtrPrfl', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherInvestmentNeed1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrSpcfcInvstmtNeed', type=InvestmentNeed2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflGrwth', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflHdgg', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflIncm', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflPnsnSchmeDE', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrPrflPrsrvtn', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SstnbltyPrefs', type=SustainabilityPreferences2Code, min=0, max=1, mutex_group=None, array=False),
	))