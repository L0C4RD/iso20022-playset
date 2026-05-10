from . import base_types
from .RiskTolerance1 import RiskTolerance1
from .InvestorKnowledge1 import InvestorKnowledge1
from .ISODate import ISODate
from .InvestorRequirements4 import InvestorRequirements4
from .InvestorType2 import InvestorType2
from .LossBearing2 import LossBearing2
from .OtherTargetMarket1 import OtherTargetMarket1

class TargetMarket4(base_types._BaseFieldType):

	__slots__ = ["_KnwldgAndOrExprnc", "_RskTlrnce", "_RefDt", "_Othr", "_InvstrTp", "_AbltyToBearLosses", "_ClntObjctvsAndNeeds"]
	@property
	def KnwldgAndOrExprnc(self):
		return self._KnwldgAndOrExprnc

	@KnwldgAndOrExprnc.setter
	def KnwldgAndOrExprnc(self, value):
		self._KnwldgAndOrExprnc = value if type(value) != auto else self.make_default("KnwldgAndOrExprnc")

	@KnwldgAndOrExprnc.deleter
	def KnwldgAndOrExprnc(self):
		del self._KnwldgAndOrExprnc
		self._KnwldgAndOrExprnc = None

	@property
	def RskTlrnce(self):
		return self._RskTlrnce

	@RskTlrnce.setter
	def RskTlrnce(self, value):
		self._RskTlrnce = value if type(value) != auto else self.make_default("RskTlrnce")

	@RskTlrnce.deleter
	def RskTlrnce(self):
		del self._RskTlrnce
		self._RskTlrnce = None

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if type(value) != auto else self.make_default("RefDt")

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = None

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
	def InvstrTp(self):
		return self._InvstrTp

	@InvstrTp.setter
	def InvstrTp(self, value):
		self._InvstrTp = value if type(value) != auto else self.make_default("InvstrTp")

	@InvstrTp.deleter
	def InvstrTp(self):
		del self._InvstrTp
		self._InvstrTp = None

	@property
	def AbltyToBearLosses(self):
		return self._AbltyToBearLosses

	@AbltyToBearLosses.setter
	def AbltyToBearLosses(self, value):
		self._AbltyToBearLosses = value if type(value) != auto else self.make_default("AbltyToBearLosses")

	@AbltyToBearLosses.deleter
	def AbltyToBearLosses(self):
		del self._AbltyToBearLosses
		self._AbltyToBearLosses = None

	@property
	def ClntObjctvsAndNeeds(self):
		return self._ClntObjctvsAndNeeds

	@ClntObjctvsAndNeeds.setter
	def ClntObjctvsAndNeeds(self, value):
		self._ClntObjctvsAndNeeds = value if type(value) != auto else self.make_default("ClntObjctvsAndNeeds")

	@ClntObjctvsAndNeeds.deleter
	def ClntObjctvsAndNeeds(self):
		del self._ClntObjctvsAndNeeds
		self._ClntObjctvsAndNeeds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='KnwldgAndOrExprnc', type=InvestorKnowledge1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnce', type=RiskTolerance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarket1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstrTp', type=InvestorType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AbltyToBearLosses', type=LossBearing2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntObjctvsAndNeeds', type=InvestorRequirements4, min=0, max=1, mutex_group=None, array=False),
	))

