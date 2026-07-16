# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection49

class CollateralAmount14(base_types._BaseFieldType):

	__slots__ = ["_Acrd", "_Termntn", "_Tx", "_UdsptdTx", "_ValSght"]
	@property
	def Acrd(self):
		return self._Acrd

	@Acrd.setter
	def Acrd(self, value):
		self._Acrd = value if value is not None else base_types.UninitialisedField(self, 'Acrd', AmountAndDirection49, False)

	@Acrd.deleter
	def Acrd(self):
		del self._Acrd
		self._Acrd = base_types.UninitialisedField(self, 'Acrd', AmountAndDirection49, False)

	@property
	def Termntn(self):
		return self._Termntn

	@Termntn.setter
	def Termntn(self, value):
		self._Termntn = value if value is not None else base_types.UninitialisedField(self, 'Termntn', AmountAndDirection49, False)

	@Termntn.deleter
	def Termntn(self):
		del self._Termntn
		self._Termntn = base_types.UninitialisedField(self, 'Termntn', AmountAndDirection49, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', AmountAndDirection49, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', AmountAndDirection49, False)

	@property
	def UdsptdTx(self):
		return self._UdsptdTx

	@UdsptdTx.setter
	def UdsptdTx(self, value):
		self._UdsptdTx = value if value is not None else base_types.UninitialisedField(self, 'UdsptdTx', AmountAndDirection49, False)

	@UdsptdTx.deleter
	def UdsptdTx(self):
		del self._UdsptdTx
		self._UdsptdTx = base_types.UninitialisedField(self, 'UdsptdTx', AmountAndDirection49, False)

	@property
	def ValSght(self):
		return self._ValSght

	@ValSght.setter
	def ValSght(self, value):
		self._ValSght = value if value is not None else base_types.UninitialisedField(self, 'ValSght', AmountAndDirection49, False)

	@ValSght.deleter
	def ValSght(self):
		del self._ValSght
		self._ValSght = base_types.UninitialisedField(self, 'ValSght', AmountAndDirection49, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acrd', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Termntn', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdsptdTx', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSght', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
	))