# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd24Amount
from . import GenericIdentification168
from . import MICIdentifier
from . import MarginRatePortfolio1
from . import NonNegativeNumber
from . import OpenInterest1
from . import Product1Choice

class ClearedProduct3(base_types._BaseFieldType):

	__slots__ = ["_CCPPdctId", "_ClrdGrssNtnlAmt", "_MrgnRatePrtfl", "_OpnIntrst", "_Pdct", "_TradgVn", "_TrdsClrd", "_UvrslPdctId"]
	@property
	def CCPPdctId(self):
		return self._CCPPdctId

	@CCPPdctId.setter
	def CCPPdctId(self, value):
		self._CCPPdctId = value if value is not None else base_types.UninitialisedField(self, 'CCPPdctId', GenericIdentification168, False)

	@CCPPdctId.deleter
	def CCPPdctId(self):
		del self._CCPPdctId
		self._CCPPdctId = base_types.UninitialisedField(self, 'CCPPdctId', GenericIdentification168, False)

	@property
	def ClrdGrssNtnlAmt(self):
		return self._ClrdGrssNtnlAmt

	@ClrdGrssNtnlAmt.setter
	def ClrdGrssNtnlAmt(self, value):
		self._ClrdGrssNtnlAmt = value if value is not None else base_types.UninitialisedField(self, 'ClrdGrssNtnlAmt', ActiveCurrencyAnd24Amount, False)

	@ClrdGrssNtnlAmt.deleter
	def ClrdGrssNtnlAmt(self):
		del self._ClrdGrssNtnlAmt
		self._ClrdGrssNtnlAmt = base_types.UninitialisedField(self, 'ClrdGrssNtnlAmt', ActiveCurrencyAnd24Amount, False)

	@property
	def MrgnRatePrtfl(self):
		return self._MrgnRatePrtfl

	@MrgnRatePrtfl.setter
	def MrgnRatePrtfl(self, value):
		self._MrgnRatePrtfl = value if value is not None else base_types.UninitialisedField(self, 'MrgnRatePrtfl', MarginRatePortfolio1, False)

	@MrgnRatePrtfl.deleter
	def MrgnRatePrtfl(self):
		del self._MrgnRatePrtfl
		self._MrgnRatePrtfl = base_types.UninitialisedField(self, 'MrgnRatePrtfl', MarginRatePortfolio1, False)

	@property
	def OpnIntrst(self):
		return self._OpnIntrst

	@OpnIntrst.setter
	def OpnIntrst(self, value):
		self._OpnIntrst = value if value is not None else base_types.UninitialisedField(self, 'OpnIntrst', OpenInterest1, False)

	@OpnIntrst.deleter
	def OpnIntrst(self):
		del self._OpnIntrst
		self._OpnIntrst = base_types.UninitialisedField(self, 'OpnIntrst', OpenInterest1, False)

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if value is not None else base_types.UninitialisedField(self, 'Pdct', Product1Choice, False)

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = base_types.UninitialisedField(self, 'Pdct', Product1Choice, False)

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if value is not None else base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, True)

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = base_types.UninitialisedField(self, 'TradgVn', MICIdentifier, True)

	@property
	def TrdsClrd(self):
		return self._TrdsClrd

	@TrdsClrd.setter
	def TrdsClrd(self, value):
		self._TrdsClrd = value if value is not None else base_types.UninitialisedField(self, 'TrdsClrd', NonNegativeNumber, False)

	@TrdsClrd.deleter
	def TrdsClrd(self):
		del self._TrdsClrd
		self._TrdsClrd = base_types.UninitialisedField(self, 'TrdsClrd', NonNegativeNumber, False)

	@property
	def UvrslPdctId(self):
		return self._UvrslPdctId

	@UvrslPdctId.setter
	def UvrslPdctId(self, value):
		self._UvrslPdctId = value if value is not None else base_types.UninitialisedField(self, 'UvrslPdctId', GenericIdentification168, False)

	@UvrslPdctId.deleter
	def UvrslPdctId(self):
		del self._UvrslPdctId
		self._UvrslPdctId = base_types.UninitialisedField(self, 'UvrslPdctId', GenericIdentification168, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CCPPdctId', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrdGrssNtnlAmt', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnRatePrtfl', type=MarginRatePortfolio1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnIntrst', type=OpenInterest1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdct', type=Product1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrdsClrd', type=NonNegativeNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UvrslPdctId', type=GenericIdentification168, min=0, max=1, mutex_group=None, array=False),
	))