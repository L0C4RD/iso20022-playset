from . import base_types
from .MessageIdentification1 import MessageIdentification1
from .ContactIdentification1 import ContactIdentification1
from .BankContactPerson1Choice import BankContactPerson1Choice
from .Baseline5 import Baseline5
from .ContactIdentification3 import ContactIdentification3
from .SimpleIdentificationInformation import SimpleIdentificationInformation

class BaselineReSubmissionV05(base_types._BaseFieldType):

	__slots__ = ["_Baseln", "_SubmissnId", "_SellrCtctPrsn", "_BuyrCtctPrsn", "_OthrBkCtctPrsn", "_SubmitrTxRef", "_TxId", "_BkCtctPrsn"]
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
	def SubmissnId(self):
		return self._SubmissnId

	@SubmissnId.setter
	def SubmissnId(self, value):
		self._SubmissnId = value if type(value) != base_types.auto else self.make_default("SubmissnId")

	@SubmissnId.deleter
	def SubmissnId(self):
		del self._SubmissnId
		self._SubmissnId = None

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

	@property
	def BkCtctPrsn(self):
		return self._BkCtctPrsn

	@BkCtctPrsn.setter
	def BkCtctPrsn(self, value):
		self._BkCtctPrsn = value if type(value) != base_types.auto else self.make_default("BkCtctPrsn")

	@BkCtctPrsn.deleter
	def BkCtctPrsn(self):
		del self._BkCtctPrsn
		self._BkCtctPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Baseln', type=Baseline5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrCtctPrsn', type=ContactIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrBkCtctPrsn', type=ContactIdentification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitrTxRef', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkCtctPrsn', type=BankContactPerson1Choice, min=1, max=1, mutex_group=None, array=False),
	))

