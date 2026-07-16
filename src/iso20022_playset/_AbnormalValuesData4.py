# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AbnormalValuesTransactionData2
from . import CounterpartyData92
from . import Number

class AbnormalValuesData4(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyId", "_NbOfDerivsRptd", "_NbOfDerivsRptdWthOtlrs", "_TxDtls"]
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
	def NbOfDerivsRptd(self):
		return self._NbOfDerivsRptd

	@NbOfDerivsRptd.setter
	def NbOfDerivsRptd(self, value):
		self._NbOfDerivsRptd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDerivsRptd', Number, False)

	@NbOfDerivsRptd.deleter
	def NbOfDerivsRptd(self):
		del self._NbOfDerivsRptd
		self._NbOfDerivsRptd = base_types.UninitialisedField(self, 'NbOfDerivsRptd', Number, False)

	@property
	def NbOfDerivsRptdWthOtlrs(self):
		return self._NbOfDerivsRptdWthOtlrs

	@NbOfDerivsRptdWthOtlrs.setter
	def NbOfDerivsRptdWthOtlrs(self, value):
		self._NbOfDerivsRptdWthOtlrs = value if value is not None else base_types.UninitialisedField(self, 'NbOfDerivsRptdWthOtlrs', Number, False)

	@NbOfDerivsRptdWthOtlrs.deleter
	def NbOfDerivsRptdWthOtlrs(self):
		del self._NbOfDerivsRptdWthOtlrs
		self._NbOfDerivsRptdWthOtlrs = base_types.UninitialisedField(self, 'NbOfDerivsRptdWthOtlrs', Number, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', AbnormalValuesTransactionData2, True)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', AbnormalValuesTransactionData2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyId', type=CounterpartyData92, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDerivsRptd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDerivsRptdWthOtlrs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=AbnormalValuesTransactionData2, min=0, max=None, mutex_group=None, array=True),
	))