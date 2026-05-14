from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Exact12Text import Exact12Text
from ._Exact15Text import Exact15Text
from ._ISODateTime import ISODateTime
from ._Max12NumericText import Max12NumericText
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._Max99Text import Max99Text
from ._PurchaseIdentifierType3Code import PurchaseIdentifierType3Code
from ._TrueFalseIndicator import TrueFalseIndicator

class TransactionIdentification61(base_types._BaseFieldType):

	__slots__ = ["_AssoctdData", "_AssoctdDataDstn", "_AssoctdDataRef", "_LifeCyclId", "_NtlData", "_PrvtData", "_PurchsIdr", "_PurchsIdrTp", "_RtrvlRefNb", "_SysTracAudtNb", "_TrnsmssnDtTm"]
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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

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
	def TrnsmssnDtTm(self):
		return self._TrnsmssnDtTm

	@TrnsmssnDtTm.setter
	def TrnsmssnDtTm(self, value):
		self._TrnsmssnDtTm = value if type(value) != base_types.auto else self.make_default("TrnsmssnDtTm")

	@TrnsmssnDtTm.deleter
	def TrnsmssnDtTm(self):
		del self._TrnsmssnDtTm
		self._TrnsmssnDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AssoctdData', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDataDstn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDataRef', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LifeCyclId', type=Exact15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsIdr', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsIdrTp', type=PurchaseIdentifierType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlRefNb', type=Exact12Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysTracAudtNb', type=Max12NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmssnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

