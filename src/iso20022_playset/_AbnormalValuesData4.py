from . import base_types
from ._CounterpartyData92 import CounterpartyData92
from ._AbnormalValuesTransactionData2 import AbnormalValuesTransactionData2
from ._Number import Number

class AbnormalValuesData4(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_NbOfDerivsRptdWthOtlrs", "_TxDtls", "_NbOfDerivsRptd"]
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
	def NbOfDerivsRptd(self):
		return self._NbOfDerivsRptd

	@NbOfDerivsRptd.setter
	def NbOfDerivsRptd(self, value):
		self._NbOfDerivsRptd = value if type(value) != base_types.auto else self.make_default("NbOfDerivsRptd")

	@NbOfDerivsRptd.deleter
	def NbOfDerivsRptd(self):
		del self._NbOfDerivsRptd
		self._NbOfDerivsRptd = None

	@property
	def NbOfDerivsRptdWthOtlrs(self):
		return self._NbOfDerivsRptdWthOtlrs

	@NbOfDerivsRptdWthOtlrs.setter
	def NbOfDerivsRptdWthOtlrs(self, value):
		self._NbOfDerivsRptdWthOtlrs = value if type(value) != base_types.auto else self.make_default("NbOfDerivsRptdWthOtlrs")

	@NbOfDerivsRptdWthOtlrs.deleter
	def NbOfDerivsRptdWthOtlrs(self):
		del self._NbOfDerivsRptdWthOtlrs
		self._NbOfDerivsRptdWthOtlrs = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDerivsRptd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDerivsRptdWthOtlrs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=AbnormalValuesTransactionData2, min=0, max=None, mutex_group=None, array=True),
	))

