# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact12Text
from . import Exact15Text
from . import ISODateTime
from . import Max12NumericText
from . import Max35Text
from . import Max70Text
from . import Max99Text
from . import PurchaseIdentifierType2Code
from . import TrueFalseIndicator

class TransactionIdentification56(base_types._BaseFieldType):

	__slots__ = ["_AssoctdData", "_AssoctdDataDstn", "_AssoctdDataRef", "_LifeCyclId", "_OthrPurchsIdrTp", "_PurchsIdr", "_PurchsIdrTp", "_RtrvlRefNb", "_SysTracAudtNb", "_TrnsmssnDtTm"]
	@property
	def AssoctdData(self):
		return self._AssoctdData

	@AssoctdData.setter
	def AssoctdData(self, value):
		self._AssoctdData = value if value is not None else base_types.UninitialisedField(self, 'AssoctdData', TrueFalseIndicator, False)

	@AssoctdData.deleter
	def AssoctdData(self):
		del self._AssoctdData
		self._AssoctdData = base_types.UninitialisedField(self, 'AssoctdData', TrueFalseIndicator, False)

	@property
	def AssoctdDataDstn(self):
		return self._AssoctdDataDstn

	@AssoctdDataDstn.setter
	def AssoctdDataDstn(self, value):
		self._AssoctdDataDstn = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDataDstn', Max35Text, False)

	@AssoctdDataDstn.deleter
	def AssoctdDataDstn(self):
		del self._AssoctdDataDstn
		self._AssoctdDataDstn = base_types.UninitialisedField(self, 'AssoctdDataDstn', Max35Text, False)

	@property
	def AssoctdDataRef(self):
		return self._AssoctdDataRef

	@AssoctdDataRef.setter
	def AssoctdDataRef(self, value):
		self._AssoctdDataRef = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDataRef', Max70Text, False)

	@AssoctdDataRef.deleter
	def AssoctdDataRef(self):
		del self._AssoctdDataRef
		self._AssoctdDataRef = base_types.UninitialisedField(self, 'AssoctdDataRef', Max70Text, False)

	@property
	def LifeCyclId(self):
		return self._LifeCyclId

	@LifeCyclId.setter
	def LifeCyclId(self, value):
		self._LifeCyclId = value if value is not None else base_types.UninitialisedField(self, 'LifeCyclId', Exact15Text, False)

	@LifeCyclId.deleter
	def LifeCyclId(self):
		del self._LifeCyclId
		self._LifeCyclId = base_types.UninitialisedField(self, 'LifeCyclId', Exact15Text, False)

	@property
	def OthrPurchsIdrTp(self):
		return self._OthrPurchsIdrTp

	@OthrPurchsIdrTp.setter
	def OthrPurchsIdrTp(self, value):
		self._OthrPurchsIdrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrPurchsIdrTp', Max35Text, False)

	@OthrPurchsIdrTp.deleter
	def OthrPurchsIdrTp(self):
		del self._OthrPurchsIdrTp
		self._OthrPurchsIdrTp = base_types.UninitialisedField(self, 'OthrPurchsIdrTp', Max35Text, False)

	@property
	def PurchsIdr(self):
		return self._PurchsIdr

	@PurchsIdr.setter
	def PurchsIdr(self, value):
		self._PurchsIdr = value if value is not None else base_types.UninitialisedField(self, 'PurchsIdr', Max99Text, False)

	@PurchsIdr.deleter
	def PurchsIdr(self):
		del self._PurchsIdr
		self._PurchsIdr = base_types.UninitialisedField(self, 'PurchsIdr', Max99Text, False)

	@property
	def PurchsIdrTp(self):
		return self._PurchsIdrTp

	@PurchsIdrTp.setter
	def PurchsIdrTp(self, value):
		self._PurchsIdrTp = value if value is not None else base_types.UninitialisedField(self, 'PurchsIdrTp', PurchaseIdentifierType2Code, False)

	@PurchsIdrTp.deleter
	def PurchsIdrTp(self):
		del self._PurchsIdrTp
		self._PurchsIdrTp = base_types.UninitialisedField(self, 'PurchsIdrTp', PurchaseIdentifierType2Code, False)

	@property
	def RtrvlRefNb(self):
		return self._RtrvlRefNb

	@RtrvlRefNb.setter
	def RtrvlRefNb(self, value):
		self._RtrvlRefNb = value if value is not None else base_types.UninitialisedField(self, 'RtrvlRefNb', Exact12Text, False)

	@RtrvlRefNb.deleter
	def RtrvlRefNb(self):
		del self._RtrvlRefNb
		self._RtrvlRefNb = base_types.UninitialisedField(self, 'RtrvlRefNb', Exact12Text, False)

	@property
	def SysTracAudtNb(self):
		return self._SysTracAudtNb

	@SysTracAudtNb.setter
	def SysTracAudtNb(self, value):
		self._SysTracAudtNb = value if value is not None else base_types.UninitialisedField(self, 'SysTracAudtNb', Max12NumericText, False)

	@SysTracAudtNb.deleter
	def SysTracAudtNb(self):
		del self._SysTracAudtNb
		self._SysTracAudtNb = base_types.UninitialisedField(self, 'SysTracAudtNb', Max12NumericText, False)

	@property
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if value is not None else base_types.UninitialisedField(self, 'TrnsmssnDtTm', ISODateTime, False)

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = base_types.UninitialisedField(self, 'TrnsmssnDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssoctdData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDataDstn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDataRef', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPurchsIdrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsIdr', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsIdrTp', type=PurchaseIdentifierType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))