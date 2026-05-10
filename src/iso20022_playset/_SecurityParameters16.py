from . import base_types
from .Max256Text import Max256Text
from .Max140Binary import Max140Binary
from .TerminalManagementAction3Code import TerminalManagementAction3Code
from .CryptographicKey18 import CryptographicKey18

class SecurityParameters16(base_types._BaseFieldType):

	__slots__ = ["_Vrsn", "_ActnTp", "_TMChllng", "_SctyElmt", "_POIChllng"]
	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != base_types.auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if type(value) != base_types.auto else self.make_default("TMChllng")

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = None

	@property
	def SctyElmt(self):
		return self._SctyElmt

	@SctyElmt.setter
	def SctyElmt(self, value):
		self._SctyElmt = value if type(value) != base_types.auto else self.make_default("SctyElmt")

	@SctyElmt.deleter
	def SctyElmt(self):
		del self._SctyElmt
		self._SctyElmt = None

	@property
	def POIChllng(self):
		return self._POIChllng

	@POIChllng.setter
	def POIChllng(self, value):
		self._POIChllng = value if type(value) != base_types.auto else self.make_default("POIChllng")

	@POIChllng.deleter
	def POIChllng(self):
		del self._POIChllng
		self._POIChllng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyElmt', type=CryptographicKey18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
	))

