from . import base_types
from ._Quantity9 import Quantity9
from ._YesNoIndicator import YesNoIndicator
from ._Max70Text import Max70Text
from ._CountryCode import CountryCode

class CertifiedCharacteristics2Choice(base_types._BaseFieldType):

	__slots__ = ["_HlthIndctn", "_Wght", "_Qty", "_Qlty", "_Anlys", "_PhytosntryIndctn", "_Orgn"]
	@property
	def HlthIndctn(self):
		return self._HlthIndctn

	@HlthIndctn.setter
	def HlthIndctn(self, value):
		self._HlthIndctn = value if type(value) != base_types.auto else self.make_default("HlthIndctn")

	@HlthIndctn.deleter
	def HlthIndctn(self):
		del self._HlthIndctn
		self._HlthIndctn = None

	@property
	def Wght(self):
		return self._Wght

	@Wght.setter
	def Wght(self, value):
		self._Wght = value if type(value) != base_types.auto else self.make_default("Wght")

	@Wght.deleter
	def Wght(self):
		del self._Wght
		self._Wght = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def Qlty(self):
		return self._Qlty

	@Qlty.setter
	def Qlty(self, value):
		self._Qlty = value if type(value) != base_types.auto else self.make_default("Qlty")

	@Qlty.deleter
	def Qlty(self):
		del self._Qlty
		self._Qlty = None

	@property
	def Anlys(self):
		return self._Anlys

	@Anlys.setter
	def Anlys(self, value):
		self._Anlys = value if type(value) != base_types.auto else self.make_default("Anlys")

	@Anlys.deleter
	def Anlys(self):
		del self._Anlys
		self._Anlys = None

	@property
	def PhytosntryIndctn(self):
		return self._PhytosntryIndctn

	@PhytosntryIndctn.setter
	def PhytosntryIndctn(self, value):
		self._PhytosntryIndctn = value if type(value) != base_types.auto else self.make_default("PhytosntryIndctn")

	@PhytosntryIndctn.deleter
	def PhytosntryIndctn(self):
		del self._PhytosntryIndctn
		self._PhytosntryIndctn = None

	@property
	def Orgn(self):
		return self._Orgn

	@Orgn.setter
	def Orgn(self, value):
		self._Orgn = value if type(value) != base_types.auto else self.make_default("Orgn")

	@Orgn.deleter
	def Orgn(self):
		del self._Orgn
		self._Orgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HlthIndctn', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wght', type=Quantity9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qlty', type=Max70Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Anlys', type=Max70Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PhytosntryIndctn', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Orgn', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
	))

