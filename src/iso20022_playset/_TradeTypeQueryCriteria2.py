from . import base_types
from ._CollateralType6Code import CollateralType6Code
from ._ExposureType10Code import ExposureType10Code
from ._Operation3Code import Operation3Code

class TradeTypeQueryCriteria2(base_types._BaseFieldType):

	__slots__ = ["_Oprtr", "_SctiesFincgTxTp", "_CollCmpntTp"]
	@property
	def CollCmpntTp(self):
		return self._CollCmpntTp

	@CollCmpntTp.setter
	def CollCmpntTp(self, value):
		self._CollCmpntTp = value if type(value) != base_types.auto else self.make_default("CollCmpntTp")

	@CollCmpntTp.deleter
	def CollCmpntTp(self):
		del self._CollCmpntTp
		self._CollCmpntTp = None

	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if type(value) != base_types.auto else self.make_default("Oprtr")

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = None

	@property
	def SctiesFincgTxTp(self):
		return self._SctiesFincgTxTp

	@SctiesFincgTxTp.setter
	def SctiesFincgTxTp(self, value):
		self._SctiesFincgTxTp = value if type(value) != base_types.auto else self.make_default("SctiesFincgTxTp")

	@SctiesFincgTxTp.deleter
	def SctiesFincgTxTp(self):
		del self._SctiesFincgTxTp
		self._SctiesFincgTxTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollCmpntTp', type=CollateralType6Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oprtr', type=Operation3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTxTp', type=ExposureType10Code, min=0, max=None, mutex_group=None, array=True),
	))

