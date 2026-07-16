# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OtherTargetMarketInvestor1
from . import TargetMarket1Code
from . import TargetMarket3Code
from . import TargetMarket5Choice

class InvestorType2(base_types._BaseFieldType):

	__slots__ = ["_InvstrTpElgblCtrPty", "_InvstrTpPrfssnl", "_InvstrTpRtl", "_Othr"]
	@property
	def InvstrTpElgblCtrPty(self):
		return self._InvstrTpElgblCtrPty

	@InvstrTpElgblCtrPty.setter
	def InvstrTpElgblCtrPty(self, value):
		self._InvstrTpElgblCtrPty = value if value is not None else base_types.UninitialisedField(self, 'InvstrTpElgblCtrPty', TargetMarket3Code, False)

	@InvstrTpElgblCtrPty.deleter
	def InvstrTpElgblCtrPty(self):
		del self._InvstrTpElgblCtrPty
		self._InvstrTpElgblCtrPty = base_types.UninitialisedField(self, 'InvstrTpElgblCtrPty', TargetMarket3Code, False)

	@property
	def InvstrTpPrfssnl(self):
		return self._InvstrTpPrfssnl

	@InvstrTpPrfssnl.setter
	def InvstrTpPrfssnl(self, value):
		self._InvstrTpPrfssnl = value if value is not None else base_types.UninitialisedField(self, 'InvstrTpPrfssnl', TargetMarket5Choice, False)

	@InvstrTpPrfssnl.deleter
	def InvstrTpPrfssnl(self):
		del self._InvstrTpPrfssnl
		self._InvstrTpPrfssnl = base_types.UninitialisedField(self, 'InvstrTpPrfssnl', TargetMarket5Choice, False)

	@property
	def InvstrTpRtl(self):
		return self._InvstrTpRtl

	@InvstrTpRtl.setter
	def InvstrTpRtl(self, value):
		self._InvstrTpRtl = value if value is not None else base_types.UninitialisedField(self, 'InvstrTpRtl', TargetMarket1Code, False)

	@InvstrTpRtl.deleter
	def InvstrTpRtl(self):
		del self._InvstrTpRtl
		self._InvstrTpRtl = base_types.UninitialisedField(self, 'InvstrTpRtl', TargetMarket1Code, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherTargetMarketInvestor1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherTargetMarketInvestor1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrTpElgblCtrPty', type=TargetMarket3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTpPrfssnl', type=TargetMarket5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTpRtl', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketInvestor1, min=0, max=None, mutex_group=None, array=True),
	))