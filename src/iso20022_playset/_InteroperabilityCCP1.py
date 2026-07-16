# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd24Amount
from . import ActiveCurrencyAndAmount
from . import AssetHolding3
from . import GenericIdentification168
from . import NonNegativeNumber

class InteroperabilityCCP1(base_types._BaseFieldType):

	__slots__ = ["_AsstHldg", "_GrssNtnlAmt", "_Id", "_TrdsClrd", "_TtlInitlMrgn"]
	@property
	def AsstHldg(self):
		return self._AsstHldg

	@AsstHldg.setter
	def AsstHldg(self, value):
		self._AsstHldg = value if value is not None else base_types.UninitialisedField(self, 'AsstHldg', AssetHolding3, True)

	@AsstHldg.deleter
	def AsstHldg(self):
		del self._AsstHldg
		self._AsstHldg = base_types.UninitialisedField(self, 'AsstHldg', AssetHolding3, True)

	@property
	def GrssNtnlAmt(self):
		return self._GrssNtnlAmt

	@GrssNtnlAmt.setter
	def GrssNtnlAmt(self, value):
		self._GrssNtnlAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssNtnlAmt', ActiveCurrencyAnd24Amount, True)

	@GrssNtnlAmt.deleter
	def GrssNtnlAmt(self):
		del self._GrssNtnlAmt
		self._GrssNtnlAmt = base_types.UninitialisedField(self, 'GrssNtnlAmt', ActiveCurrencyAnd24Amount, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification168, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification168, False)

	@property
	def TrdsClrd(self):
		return self._TrdsClrd

	@TrdsClrd.setter
	def TrdsClrd(self, value):
		self._TrdsClrd = value if value is not None else base_types.UninitialisedField(self, 'TrdsClrd', NonNegativeNumber, False)

	@TrdsClrd.deleter
	def TrdsClrd(self):
		del self._TrdsClrd
		self._TrdsClrd = base_types.UninitialisedField(self, 'TrdsClrd', NonNegativeNumber, False)

	@property
	def TtlInitlMrgn(self):
		return self._TtlInitlMrgn

	@TtlInitlMrgn.setter
	def TtlInitlMrgn(self, value):
		self._TtlInitlMrgn = value if value is not None else base_types.UninitialisedField(self, 'TtlInitlMrgn', ActiveCurrencyAndAmount, True)

	@TtlInitlMrgn.deleter
	def TtlInitlMrgn(self):
		del self._TtlInitlMrgn
		self._TtlInitlMrgn = base_types.UninitialisedField(self, 'TtlInitlMrgn', ActiveCurrencyAndAmount, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstHldg', type=AssetHolding3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrssNtnlAmt', type=ActiveCurrencyAnd24Amount, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrdsClrd', type=NonNegativeNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlInitlMrgn', type=ActiveCurrencyAndAmount, min=1, max=None, mutex_group=None, array=True),
	))