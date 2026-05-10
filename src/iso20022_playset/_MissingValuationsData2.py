from . import base_types
from .Number import Number
from .CounterpartyData92 import CounterpartyData92
from .MissingValuationsTransactionData2 import MissingValuationsTransactionData2

class MissingValuationsData2(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_NbOfOutsdngDerivsWthNoValtn", "_TxDtls", "_NbOfOutsdngDerivsWthOutdtdValtn", "_NbOfOutsdngDerivs"]
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
	def NbOfOutsdngDerivsWthNoValtn(self):
		return self._NbOfOutsdngDerivsWthNoValtn

	@NbOfOutsdngDerivsWthNoValtn.setter
	def NbOfOutsdngDerivsWthNoValtn(self, value):
		self._NbOfOutsdngDerivsWthNoValtn = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivsWthNoValtn")

	@NbOfOutsdngDerivsWthNoValtn.deleter
	def NbOfOutsdngDerivsWthNoValtn(self):
		del self._NbOfOutsdngDerivsWthNoValtn
		self._NbOfOutsdngDerivsWthNoValtn = None

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
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		return self._NbOfOutsdngDerivsWthOutdtdValtn

	@NbOfOutsdngDerivsWthOutdtdValtn.setter
	def NbOfOutsdngDerivsWthOutdtdValtn(self, value):
		self._NbOfOutsdngDerivsWthOutdtdValtn = value if type(value) != base_types.auto else self.make_default("NbOfOutsdngDerivsWthOutdtdValtn")

	@NbOfOutsdngDerivsWthOutdtdValtn.deleter
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		del self._NbOfOutsdngDerivsWthOutdtdValtn
		self._NbOfOutsdngDerivsWthOutdtdValtn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=MissingValuationsTransactionData2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

