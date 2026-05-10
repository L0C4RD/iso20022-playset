from . import base_types
from .SimpleIdentificationInformation import SimpleIdentificationInformation
from .MessageIdentification1 import MessageIdentification1
from .TransactionStatus4 import TransactionStatus4
from .PendingActivity2 import PendingActivity2
from .DocumentIdentification3 import DocumentIdentification3
from .ContactIdentification1 import ContactIdentification1
from .ContactIdentification3 import ContactIdentification3
from .Baseline5 import Baseline5
from .DocumentIdentification5 import DocumentIdentification5
from .ReportType1 import ReportType1

class FullPushThroughReportV05(base_types._BaseFieldType):

	__slots__ = ["_PushdThrghBaseln", "_ReqForActn", "_SellrCtctPrsn", "_TxSts", "_TxId", "_BuyrBkCtctPrsn", "_EstblishdBaselnId", "_UsrTxRef", "_OthrBkCtctPrsn", "_SellrBkCtctPrsn", "_RptPurp", "_BuyrCtctPrsn", "_RptId"]
	@property
	def PushdThrghBaseln(self):
		return self._PushdThrghBaseln

	@PushdThrghBaseln.setter
	def PushdThrghBaseln(self, value):
		self._PushdThrghBaseln = value if type(value) != auto else self.make_default("PushdThrghBaseln")

	@PushdThrghBaseln.deleter
	def PushdThrghBaseln(self):
		del self._PushdThrghBaseln
		self._PushdThrghBaseln = None

	@property
	def ReqForActn(self):
		return self._ReqForActn

	@ReqForActn.setter
	def ReqForActn(self, value):
		self._ReqForActn = value if type(value) != auto else self.make_default("ReqForActn")

	@ReqForActn.deleter
	def ReqForActn(self):
		del self._ReqForActn
		self._ReqForActn = None

	@property
	def SellrCtctPrsn(self):
		return self._SellrCtctPrsn

	@SellrCtctPrsn.setter
	def SellrCtctPrsn(self, value):
		self._SellrCtctPrsn = value if type(value) != auto else self.make_default("SellrCtctPrsn")

	@SellrCtctPrsn.deleter
	def SellrCtctPrsn(self):
		del self._SellrCtctPrsn
		self._SellrCtctPrsn = None

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if type(value) != auto else self.make_default("TxSts")

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def BuyrBkCtctPrsn(self):
		return self._BuyrBkCtctPrsn

	@BuyrBkCtctPrsn.setter
	def BuyrBkCtctPrsn(self, value):
		self._BuyrBkCtctPrsn = value if type(value) != auto else self.make_default("BuyrBkCtctPrsn")

	@BuyrBkCtctPrsn.deleter
	def BuyrBkCtctPrsn(self):
		del self._BuyrBkCtctPrsn
		self._BuyrBkCtctPrsn = None

	@property
	def EstblishdBaselnId(self):
		return self._EstblishdBaselnId

	@EstblishdBaselnId.setter
	def EstblishdBaselnId(self, value):
		self._EstblishdBaselnId = value if type(value) != auto else self.make_default("EstblishdBaselnId")

	@EstblishdBaselnId.deleter
	def EstblishdBaselnId(self):
		del self._EstblishdBaselnId
		self._EstblishdBaselnId = None

	@property
	def UsrTxRef(self):
		return self._UsrTxRef

	@UsrTxRef.setter
	def UsrTxRef(self, value):
		self._UsrTxRef = value if type(value) != auto else self.make_default("UsrTxRef")

	@UsrTxRef.deleter
	def UsrTxRef(self):
		del self._UsrTxRef
		self._UsrTxRef = None

	@property
	def OthrBkCtctPrsn(self):
		return self._OthrBkCtctPrsn

	@OthrBkCtctPrsn.setter
	def OthrBkCtctPrsn(self, value):
		self._OthrBkCtctPrsn = value if type(value) != auto else self.make_default("OthrBkCtctPrsn")

	@OthrBkCtctPrsn.deleter
	def OthrBkCtctPrsn(self):
		del self._OthrBkCtctPrsn
		self._OthrBkCtctPrsn = None

	@property
	def SellrBkCtctPrsn(self):
		return self._SellrBkCtctPrsn

	@SellrBkCtctPrsn.setter
	def SellrBkCtctPrsn(self, value):
		self._SellrBkCtctPrsn = value if type(value) != auto else self.make_default("SellrBkCtctPrsn")

	@SellrBkCtctPrsn.deleter
	def SellrBkCtctPrsn(self):
		del self._SellrBkCtctPrsn
		self._SellrBkCtctPrsn = None

	@property
	def RptPurp(self):
		return self._RptPurp

	@RptPurp.setter
	def RptPurp(self, value):
		self._RptPurp = value if type(value) != auto else self.make_default("RptPurp")

	@RptPurp.deleter
	def RptPurp(self):
		del self._RptPurp
		self._RptPurp = None

	@property
	def BuyrCtctPrsn(self):
		return self._BuyrCtctPrsn

	@BuyrCtctPrsn.setter
	def BuyrCtctPrsn(self, value):
		self._BuyrCtctPrsn = value if type(value) != auto else self.make_default("BuyrCtctPrsn")

	@BuyrCtctPrsn.deleter
	def BuyrCtctPrsn(self):
		del self._BuyrCtctPrsn
		self._BuyrCtctPrsn = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PushdThrghBaseln', type=Baseline5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBkCtctPrsn', type=ContactIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptPurp', type=ReportType1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

