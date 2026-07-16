# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OtherTargetMarketLossBearing1
from . import PercentageRate
from . import TargetMarket1Code

class LossBearing2(base_types._BaseFieldType):

	__slots__ = ["_LossByndCptl", "_LtdCptlLoss", "_LtdCptlLossLvl", "_NoCptlGrnt", "_NoCptlLoss", "_Othr"]
	@property
	def LossByndCptl(self):
		return self._LossByndCptl

	@LossByndCptl.setter
	def LossByndCptl(self, value):
		self._LossByndCptl = value if value is not None else base_types.UninitialisedField(self, 'LossByndCptl', TargetMarket1Code, False)

	@LossByndCptl.deleter
	def LossByndCptl(self):
		del self._LossByndCptl
		self._LossByndCptl = base_types.UninitialisedField(self, 'LossByndCptl', TargetMarket1Code, False)

	@property
	def LtdCptlLoss(self):
		return self._LtdCptlLoss

	@LtdCptlLoss.setter
	def LtdCptlLoss(self, value):
		self._LtdCptlLoss = value if value is not None else base_types.UninitialisedField(self, 'LtdCptlLoss', TargetMarket1Code, False)

	@LtdCptlLoss.deleter
	def LtdCptlLoss(self):
		del self._LtdCptlLoss
		self._LtdCptlLoss = base_types.UninitialisedField(self, 'LtdCptlLoss', TargetMarket1Code, False)

	@property
	def LtdCptlLossLvl(self):
		return self._LtdCptlLossLvl

	@LtdCptlLossLvl.setter
	def LtdCptlLossLvl(self, value):
		self._LtdCptlLossLvl = value if value is not None else base_types.UninitialisedField(self, 'LtdCptlLossLvl', PercentageRate, False)

	@LtdCptlLossLvl.deleter
	def LtdCptlLossLvl(self):
		del self._LtdCptlLossLvl
		self._LtdCptlLossLvl = base_types.UninitialisedField(self, 'LtdCptlLossLvl', PercentageRate, False)

	@property
	def NoCptlGrnt(self):
		return self._NoCptlGrnt

	@NoCptlGrnt.setter
	def NoCptlGrnt(self, value):
		self._NoCptlGrnt = value if value is not None else base_types.UninitialisedField(self, 'NoCptlGrnt', TargetMarket1Code, False)

	@NoCptlGrnt.deleter
	def NoCptlGrnt(self):
		del self._NoCptlGrnt
		self._NoCptlGrnt = base_types.UninitialisedField(self, 'NoCptlGrnt', TargetMarket1Code, False)

	@property
	def NoCptlLoss(self):
		return self._NoCptlLoss

	@NoCptlLoss.setter
	def NoCptlLoss(self, value):
		self._NoCptlLoss = value if value is not None else base_types.UninitialisedField(self, 'NoCptlLoss', TargetMarket1Code, False)

	@NoCptlLoss.deleter
	def NoCptlLoss(self):
		del self._NoCptlLoss
		self._NoCptlLoss = base_types.UninitialisedField(self, 'NoCptlLoss', TargetMarket1Code, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherTargetMarketLossBearing1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherTargetMarketLossBearing1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LossByndCptl', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdCptlLoss', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdCptlLossLvl', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoCptlGrnt', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoCptlLoss', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketLossBearing1, min=0, max=None, mutex_group=None, array=True),
	))