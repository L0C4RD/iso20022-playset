# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CounterpartyData92
from . import MissingValuationsTransactionData2
from . import Number

class MissingValuationsData2(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_NbOfOutsdngDerivs", "_NbOfOutsdngDerivsWthNoValtn", "_NbOfOutsdngDerivsWthOutdtdValtn", "_TxDtls"]
	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyData92, False)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', CounterpartyData92, False)

	@property
	def NbOfOutsdngDerivs(self):
		return self._NbOfOutsdngDerivs

	@NbOfOutsdngDerivs.setter
	def NbOfOutsdngDerivs(self, value):
		self._NbOfOutsdngDerivs = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivs', Number, False)

	@NbOfOutsdngDerivs.deleter
	def NbOfOutsdngDerivs(self):
		del self._NbOfOutsdngDerivs
		self._NbOfOutsdngDerivs = base_types.UninitialisedField(self, 'NbOfOutsdngDerivs', Number, False)

	@property
	def NbOfOutsdngDerivsWthNoValtn(self):
		return self._NbOfOutsdngDerivsWthNoValtn

	@NbOfOutsdngDerivsWthNoValtn.setter
	def NbOfOutsdngDerivsWthNoValtn(self, value):
		self._NbOfOutsdngDerivsWthNoValtn = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoValtn', Number, False)

	@NbOfOutsdngDerivsWthNoValtn.deleter
	def NbOfOutsdngDerivsWthNoValtn(self):
		del self._NbOfOutsdngDerivsWthNoValtn
		self._NbOfOutsdngDerivsWthNoValtn = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoValtn', Number, False)

	@property
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		return self._NbOfOutsdngDerivsWthOutdtdValtn

	@NbOfOutsdngDerivsWthOutdtdValtn.setter
	def NbOfOutsdngDerivsWthOutdtdValtn(self, value):
		self._NbOfOutsdngDerivsWthOutdtdValtn = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdValtn', Number, False)

	@NbOfOutsdngDerivsWthOutdtdValtn.deleter
	def NbOfOutsdngDerivsWthOutdtdValtn(self):
		del self._NbOfOutsdngDerivsWthOutdtdValtn
		self._NbOfOutsdngDerivsWthOutdtdValtn = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdValtn', Number, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', MissingValuationsTransactionData2, True)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', MissingValuationsTransactionData2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdValtn', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=MissingValuationsTransactionData2, min=0, max=None, mutex_group=None, array=True),
	))