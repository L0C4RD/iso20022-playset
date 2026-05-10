from . import base_types
from ._ContactIdentification3 import ContactIdentification3
from ._SimpleIdentificationInformation import SimpleIdentificationInformation
from ._ContactIdentification1 import ContactIdentification1
from ._MessageIdentification1 import MessageIdentification1
from ._Baseline5 import Baseline5

class BaselineAmendmentRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Baseln", "_TxId", "_SubmitrTxRef", "_ReqId", "_SellrBkCtctPrsn", "_BuyrCtctPrsn", "_BuyrBkCtctPrsn", "_SellrCtctPrsn", "_OthrBkCtctPrsn"]
	@property
	def Baseln(self):
		return self._Baseln

	@Baseln.setter
	def Baseln(self, value):
		self._Baseln = value if type(value) != base_types.auto else self.make_default("Baseln")

	@Baseln.deleter
	def Baseln(self):
		del self._Baseln
		self._Baseln = None

	@property
	def BuyrBkCtctPrsn(self):
		return self._BuyrBkCtctPrsn

	@BuyrBkCtctPrsn.setter
	def BuyrBkCtctPrsn(self, value):
		self._BuyrBkCtctPrsn = value if type(value) != base_types.auto else self.make_default("BuyrBkCtctPrsn")

	@BuyrBkCtctPrsn.deleter
	def BuyrBkCtctPrsn(self):
		del self._BuyrBkCtctPrsn
		self._BuyrBkCtctPrsn = None

	@property
	def BuyrCtctPrsn(self):
		return self._BuyrCtctPrsn

	@BuyrCtctPrsn.setter
	def BuyrCtctPrsn(self, value):
		self._BuyrCtctPrsn = value if type(value) != base_types.auto else self.make_default("BuyrCtctPrsn")

	@BuyrCtctPrsn.deleter
	def BuyrCtctPrsn(self):
		del self._BuyrCtctPrsn
		self._BuyrCtctPrsn = None

	@property
	def OthrBkCtctPrsn(self):
		return self._OthrBkCtctPrsn

	@OthrBkCtctPrsn.setter
	def OthrBkCtctPrsn(self, value):
		self._OthrBkCtctPrsn = value if type(value) != base_types.auto else self.make_default("OthrBkCtctPrsn")

	@OthrBkCtctPrsn.deleter
	def OthrBkCtctPrsn(self):
		del self._OthrBkCtctPrsn
		self._OthrBkCtctPrsn = None

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != base_types.auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

	@property
	def SellrBkCtctPrsn(self):
		return self._SellrBkCtctPrsn

	@SellrBkCtctPrsn.setter
	def SellrBkCtctPrsn(self, value):
		self._SellrBkCtctPrsn = value if type(value) != base_types.auto else self.make_default("SellrBkCtctPrsn")

	@SellrBkCtctPrsn.deleter
	def SellrBkCtctPrsn(self):
		del self._SellrBkCtctPrsn
		self._SellrBkCtctPrsn = None

	@property
	def SellrCtctPrsn(self):
		return self._SellrCtctPrsn

	@SellrCtctPrsn.setter
	def SellrCtctPrsn(self, value):
		self._SellrCtctPrsn = value if type(value) != base_types.auto else self.make_default("SellrCtctPrsn")

	@SellrCtctPrsn.deleter
	def SellrCtctPrsn(self):
		del self._SellrCtctPrsn
		self._SellrCtctPrsn = None

	@property
	def SubmitrTxRef(self):
		return self._SubmitrTxRef

	@SubmitrTxRef.setter
	def SubmitrTxRef(self, value):
		self._SubmitrTxRef = value if type(value) != base_types.auto else self.make_default("SubmitrTxRef")

	@SubmitrTxRef.deleter
	def SubmitrTxRef(self):
		del self._SubmitrTxRef
		self._SubmitrTxRef = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Baseln', type=Baseline5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBkCtctPrsn', type=ContactIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrBkCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))

