from . import base_types
import TargetMarket1Code
import OtherTargetMarketInvestorKnowledge1

class InvestorKnowledge1(base_types._BaseFieldType):

	__slots__ = ["_InfrmdInvstr", "_Othr", "_AdvncdInvstr", "_BsicInvstr", "_ExprtInvstrDE"]
	@property
	def InfrmdInvstr(self):
		return self._InfrmdInvstr

	@InfrmdInvstr.setter
	def InfrmdInvstr(self, value):
		self._InfrmdInvstr = value if type(value) != auto else self.make_default("InfrmdInvstr")

	@InfrmdInvstr.deleter
	def InfrmdInvstr(self):
		del self._InfrmdInvstr
		self._InfrmdInvstr = None

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
	def AdvncdInvstr(self):
		return self._AdvncdInvstr

	@AdvncdInvstr.setter
	def AdvncdInvstr(self, value):
		self._AdvncdInvstr = value if type(value) != auto else self.make_default("AdvncdInvstr")

	@AdvncdInvstr.deleter
	def AdvncdInvstr(self):
		del self._AdvncdInvstr
		self._AdvncdInvstr = None

	@property
	def BsicInvstr(self):
		return self._BsicInvstr

	@BsicInvstr.setter
	def BsicInvstr(self, value):
		self._BsicInvstr = value if type(value) != auto else self.make_default("BsicInvstr")

	@BsicInvstr.deleter
	def BsicInvstr(self):
		del self._BsicInvstr
		self._BsicInvstr = None

	@property
	def ExprtInvstrDE(self):
		return self._ExprtInvstrDE

	@ExprtInvstrDE.setter
	def ExprtInvstrDE(self, value):
		self._ExprtInvstrDE = value if type(value) != auto else self.make_default("ExprtInvstrDE")

	@ExprtInvstrDE.deleter
	def ExprtInvstrDE(self):
		del self._ExprtInvstrDE
		self._ExprtInvstrDE = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfrmdInvstr', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketInvestorKnowledge1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdvncdInvstr', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsicInvstr', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExprtInvstrDE', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
	))

