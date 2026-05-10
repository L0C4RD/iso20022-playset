from . import base_types
import DocumentIdentification3
import MessageIdentification1
import PendingActivity2
import TransactionStatus4
import PartyIdentification26
import MisMatchReport3
import SimpleIdentificationInformation
import ReportType3
import DocumentIdentification10
import BICIdentification1
import DocumentIdentification5

class DataSetMatchReportV03(base_types._BaseFieldType):

	__slots__ = ["_TxSts", "_EstblishdBaselnId", "_BuyrBk", "_CmpardDocRef", "_SubmissnTp", "_Rpt", "_ReqForActn", "_UsrTxRef", "_Sellr", "_SellrBk", "_RptId", "_TxId", "_Buyr"]
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
	def CmpardDocRef(self):
		return self._CmpardDocRef

	@CmpardDocRef.setter
	def CmpardDocRef(self, value):
		self._CmpardDocRef = value if type(value) != auto else self.make_default("CmpardDocRef")

	@CmpardDocRef.deleter
	def CmpardDocRef(self):
		del self._CmpardDocRef
		self._CmpardDocRef = None

	@property
	def SubmissnTp(self):
		return self._SubmissnTp

	@SubmissnTp.setter
	def SubmissnTp(self, value):
		self._SubmissnTp = value if type(value) != auto else self.make_default("SubmissnTp")

	@SubmissnTp.deleter
	def SubmissnTp(self):
		del self._SubmissnTp
		self._SubmissnTp = None

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if type(value) != auto else self.make_default("Rpt")

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = None

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
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxSts', type=TransactionStatus4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdBaselnId', type=DocumentIdentification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpardDocRef', type=DocumentIdentification10, min=2, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmissnTp', type=ReportType3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=MisMatchReport3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForActn', type=PendingActivity2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sellr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBk', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentification26, min=1, max=1, mutex_group=None, array=False),
	))

