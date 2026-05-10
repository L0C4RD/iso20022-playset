from . import base_types
from .Max35Text import Max35Text
from .TaxType9Code import TaxType9Code

class TaxType2Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrTaxTp", "_Tp"]
	@property
	def OthrTaxTp(self):
		return self._OthrTaxTp

	@OthrTaxTp.setter
	def OthrTaxTp(self, value):
		self._OthrTaxTp = value if type(value) != base_types.auto else self.make_default("OthrTaxTp")

	@OthrTaxTp.deleter
	def OthrTaxTp(self):
		del self._OthrTaxTp
		self._OthrTaxTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrTaxTp', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType9Code, min=0, max=1, mutex_group=1, array=False),
	))

