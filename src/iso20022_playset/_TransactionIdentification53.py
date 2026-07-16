# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact12Text
from . import Exact15Text
from . import Exact2NumericText
from . import ISODateTime
from . import LifeCycleSupport1Code
from . import Max1000Text
from . import Max12NumericText
from . import Max140Text
from . import Max23NumericText
from . import Max35Text
from . import Max70Text
from . import Max99Text
from . import PurchaseIdentifierType2Code

class TransactionIdentification53(base_types._BaseFieldType):

	__slots__ = ["_AcqrrRefData", "_AcqrrRefNb", "_AssoctdDataRef", "_AuthntcnTkn", "_AuthstnSeqNb", "_IssrRefData", "_LifeCyclId", "_LifeCyclSpprt", "_OthrPurchsIdrTp", "_PresntmntSeqCnt", "_PresntmntSeqNb", "_PurchsIdr", "_PurchsIdrTp", "_RtrvlRefNb", "_SysTracAudtNb", "_TrnsmssnDtTm"]
	@property
	def AcqrrRefData(self):
		return self._AcqrrRefData

	@AcqrrRefData.setter
	def AcqrrRefData(self, value):
		self._AcqrrRefData = value if value is not None else base_types.UninitialisedField(self, 'AcqrrRefData', Max140Text, False)

	@AcqrrRefData.deleter
	def AcqrrRefData(self):
		del self._AcqrrRefData
		self._AcqrrRefData = base_types.UninitialisedField(self, 'AcqrrRefData', Max140Text, False)

	@property
	def AcqrrRefNb(self):
		return self._AcqrrRefNb

	@AcqrrRefNb.setter
	def AcqrrRefNb(self, value):
		self._AcqrrRefNb = value if value is not None else base_types.UninitialisedField(self, 'AcqrrRefNb', Max23NumericText, False)

	@AcqrrRefNb.deleter
	def AcqrrRefNb(self):
		del self._AcqrrRefNb
		self._AcqrrRefNb = base_types.UninitialisedField(self, 'AcqrrRefNb', Max23NumericText, False)

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
	def AuthntcnTkn(self):
		return self._AuthntcnTkn

	@AuthntcnTkn.setter
	def AuthntcnTkn(self, value):
		self._AuthntcnTkn = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnTkn', Max35Text, False)

	@AuthntcnTkn.deleter
	def AuthntcnTkn(self):
		del self._AuthntcnTkn
		self._AuthntcnTkn = base_types.UninitialisedField(self, 'AuthntcnTkn', Max35Text, False)

	@property
	def AuthstnSeqNb(self):
		return self._AuthstnSeqNb

	@AuthstnSeqNb.setter
	def AuthstnSeqNb(self, value):
		self._AuthstnSeqNb = value if value is not None else base_types.UninitialisedField(self, 'AuthstnSeqNb', Exact2NumericText, False)

	@AuthstnSeqNb.deleter
	def AuthstnSeqNb(self):
		del self._AuthstnSeqNb
		self._AuthstnSeqNb = base_types.UninitialisedField(self, 'AuthstnSeqNb', Exact2NumericText, False)

	@property
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if value is not None else base_types.UninitialisedField(self, 'IssrRefData', Max1000Text, False)

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = base_types.UninitialisedField(self, 'IssrRefData', Max1000Text, False)

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
	def LifeCyclSpprt(self):
		return self._LifeCyclSpprt

	@LifeCyclSpprt.setter
	def LifeCyclSpprt(self, value):
		self._LifeCyclSpprt = value if value is not None else base_types.UninitialisedField(self, 'LifeCyclSpprt', LifeCycleSupport1Code, False)

	@LifeCyclSpprt.deleter
	def LifeCyclSpprt(self):
		del self._LifeCyclSpprt
		self._LifeCyclSpprt = base_types.UninitialisedField(self, 'LifeCyclSpprt', LifeCycleSupport1Code, False)

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
	def PresntmntSeqCnt(self):
		return self._PresntmntSeqCnt

	@PresntmntSeqCnt.setter
	def PresntmntSeqCnt(self, value):
		self._PresntmntSeqCnt = value if value is not None else base_types.UninitialisedField(self, 'PresntmntSeqCnt', Exact2NumericText, False)

	@PresntmntSeqCnt.deleter
	def PresntmntSeqCnt(self):
		del self._PresntmntSeqCnt
		self._PresntmntSeqCnt = base_types.UninitialisedField(self, 'PresntmntSeqCnt', Exact2NumericText, False)

	@property
	def PresntmntSeqNb(self):
		return self._PresntmntSeqNb

	@PresntmntSeqNb.setter
	def PresntmntSeqNb(self, value):
		self._PresntmntSeqNb = value if value is not None else base_types.UninitialisedField(self, 'PresntmntSeqNb', Exact2NumericText, False)

	@PresntmntSeqNb.deleter
	def PresntmntSeqNb(self):
		del self._PresntmntSeqNb
		self._PresntmntSeqNb = base_types.UninitialisedField(self, 'PresntmntSeqNb', Exact2NumericText, False)

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
		base_types.FieldEntry(name='AcqrrRefData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrRefNb', type=Max23NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDataRef', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnTkn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnSeqNb', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrRefData', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclSpprt', type=LifeCycleSupport1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPurchsIdrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntmntSeqCnt', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntmntSeqNb', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsIdr', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsIdrTp', type=PurchaseIdentifierType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))