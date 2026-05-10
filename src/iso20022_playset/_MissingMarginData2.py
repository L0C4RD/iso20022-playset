from . import base_types
from .Number import Number
from .MissingMarginTransactionData2 import MissingMarginTransactionData2
from .CounterpartyData92 import CounterpartyData92

class MissingMarginData2(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_TxDtls", "_NbOfOutsdngDerivsWthNoMrgnInf", "_NbOfOutsdngDerivs", "_NbOfOutsdngDerivsWthOutdtdMrgnInf"]
	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != base_types.auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		return self._NbOfOutsdngDerivsWthNoMrgnInf

	@NbOfOutsdngDerivsWthNoMrgnInf.setter
	def NbOfOutsdngDerivsWthNoMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthNoMrgnInf = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivsWthNoMrgnInf")

	@NbOfOutsdngDerivsWthNoMrgnInf.deleter
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		del self._NbOfOutsdngDerivsWthNoMrgnInf
		self._NbOfOutsdngDerivsWthNoMrgnInf = None

	@property
	def NbOfOutsdngDerivs(self):
		return self._NbOfOutsdngDerivs

	@NbOfOutsdngDerivs.setter
	def NbOfOutsdngDerivs(self, value):
		self._NbOfOutsdngDerivs = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivs")

	@NbOfOutsdngDerivs.deleter
	def NbOfOutsdngDerivs(self):
		del self._NbOfOutsdngDerivs
		self._NbOfOutsdngDerivs = None

	@property
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		return self._NbOfOutsdngDerivsWthOutdtdMrgnInf

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.setter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivsWthOutdtdMrgnInf")

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.deleter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		del self._NbOfOutsdngDerivsWthOutdtdMrgnInf
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=MissingMarginTransactionData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

