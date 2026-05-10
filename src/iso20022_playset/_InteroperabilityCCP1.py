from . import base_types
from ._NonNegativeNumber import NonNegativeNumber
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._GenericIdentification168 import GenericIdentification168
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._AssetHolding3 import AssetHolding3

class InteroperabilityCCP1(base_types._BaseFieldType):

	__slots__ = ["_TrdsClrd", "_GrssNtnlAmt", "_TtlInitlMrgn", "_Id", "_AsstHldg"]
	@property
	def TrdsClrd(self):
		return self._TrdsClrd

	@TrdsClrd.setter
	def TrdsClrd(self, value):
		self._TrdsClrd = value if type(value) != base_types.auto else self.make_default("TrdsClrd")

	@TrdsClrd.deleter
	def TrdsClrd(self):
		del self._TrdsClrd
		self._TrdsClrd = None

	@property
	def GrssNtnlAmt(self):
		return self._GrssNtnlAmt

	@GrssNtnlAmt.setter
	def GrssNtnlAmt(self, value):
		self._GrssNtnlAmt = value if type(value) != base_types.auto else self.make_default("GrssNtnlAmt")

	@GrssNtnlAmt.deleter
	def GrssNtnlAmt(self):
		del self._GrssNtnlAmt
		self._GrssNtnlAmt = None

	@property
	def TtlInitlMrgn(self):
		return self._TtlInitlMrgn

	@TtlInitlMrgn.setter
	def TtlInitlMrgn(self, value):
		self._TtlInitlMrgn = value if type(value) != base_types.auto else self.make_default("TtlInitlMrgn")

	@TtlInitlMrgn.deleter
	def TtlInitlMrgn(self):
		del self._TtlInitlMrgn
		self._TtlInitlMrgn = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AsstHldg(self):
		return self._AsstHldg

	@AsstHldg.setter
	def AsstHldg(self, value):
		self._AsstHldg = value if type(value) != base_types.auto else self.make_default("AsstHldg")

	@AsstHldg.deleter
	def AsstHldg(self):
		del self._AsstHldg
		self._AsstHldg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrdsClrd', type=NonNegativeNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssNtnlAmt', type=ActiveCurrencyAnd24Amount, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlInitlMrgn', type=ActiveCurrencyAndAmount, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstHldg', type=AssetHolding3, min=1, max=None, mutex_group=None, array=True),
	))

