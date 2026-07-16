# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import Max35Text
from . import TargetMarket1Choice

class OtherTargetMarketInvestorKnowledge1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_InvstrKnwldgTp", "_Trgt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@property
	def InvstrKnwldgTp(self):
		return self._InvstrKnwldgTp

	@InvstrKnwldgTp.setter
	def InvstrKnwldgTp(self, value):
		self._InvstrKnwldgTp = value if value is not None else base_types.UninitialisedField(self, 'InvstrKnwldgTp', Max35Text, False)

	@InvstrKnwldgTp.deleter
	def InvstrKnwldgTp(self):
		del self._InvstrKnwldgTp
		self._InvstrKnwldgTp = base_types.UninitialisedField(self, 'InvstrKnwldgTp', Max35Text, False)

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if value is not None else base_types.UninitialisedField(self, 'Trgt', TargetMarket1Choice, False)

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = base_types.UninitialisedField(self, 'Trgt', TargetMarket1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrKnwldgTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=TargetMarket1Choice, min=0, max=1, mutex_group=None, array=False),
	))