# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExpectedExecutionDetails4
from . import Fee3
from . import FundOrderData5
from . import HoldBackInformation3
from . import Max35Text
from . import OrderStatus5Choice
from . import PartyIdentification113

class IndividualOrderStatusAndReason7(base_types._BaseFieldType):

	__slots__ = ["_ClntRef", "_CxlRef", "_DealRef", "_GtgOrHldBckDtls", "_MstrRef", "_NewDtls", "_OrdrData", "_OrdrRef", "_OrdrSts", "_RprdFee", "_StsInitr"]
	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', Max35Text, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', Max35Text, False)

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if value is not None else base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = base_types.UninitialisedField(self, 'CxlRef', Max35Text, False)

	@property
	def DealRef(self):
		return self._DealRef

	@DealRef.setter
	def DealRef(self, value):
		self._DealRef = value if value is not None else base_types.UninitialisedField(self, 'DealRef', Max35Text, False)

	@DealRef.deleter
	def DealRef(self):
		del self._DealRef
		self._DealRef = base_types.UninitialisedField(self, 'DealRef', Max35Text, False)

	@property
	def GtgOrHldBckDtls(self):
		return self._GtgOrHldBckDtls

	@GtgOrHldBckDtls.setter
	def GtgOrHldBckDtls(self, value):
		self._GtgOrHldBckDtls = value if value is not None else base_types.UninitialisedField(self, 'GtgOrHldBckDtls', HoldBackInformation3, False)

	@GtgOrHldBckDtls.deleter
	def GtgOrHldBckDtls(self):
		del self._GtgOrHldBckDtls
		self._GtgOrHldBckDtls = base_types.UninitialisedField(self, 'GtgOrHldBckDtls', HoldBackInformation3, False)

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
	def NewDtls(self):
		return self._NewDtls

	@NewDtls.setter
	def NewDtls(self, value):
		self._NewDtls = value if value is not None else base_types.UninitialisedField(self, 'NewDtls', ExpectedExecutionDetails4, False)

	@NewDtls.deleter
	def NewDtls(self):
		del self._NewDtls
		self._NewDtls = base_types.UninitialisedField(self, 'NewDtls', ExpectedExecutionDetails4, False)

	@property
	def OrdrData(self):
		return self._OrdrData

	@OrdrData.setter
	def OrdrData(self, value):
		self._OrdrData = value if value is not None else base_types.UninitialisedField(self, 'OrdrData', FundOrderData5, False)

	@OrdrData.deleter
	def OrdrData(self):
		del self._OrdrData
		self._OrdrData = base_types.UninitialisedField(self, 'OrdrData', FundOrderData5, False)

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if value is not None else base_types.UninitialisedField(self, 'OrdrRef', Max35Text, False)

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = base_types.UninitialisedField(self, 'OrdrRef', Max35Text, False)

	@property
	def OrdrSts(self):
		return self._OrdrSts

	@OrdrSts.setter
	def OrdrSts(self, value):
		self._OrdrSts = value if value is not None else base_types.UninitialisedField(self, 'OrdrSts', OrderStatus5Choice, False)

	@OrdrSts.deleter
	def OrdrSts(self):
		del self._OrdrSts
		self._OrdrSts = base_types.UninitialisedField(self, 'OrdrSts', OrderStatus5Choice, False)

	@property
	def RprdFee(self):
		return self._RprdFee

	@RprdFee.setter
	def RprdFee(self, value):
		self._RprdFee = value if value is not None else base_types.UninitialisedField(self, 'RprdFee', Fee3, True)

	@RprdFee.deleter
	def RprdFee(self):
		del self._RprdFee
		self._RprdFee = base_types.UninitialisedField(self, 'RprdFee', Fee3, True)

	@property
	def StsInitr(self):
		return self._StsInitr

	@StsInitr.setter
	def StsInitr(self, value):
		self._StsInitr = value if value is not None else base_types.UninitialisedField(self, 'StsInitr', PartyIdentification113, False)

	@StsInitr.deleter
	def StsInitr(self):
		del self._StsInitr
		self._StsInitr = base_types.UninitialisedField(self, 'StsInitr', PartyIdentification113, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GtgOrHldBckDtls', type=HoldBackInformation3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewDtls', type=ExpectedExecutionDetails4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrData', type=FundOrderData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrSts', type=OrderStatus5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdFee', type=Fee3, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsInitr', type=PartyIdentification113, min=0, max=1, mutex_group=None, array=False),
	))