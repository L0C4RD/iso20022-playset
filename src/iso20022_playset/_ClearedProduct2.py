# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._GenericIdentification168 import GenericIdentification168
from ._MICIdentifier import MICIdentifier
from ._NonNegativeNumber import NonNegativeNumber
from ._OpenInterest1 import OpenInterest1
from ._Product1Choice import Product1Choice

class ClearedProduct2(base_types._BaseFieldType):

	__slots__ = ["_CCPPdctId", "_ClrdGrssNtnlAmt", "_OpnIntrst", "_Pdct", "_TradgVn", "_TrdsClrd", "_UvrslPdctId"]
	@property
	def CCPPdctId(self):
		return self._CCPPdctId

	@CCPPdctId.setter
	def CCPPdctId(self, value):
		self._CCPPdctId = value if type(value) != base_types.auto else self.make_default("CCPPdctId")

	@CCPPdctId.deleter
	def CCPPdctId(self):
		del self._CCPPdctId
		self._CCPPdctId = None

	@property
	def ClrdGrssNtnlAmt(self):
		return self._ClrdGrssNtnlAmt

	@ClrdGrssNtnlAmt.setter
	def ClrdGrssNtnlAmt(self, value):
		self._ClrdGrssNtnlAmt = value if type(value) != base_types.auto else self.make_default("ClrdGrssNtnlAmt")

	@ClrdGrssNtnlAmt.deleter
	def ClrdGrssNtnlAmt(self):
		del self._ClrdGrssNtnlAmt
		self._ClrdGrssNtnlAmt = None

	@property
	def OpnIntrst(self):
		return self._OpnIntrst

	@OpnIntrst.setter
	def OpnIntrst(self, value):
		self._OpnIntrst = value if type(value) != base_types.auto else self.make_default("OpnIntrst")

	@OpnIntrst.deleter
	def OpnIntrst(self):
		del self._OpnIntrst
		self._OpnIntrst = None

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if type(value) != base_types.auto else self.make_default("Pdct")

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = None

	@property
	def TradgVn(self):
		return self._TradgVn

	@TradgVn.setter
	def TradgVn(self, value):
		self._TradgVn = value if type(value) != base_types.auto else self.make_default("TradgVn")

	@TradgVn.deleter
	def TradgVn(self):
		del self._TradgVn
		self._TradgVn = None

	@property
	def TrdsClrd(self):
		return self._TrdsClrd

	@TrdsClrd.setter
	def TrdsClrd(self, value):
		self._TrdsClrd = value if type(value) != base_types.auto else self.make_default("TrdsClrd")

	@TrdsClrd.deleter
	def TrdsClrd(self):
		del self._TrdsClrd
		self._TrdsClrd = None

	@property
	def UvrslPdctId(self):
		return self._UvrslPdctId

	@UvrslPdctId.setter
	def UvrslPdctId(self, value):
		self._UvrslPdctId = value if type(value) != base_types.auto else self.make_default("UvrslPdctId")

	@UvrslPdctId.deleter
	def UvrslPdctId(self):
		del self._UvrslPdctId
		self._UvrslPdctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CCPPdctId', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrdGrssNtnlAmt', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpnIntrst', type=OpenInterest1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdct', type=Product1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgVn', type=MICIdentifier, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrdsClrd', type=NonNegativeNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UvrslPdctId', type=GenericIdentification168, min=0, max=1, mutex_group=None, array=False),
	))