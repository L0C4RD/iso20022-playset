# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference10
from . import AdditionalReference11
from . import MarketPracticeVersion1
from . import Max35Text
from . import MessageIdentification1
from . import TransferReference14

class PortfolioTransferCancellationRequestV09(base_types._BaseFieldType):

	__slots__ = ["_MktPrctcVrsn", "_MsgRef", "_MstrRef", "_PoolRef", "_PrvsRef", "_RltdRef", "_TrfRefs"]
	@property
	def MktPrctcVrsn(self):
		return self._MktPrctcVrsn

	@MktPrctcVrsn.setter
	def MktPrctcVrsn(self, value):
		self._MktPrctcVrsn = value if value is not None else base_types.UninitialisedField(self, 'MktPrctcVrsn', MarketPracticeVersion1, False)

	@MktPrctcVrsn.deleter
	def MktPrctcVrsn(self):
		del self._MktPrctcVrsn
		self._MktPrctcVrsn = base_types.UninitialisedField(self, 'MktPrctcVrsn', MarketPracticeVersion1, False)

	@property
	def MsgRef(self):
		return self._MsgRef

	@MsgRef.setter
	def MsgRef(self, value):
		self._MsgRef = value if value is not None else base_types.UninitialisedField(self, 'MsgRef', MessageIdentification1, False)

	@MsgRef.deleter
	def MsgRef(self):
		del self._MsgRef
		self._MsgRef = base_types.UninitialisedField(self, 'MsgRef', MessageIdentification1, False)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if value is not None else base_types.UninitialisedField(self, 'PoolRef', AdditionalReference11, False)

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = base_types.UninitialisedField(self, 'PoolRef', AdditionalReference11, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, False)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference10, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference10, False)

	@property
	def TrfRefs(self):
		return self._TrfRefs

	@TrfRefs.setter
	def TrfRefs(self, value):
		self._TrfRefs = value if value is not None else base_types.UninitialisedField(self, 'TrfRefs', TransferReference14, False)

	@TrfRefs.deleter
	def TrfRefs(self):
		del self._TrfRefs
		self._TrfRefs = base_types.UninitialisedField(self, 'TrfRefs', TransferReference14, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRefs', type=TransferReference14, min=1, max=1, mutex_group=None, array=False),
	))