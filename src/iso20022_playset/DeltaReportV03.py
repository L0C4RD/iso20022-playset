import base_types
import TransactionStatus4
import ComparisonResult2
import BICIdentification1
import MessageIdentification1
import DocumentIdentification3
import PendingActivity2
import DocumentIdentification5
import Count1
import DocumentIdentification1
import SimpleIdentificationInformation
import PartyIdentification26

class DeltaReportV03(base_types._BaseFieldType):

	__slots__ = ["_ReqForActn", "_Sellr", "_EstblishdBaselnId", "_Buyr", "_BuyrBk", "_SellrBk", "_TxId", "_UsrTxRef", "_AmdmntNb", "_UpdtdElmt", "_TxSts", "_RptId", "_SubmitrPropsdBaselnRef"]
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
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

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
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def BuyrBk(self):
		return self._BuyrBk

	@BuyrBk.setter
	def BuyrBk(self, value):
		self._BuyrBk = value if type(value) != auto else self.make_default("BuyrBk")

	@BuyrBk.deleter
	def BuyrBk(self):
		del self._BuyrBk
		self._BuyrBk = None

	@property
	def SellrBk(self):
		return self._SellrBk

	@SellrBk.setter
	def SellrBk(self, value):
		self._SellrBk = value if type(value) != auto else self.make_default("SellrBk")

	@SellrBk.deleter
	def SellrBk(self):
		del self._SellrBk
		self._SellrBk = None

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
	def AmdmntNb(self):
		return self._AmdmntNb

	@AmdmntNb.setter
	def AmdmntNb(self, value):
		self._AmdmntNb = value if type(value) != auto else self.make_default("AmdmntNb")

	@AmdmntNb.deleter
	def AmdmntNb(self):
		del self._AmdmntNb
		self._AmdmntNb = None

	@property
	def UpdtdElmt(self):
		return self._UpdtdElmt

	@UpdtdElmt.setter
	def UpdtdElmt(self, value):
		self._UpdtdElmt = value if type(value) != auto else self.make_default("UpdtdElmt")

	@UpdtdElmt.deleter
	def UpdtdElmt(self):
		del self._UpdtdElmt
		self._UpdtdElmt = None

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
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def SubmitrPropsdBaselnRef(self):
		return self._SubmitrPropsdBaselnRef

	@SubmitrPropsdBaselnRef.setter
	def SubmitrPropsdBaselnRef(self, value):
		self._SubmitrPropsdBaselnRef = value if type(value) != auto else self.make_default("SubmitrPropsdBaselnRef")

	@SubmitrPropsdBaselnRef.deleter
	def SubmitrPropsdBaselnRef(self):
		del self._SubmitrPropsdBaselnRef
		self._SubmitrPropsdBaselnRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmdmntNb', type=Count1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdtdElmt', type=ComparisonResult2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitrPropsdBaselnRef', type=DocumentIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

