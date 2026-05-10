from . import base_types
from .LifeCycleSupport1Code import LifeCycleSupport1Code
from .Max99Text import Max99Text
from .Max12NumericText import Max12NumericText
from .Max1000Text import Max1000Text
from .Max70Text import Max70Text
from .ISOTime import ISOTime
from .Exact12Text import Exact12Text
from .ISODate import ISODate
from .Exact15Text import Exact15Text
from .Max23NumericText import Max23NumericText
from .ISODateTime import ISODateTime
from .Max140Text import Max140Text
from .Exact2NumericText import Exact2NumericText
from .Max35Text import Max35Text
from .PurchaseIdentifierType2Code import PurchaseIdentifierType2Code
from .TrueFalseIndicator import TrueFalseIndicator

class TransactionIdentification55(base_types._BaseFieldType):

	__slots__ = ["_PurchsIdrTp", "_TmZone", "_AssoctdData", "_AssoctdDataDstn", "_OthrPurchsIdrTp", "_RtrvlRefNb", "_LifeCyclId", "_AcqrrRefNb", "_PresntmntSeqCnt", "_LifeCyclIdMssng", "_LclDt", "_AuthstnSeqNb", "_AcqrrRefData", "_AuthntcnTkn", "_PresntmntSeqNb", "_SysTracAudtNb", "_IssrRefData", "_LifeCyclSpprt", "_TrnsmssnDtTm", "_LclTm", "_AssoctdDataRef", "_PurchsIdr"]
	@property
	def PurchsIdrTp(self):
		return self._PurchsIdrTp

	@PurchsIdrTp.setter
	def PurchsIdrTp(self, value):
		self._PurchsIdrTp = value if type(value) != base_types.auto else self.make_default("PurchsIdrTp")

	@PurchsIdrTp.deleter
	def PurchsIdrTp(self):
		del self._PurchsIdrTp
		self._PurchsIdrTp = None

	@property
	def TmZone(self):
		return self._TmZone

	@TmZone.setter
	def TmZone(self, value):
		self._TmZone = value if type(value) != base_types.auto else self.make_default("TmZone")

	@TmZone.deleter
	def TmZone(self):
		del self._TmZone
		self._TmZone = None

	@property
	def AssoctdData(self):
		return self._AssoctdData

	@AssoctdData.setter
	def AssoctdData(self, value):
		self._AssoctdData = value if type(value) != base_types.auto else self.make_default("AssoctdData")

	@AssoctdData.deleter
	def AssoctdData(self):
		del self._AssoctdData
		self._AssoctdData = None

	@property
	def AssoctdDataDstn(self):
		return self._AssoctdDataDstn

	@AssoctdDataDstn.setter
	def AssoctdDataDstn(self, value):
		self._AssoctdDataDstn = value if type(value) != base_types.auto else self.make_default("AssoctdDataDstn")

	@AssoctdDataDstn.deleter
	def AssoctdDataDstn(self):
		del self._AssoctdDataDstn
		self._AssoctdDataDstn = None

	@property
	def OthrPurchsIdrTp(self):
		return self._OthrPurchsIdrTp

	@OthrPurchsIdrTp.setter
	def OthrPurchsIdrTp(self, value):
		self._OthrPurchsIdrTp = value if type(value) != base_types.auto else self.make_default("OthrPurchsIdrTp")

	@OthrPurchsIdrTp.deleter
	def OthrPurchsIdrTp(self):
		del self._OthrPurchsIdrTp
		self._OthrPurchsIdrTp = None

	@property
	def RtrvlRefNb(self):
		return self._RtrvlRefNb

	@RtrvlRefNb.setter
	def RtrvlRefNb(self, value):
		self._RtrvlRefNb = value if type(value) != base_types.auto else self.make_default("RtrvlRefNb")

	@RtrvlRefNb.deleter
	def RtrvlRefNb(self):
		del self._RtrvlRefNb
		self._RtrvlRefNb = None

	@property
	def LifeCyclId(self):
		return self._LifeCyclId

	@LifeCyclId.setter
	def LifeCyclId(self, value):
		self._LifeCyclId = value if type(value) != base_types.auto else self.make_default("LifeCyclId")

	@LifeCyclId.deleter
	def LifeCyclId(self):
		del self._LifeCyclId
		self._LifeCyclId = None

	@property
	def AcqrrRefNb(self):
		return self._AcqrrRefNb

	@AcqrrRefNb.setter
	def AcqrrRefNb(self, value):
		self._AcqrrRefNb = value if type(value) != base_types.auto else self.make_default("AcqrrRefNb")

	@AcqrrRefNb.deleter
	def AcqrrRefNb(self):
		del self._AcqrrRefNb
		self._AcqrrRefNb = None

	@property
	def PresntmntSeqCnt(self):
		return self._PresntmntSeqCnt

	@PresntmntSeqCnt.setter
	def PresntmntSeqCnt(self, value):
		self._PresntmntSeqCnt = value if type(value) != base_types.auto else self.make_default("PresntmntSeqCnt")

	@PresntmntSeqCnt.deleter
	def PresntmntSeqCnt(self):
		del self._PresntmntSeqCnt
		self._PresntmntSeqCnt = None

	@property
	def LifeCyclIdMssng(self):
		return self._LifeCyclIdMssng

	@LifeCyclIdMssng.setter
	def LifeCyclIdMssng(self, value):
		self._LifeCyclIdMssng = value if type(value) != base_types.auto else self.make_default("LifeCyclIdMssng")

	@LifeCyclIdMssng.deleter
	def LifeCyclIdMssng(self):
		del self._LifeCyclIdMssng
		self._LifeCyclIdMssng = None

	@property
	def LclDt(self):
		return self._LclDt

	@LclDt.setter
	def LclDt(self, value):
		self._LclDt = value if type(value) != base_types.auto else self.make_default("LclDt")

	@LclDt.deleter
	def LclDt(self):
		del self._LclDt
		self._LclDt = None

	@property
	def AuthstnSeqNb(self):
		return self._AuthstnSeqNb

	@AuthstnSeqNb.setter
	def AuthstnSeqNb(self, value):
		self._AuthstnSeqNb = value if type(value) != base_types.auto else self.make_default("AuthstnSeqNb")

	@AuthstnSeqNb.deleter
	def AuthstnSeqNb(self):
		del self._AuthstnSeqNb
		self._AuthstnSeqNb = None

	@property
	def AcqrrRefData(self):
		return self._AcqrrRefData

	@AcqrrRefData.setter
	def AcqrrRefData(self, value):
		self._AcqrrRefData = value if type(value) != base_types.auto else self.make_default("AcqrrRefData")

	@AcqrrRefData.deleter
	def AcqrrRefData(self):
		del self._AcqrrRefData
		self._AcqrrRefData = None

	@property
	def AuthntcnTkn(self):
		return self._AuthntcnTkn

	@AuthntcnTkn.setter
	def AuthntcnTkn(self, value):
		self._AuthntcnTkn = value if type(value) != base_types.auto else self.make_default("AuthntcnTkn")

	@AuthntcnTkn.deleter
	def AuthntcnTkn(self):
		del self._AuthntcnTkn
		self._AuthntcnTkn = None

	@property
	def PresntmntSeqNb(self):
		return self._PresntmntSeqNb

	@PresntmntSeqNb.setter
	def PresntmntSeqNb(self, value):
		self._PresntmntSeqNb = value if type(value) != base_types.auto else self.make_default("PresntmntSeqNb")

	@PresntmntSeqNb.deleter
	def PresntmntSeqNb(self):
		del self._PresntmntSeqNb
		self._PresntmntSeqNb = None

	@property
	def SysTracAudtNb(self):
		return self._SysTracAudtNb

	@SysTracAudtNb.setter
	def SysTracAudtNb(self, value):
		self._SysTracAudtNb = value if type(value) != base_types.auto else self.make_default("SysTracAudtNb")

	@SysTracAudtNb.deleter
	def SysTracAudtNb(self):
		del self._SysTracAudtNb
		self._SysTracAudtNb = None

	@property
	def IssrRefData(self):
		return self._IssrRefData

	@IssrRefData.setter
	def IssrRefData(self, value):
		self._IssrRefData = value if type(value) != base_types.auto else self.make_default("IssrRefData")

	@IssrRefData.deleter
	def IssrRefData(self):
		del self._IssrRefData
		self._IssrRefData = None

	@property
	def LifeCyclSpprt(self):
		return self._LifeCyclSpprt

	@LifeCyclSpprt.setter
	def LifeCyclSpprt(self, value):
		self._LifeCyclSpprt = value if type(value) != base_types.auto else self.make_default("LifeCyclSpprt")

	@LifeCyclSpprt.deleter
	def LifeCyclSpprt(self):
		del self._LifeCyclSpprt
		self._LifeCyclSpprt = None

	@property
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if type(value) != base_types.auto else self.make_default("TrnsmssnDtTm")

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = None

	@property
	def LclTm(self):
		return self._LclTm

	@LclTm.setter
	def LclTm(self, value):
		self._LclTm = value if type(value) != base_types.auto else self.make_default("LclTm")

	@LclTm.deleter
	def LclTm(self):
		del self._LclTm
		self._LclTm = None

	@property
	def AssoctdDataRef(self):
		return self._AssoctdDataRef

	@AssoctdDataRef.setter
	def AssoctdDataRef(self, value):
		self._AssoctdDataRef = value if type(value) != base_types.auto else self.make_default("AssoctdDataRef")

	@AssoctdDataRef.deleter
	def AssoctdDataRef(self):
		del self._AssoctdDataRef
		self._AssoctdDataRef = None

	@property
	def PurchsIdr(self):
		return self._PurchsIdr

	@PurchsIdr.setter
	def PurchsIdr(self, value):
		self._PurchsIdr = value if type(value) != base_types.auto else self.make_default("PurchsIdr")

	@PurchsIdr.deleter
	def PurchsIdr(self):
		del self._PurchsIdr
		self._PurchsIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PurchsIdrTp', type=PurchaseIdentifierType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmZone', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDataDstn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPurchsIdrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrRefNb', type=Max23NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntmntSeqCnt', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclIdMssng', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnSeqNb', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrRefData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnTkn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PresntmntSeqNb', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrRefData', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclSpprt', type=LifeCycleSupport1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDataRef', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsIdr', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
	))

