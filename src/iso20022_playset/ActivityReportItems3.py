import base_types
import Max35Text
import BICIdentification1
import DocumentIdentification5
import ActivityDetails1
import PendingActivity2

class ActivityReportItems3(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_UsrTxRef", "_PdgReqForActn", "_RptdNtty", "_RptdItm"]
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
	def PdgReqForActn(self):
		return self._PdgReqForActn

	@PdgReqForActn.setter
	def PdgReqForActn(self, value):
		self._PdgReqForActn = value if type(value) != auto else self.make_default("PdgReqForActn")

	@PdgReqForActn.deleter
	def PdgReqForActn(self):
		del self._PdgReqForActn
		self._PdgReqForActn = None

	@property
	def RptdNtty(self):
		return self._RptdNtty

	@RptdNtty.setter
	def RptdNtty(self, value):
		self._RptdNtty = value if type(value) != auto else self.make_default("RptdNtty")

	@RptdNtty.deleter
	def RptdNtty(self):
		del self._RptdNtty
		self._RptdNtty = None

	@property
	def RptdItm(self):
		return self._RptdItm

	@RptdItm.setter
	def RptdItm(self, value):
		self._RptdItm = value if type(value) != auto else self.make_default("RptdItm")

	@RptdItm.deleter
	def RptdItm(self):
		del self._RptdItm
		self._RptdItm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrTxRef', type=DocumentIdentification5, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdgReqForActn', type=PendingActivity2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptdNtty', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptdItm', type=ActivityDetails1, min=1, max=None, mutex_group=None, array=True),
	))

