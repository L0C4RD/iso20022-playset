# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OtherTargetMarketInvestorKnowledge1
from . import TargetMarket1Code

class InvestorKnowledge1(base_types._BaseFieldType):

	__slots__ = ["_AdvncdInvstr", "_BsicInvstr", "_ExprtInvstrDE", "_InfrmdInvstr", "_Othr"]
	@property
	def AdvncdInvstr(self):
		return self._AdvncdInvstr

	@AdvncdInvstr.setter
	def AdvncdInvstr(self, value):
		self._AdvncdInvstr = value if value is not None else base_types.UninitialisedField(self, 'AdvncdInvstr', TargetMarket1Code, False)

	@AdvncdInvstr.deleter
	def AdvncdInvstr(self):
		del self._AdvncdInvstr
		self._AdvncdInvstr = base_types.UninitialisedField(self, 'AdvncdInvstr', TargetMarket1Code, False)

	@property
	def BsicInvstr(self):
		return self._BsicInvstr

	@BsicInvstr.setter
	def BsicInvstr(self, value):
		self._BsicInvstr = value if value is not None else base_types.UninitialisedField(self, 'BsicInvstr', TargetMarket1Code, False)

	@BsicInvstr.deleter
	def BsicInvstr(self):
		del self._BsicInvstr
		self._BsicInvstr = base_types.UninitialisedField(self, 'BsicInvstr', TargetMarket1Code, False)

	@property
	def ExprtInvstrDE(self):
		return self._ExprtInvstrDE

	@ExprtInvstrDE.setter
	def ExprtInvstrDE(self, value):
		self._ExprtInvstrDE = value if value is not None else base_types.UninitialisedField(self, 'ExprtInvstrDE', TargetMarket1Code, False)

	@ExprtInvstrDE.deleter
	def ExprtInvstrDE(self):
		del self._ExprtInvstrDE
		self._ExprtInvstrDE = base_types.UninitialisedField(self, 'ExprtInvstrDE', TargetMarket1Code, False)

	@property
	def InfrmdInvstr(self):
		return self._InfrmdInvstr

	@InfrmdInvstr.setter
	def InfrmdInvstr(self, value):
		self._InfrmdInvstr = value if value is not None else base_types.UninitialisedField(self, 'InfrmdInvstr', TargetMarket1Code, False)

	@InfrmdInvstr.deleter
	def InfrmdInvstr(self):
		del self._InfrmdInvstr
		self._InfrmdInvstr = base_types.UninitialisedField(self, 'InfrmdInvstr', TargetMarket1Code, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherTargetMarketInvestorKnowledge1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherTargetMarketInvestorKnowledge1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdvncdInvstr', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsicInvstr', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExprtInvstrDE', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfrmdInvstr', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketInvestorKnowledge1, min=0, max=None, mutex_group=None, array=True),
	))