from . import base_types
from ._CollateralAmount9 import CollateralAmount9
from ._BaseOneRate import BaseOneRate

class ValuationsDetails2(base_types._BaseFieldType):

	__slots__ = ["_Hrcut", "_ValtnDtlsAmt"]
	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != base_types.auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	@property
	def ValtnDtlsAmt(self):
		return self._ValtnDtlsAmt

	@ValtnDtlsAmt.setter
	def ValtnDtlsAmt(self, value):
		self._ValtnDtlsAmt = value if type(value) != base_types.auto else self.make_default("ValtnDtlsAmt")

	@ValtnDtlsAmt.deleter
	def ValtnDtlsAmt(self):
		del self._ValtnDtlsAmt
		self._ValtnDtlsAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrcut', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtlsAmt', type=CollateralAmount9, min=1, max=None, mutex_group=None, array=True),
	))

