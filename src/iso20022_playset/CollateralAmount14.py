import base_types
import AmountAndDirection49

class CollateralAmount14(base_types._BaseFieldType):

	__slots__ = ["_Termntn", "_Acrd", "_ValSght", "_UdsptdTx", "_Tx"]
	@property
	def Termntn(self):
		return self._Termntn

	@Termntn.setter
	def Termntn(self, value):
		self._Termntn = value if type(value) != auto else self.make_default("Termntn")

	@Termntn.deleter
	def Termntn(self):
		del self._Termntn
		self._Termntn = None

	@property
	def Acrd(self):
		return self._Acrd

	@Acrd.setter
	def Acrd(self, value):
		self._Acrd = value if type(value) != auto else self.make_default("Acrd")

	@Acrd.deleter
	def Acrd(self):
		del self._Acrd
		self._Acrd = None

	@property
	def ValSght(self):
		return self._ValSght

	@ValSght.setter
	def ValSght(self, value):
		self._ValSght = value if type(value) != auto else self.make_default("ValSght")

	@ValSght.deleter
	def ValSght(self):
		del self._ValSght
		self._ValSght = None

	@property
	def UdsptdTx(self):
		return self._UdsptdTx

	@UdsptdTx.setter
	def UdsptdTx(self, value):
		self._UdsptdTx = value if type(value) != auto else self.make_default("UdsptdTx")

	@UdsptdTx.deleter
	def UdsptdTx(self):
		del self._UdsptdTx
		self._UdsptdTx = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Termntn', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acrd', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValSght', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdsptdTx', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
	))

