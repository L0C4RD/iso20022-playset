import base_types
import TargetMarket5Choice
import TargetMarket1Code
import TargetMarket3Code
import OtherTargetMarketInvestor1

class InvestorType2(base_types._BaseFieldType):

	__slots__ = ["_InvstrTpElgblCtrPty", "_InvstrTpPrfssnl", "_InvstrTpRtl", "_Othr"]
	@property
	def InvstrTpElgblCtrPty(self):
		return self._InvstrTpElgblCtrPty

	@InvstrTpElgblCtrPty.setter
	def InvstrTpElgblCtrPty(self, value):
		self._InvstrTpElgblCtrPty = value if type(value) != auto else self.make_default("InvstrTpElgblCtrPty")

	@InvstrTpElgblCtrPty.deleter
	def InvstrTpElgblCtrPty(self):
		del self._InvstrTpElgblCtrPty
		self._InvstrTpElgblCtrPty = None

	@property
	def InvstrTpPrfssnl(self):
		return self._InvstrTpPrfssnl

	@InvstrTpPrfssnl.setter
	def InvstrTpPrfssnl(self, value):
		self._InvstrTpPrfssnl = value if type(value) != auto else self.make_default("InvstrTpPrfssnl")

	@InvstrTpPrfssnl.deleter
	def InvstrTpPrfssnl(self):
		del self._InvstrTpPrfssnl
		self._InvstrTpPrfssnl = None

	@property
	def InvstrTpRtl(self):
		return self._InvstrTpRtl

	@InvstrTpRtl.setter
	def InvstrTpRtl(self, value):
		self._InvstrTpRtl = value if type(value) != auto else self.make_default("InvstrTpRtl")

	@InvstrTpRtl.deleter
	def InvstrTpRtl(self):
		del self._InvstrTpRtl
		self._InvstrTpRtl = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrTpElgblCtrPty', type=TargetMarket3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTpPrfssnl', type=TargetMarket5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTpRtl', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketInvestor1, min=0, max=None, mutex_group=None, array=True),
	))

