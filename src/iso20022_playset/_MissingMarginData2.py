# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CounterpartyData92
from . import MissingMarginTransactionData2
from . import Number

class MissingMarginData2(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_NbOfOutsdngDerivs", "_NbOfOutsdngDerivsWthNoMrgnInf", "_NbOfOutsdngDerivsWthOutdtdMrgnInf", "_TxDtls"]
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
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		return self._NbOfOutsdngDerivsWthNoMrgnInf

	@NbOfOutsdngDerivsWthNoMrgnInf.setter
	def NbOfOutsdngDerivsWthNoMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthNoMrgnInf = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoMrgnInf', Number, False)

	@NbOfOutsdngDerivsWthNoMrgnInf.deleter
	def NbOfOutsdngDerivsWthNoMrgnInf(self):
		del self._NbOfOutsdngDerivsWthNoMrgnInf
		self._NbOfOutsdngDerivsWthNoMrgnInf = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthNoMrgnInf', Number, False)

	@property
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		return self._NbOfOutsdngDerivsWthOutdtdMrgnInf

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.setter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self, value):
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = value if value is not None else base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdMrgnInf', Number, False)

	@NbOfOutsdngDerivsWthOutdtdMrgnInf.deleter
	def NbOfOutsdngDerivsWthOutdtdMrgnInf(self):
		del self._NbOfOutsdngDerivsWthOutdtdMrgnInf
		self._NbOfOutsdngDerivsWthOutdtdMrgnInf = base_types.UninitialisedField(self, 'NbOfOutsdngDerivsWthOutdtdMrgnInf', Number, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', MissingMarginTransactionData2, True)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', MissingMarginTransactionData2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthNoMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfOutsdngDerivsWthOutdtdMrgnInf', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=MissingMarginTransactionData2, min=0, max=None, mutex_group=None, array=True),
	))