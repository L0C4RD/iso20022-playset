import base_types
import PercentageRate
import TargetMarket1Code
import OtherTargetMarketLossBearing1

class LossBearing2(base_types._BaseFieldType):

	__slots__ = ["_NoCptlLoss", "_NoCptlGrnt", "_LtdCptlLoss", "_LtdCptlLossLvl", "_Othr", "_LossByndCptl"]
	@property
	def NoCptlLoss(self):
		return self._NoCptlLoss

	@NoCptlLoss.setter
	def NoCptlLoss(self, value):
		self._NoCptlLoss = value if type(value) != auto else self.make_default("NoCptlLoss")

	@NoCptlLoss.deleter
	def NoCptlLoss(self):
		del self._NoCptlLoss
		self._NoCptlLoss = None

	@property
	def NoCptlGrnt(self):
		return self._NoCptlGrnt

	@NoCptlGrnt.setter
	def NoCptlGrnt(self, value):
		self._NoCptlGrnt = value if type(value) != auto else self.make_default("NoCptlGrnt")

	@NoCptlGrnt.deleter
	def NoCptlGrnt(self):
		del self._NoCptlGrnt
		self._NoCptlGrnt = None

	@property
	def LtdCptlLoss(self):
		return self._LtdCptlLoss

	@LtdCptlLoss.setter
	def LtdCptlLoss(self, value):
		self._LtdCptlLoss = value if type(value) != auto else self.make_default("LtdCptlLoss")

	@LtdCptlLoss.deleter
	def LtdCptlLoss(self):
		del self._LtdCptlLoss
		self._LtdCptlLoss = None

	@property
	def LtdCptlLossLvl(self):
		return self._LtdCptlLossLvl

	@LtdCptlLossLvl.setter
	def LtdCptlLossLvl(self, value):
		self._LtdCptlLossLvl = value if type(value) != auto else self.make_default("LtdCptlLossLvl")

	@LtdCptlLossLvl.deleter
	def LtdCptlLossLvl(self):
		del self._LtdCptlLossLvl
		self._LtdCptlLossLvl = None

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
	def LossByndCptl(self):
		return self._LossByndCptl

	@LossByndCptl.setter
	def LossByndCptl(self, value):
		self._LossByndCptl = value if type(value) != auto else self.make_default("LossByndCptl")

	@LossByndCptl.deleter
	def LossByndCptl(self):
		del self._LossByndCptl
		self._LossByndCptl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoCptlLoss', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoCptlGrnt', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdCptlLoss', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtdCptlLossLvl', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarketLossBearing1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LossByndCptl', type=TargetMarket1Code, min=0, max=1, mutex_group=None, array=False),
	))

