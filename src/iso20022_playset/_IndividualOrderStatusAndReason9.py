# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ExpectedExecutionDetails5 import ExpectedExecutionDetails5
from ._Fee12 import Fee12
from ._FundOrderData7 import FundOrderData7
from ._HoldBackInformation4 import HoldBackInformation4
from ._Max35Text import Max35Text
from ._OrderStatus6Choice import OrderStatus6Choice
from ._PartyIdentification139 import PartyIdentification139

class IndividualOrderStatusAndReason9(base_types._BaseFieldType):

	__slots__ = ["_ClntRef", "_CxlRef", "_DealRef", "_GtgOrHldBckDtls", "_MstrRef", "_NewDtls", "_NonceId", "_OrdrData", "_OrdrRef", "_OrdrSts", "_RprdFee", "_StsInitr"]
	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if type(value) != base_types.auto else self.make_default("CxlRef")

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = None

	@property
	def DealRef(self):
		return self._DealRef

	@DealRef.setter
	def DealRef(self, value):
		self._DealRef = value if type(value) != base_types.auto else self.make_default("DealRef")

	@DealRef.deleter
	def DealRef(self):
		del self._DealRef
		self._DealRef = None

	@property
	def GtgOrHldBckDtls(self):
		return self._GtgOrHldBckDtls

	@GtgOrHldBckDtls.setter
	def GtgOrHldBckDtls(self, value):
		self._GtgOrHldBckDtls = value if type(value) != base_types.auto else self.make_default("GtgOrHldBckDtls")

	@GtgOrHldBckDtls.deleter
	def GtgOrHldBckDtls(self):
		del self._GtgOrHldBckDtls
		self._GtgOrHldBckDtls = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def NewDtls(self):
		return self._NewDtls

	@NewDtls.setter
	def NewDtls(self, value):
		self._NewDtls = value if type(value) != base_types.auto else self.make_default("NewDtls")

	@NewDtls.deleter
	def NewDtls(self):
		del self._NewDtls
		self._NewDtls = None

	@property
	def NonceId(self):
		return self._NonceId

	@NonceId.setter
	def NonceId(self, value):
		self._NonceId = value if type(value) != base_types.auto else self.make_default("NonceId")

	@NonceId.deleter
	def NonceId(self):
		del self._NonceId
		self._NonceId = None

	@property
	def OrdrData(self):
		return self._OrdrData

	@OrdrData.setter
	def OrdrData(self, value):
		self._OrdrData = value if type(value) != base_types.auto else self.make_default("OrdrData")

	@OrdrData.deleter
	def OrdrData(self):
		del self._OrdrData
		self._OrdrData = None

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != base_types.auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def OrdrSts(self):
		return self._OrdrSts

	@OrdrSts.setter
	def OrdrSts(self, value):
		self._OrdrSts = value if type(value) != base_types.auto else self.make_default("OrdrSts")

	@OrdrSts.deleter
	def OrdrSts(self):
		del self._OrdrSts
		self._OrdrSts = None

	@property
	def RprdFee(self):
		return self._RprdFee

	@RprdFee.setter
	def RprdFee(self, value):
		self._RprdFee = value if type(value) != base_types.auto else self.make_default("RprdFee")

	@RprdFee.deleter
	def RprdFee(self):
		del self._RprdFee
		self._RprdFee = None

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if type(value) != base_types.auto else self.make_default("StsInitr")

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GtgOrHldBckDtls', type=HoldBackInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDtls', type=ExpectedExecutionDetails5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrData', type=FundOrderData7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrSts', type=OrderStatus6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdFee', type=Fee12, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
	))