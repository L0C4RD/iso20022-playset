# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import InvestorKnowledge1
from . import InvestorRequirements4
from . import InvestorType2
from . import LossBearing2
from . import OtherTargetMarket1
from . import RiskTolerance1

class TargetMarket4(base_types._BaseFieldType):

	__slots__ = ["_AbltyToBearLosses", "_ClntObjctvsAndNeeds", "_InvstrTp", "_KnwldgAndOrExprnc", "_Othr", "_RefDt", "_RskTlrnce"]
	@property
	def AbltyToBearLosses(self):
		return self._AbltyToBearLosses

	@AbltyToBearLosses.setter
	def AbltyToBearLosses(self, value):
		self._AbltyToBearLosses = value if value is not None else base_types.UninitialisedField(self, 'AbltyToBearLosses', LossBearing2, False)

	@AbltyToBearLosses.deleter
	def AbltyToBearLosses(self):
		del self._AbltyToBearLosses
		self._AbltyToBearLosses = base_types.UninitialisedField(self, 'AbltyToBearLosses', LossBearing2, False)

	@property
	def ClntObjctvsAndNeeds(self):
		return self._ClntObjctvsAndNeeds

	@ClntObjctvsAndNeeds.setter
	def ClntObjctvsAndNeeds(self, value):
		self._ClntObjctvsAndNeeds = value if value is not None else base_types.UninitialisedField(self, 'ClntObjctvsAndNeeds', InvestorRequirements4, False)

	@ClntObjctvsAndNeeds.deleter
	def ClntObjctvsAndNeeds(self):
		del self._ClntObjctvsAndNeeds
		self._ClntObjctvsAndNeeds = base_types.UninitialisedField(self, 'ClntObjctvsAndNeeds', InvestorRequirements4, False)

	@property
	def InvstrTp(self):
		return self._InvstrTp

	@InvstrTp.setter
	def InvstrTp(self, value):
		self._InvstrTp = value if value is not None else base_types.UninitialisedField(self, 'InvstrTp', InvestorType2, False)

	@InvstrTp.deleter
	def InvstrTp(self):
		del self._InvstrTp
		self._InvstrTp = base_types.UninitialisedField(self, 'InvstrTp', InvestorType2, False)

	@property
	def KnwldgAndOrExprnc(self):
		return self._KnwldgAndOrExprnc

	@KnwldgAndOrExprnc.setter
	def KnwldgAndOrExprnc(self, value):
		self._KnwldgAndOrExprnc = value if value is not None else base_types.UninitialisedField(self, 'KnwldgAndOrExprnc', InvestorKnowledge1, False)

	@KnwldgAndOrExprnc.deleter
	def KnwldgAndOrExprnc(self):
		del self._KnwldgAndOrExprnc
		self._KnwldgAndOrExprnc = base_types.UninitialisedField(self, 'KnwldgAndOrExprnc', InvestorKnowledge1, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherTargetMarket1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherTargetMarket1, True)

	@property
	def RefDt(self):
		return self._RefDt

	@RefDt.setter
	def RefDt(self, value):
		self._RefDt = value if value is not None else base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@RefDt.deleter
	def RefDt(self):
		del self._RefDt
		self._RefDt = base_types.UninitialisedField(self, 'RefDt', ISODate, False)

	@property
	def RskTlrnce(self):
		return self._RskTlrnce

	@RskTlrnce.setter
	def RskTlrnce(self, value):
		self._RskTlrnce = value if value is not None else base_types.UninitialisedField(self, 'RskTlrnce', RiskTolerance1, False)

	@RskTlrnce.deleter
	def RskTlrnce(self):
		del self._RskTlrnce
		self._RskTlrnce = base_types.UninitialisedField(self, 'RskTlrnce', RiskTolerance1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AbltyToBearLosses', type=LossBearing2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntObjctvsAndNeeds', type=InvestorRequirements4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrTp', type=InvestorType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KnwldgAndOrExprnc', type=InvestorKnowledge1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherTargetMarket1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RskTlrnce', type=RiskTolerance1, min=0, max=1, mutex_group=None, array=False),
	))