import base_types
import Quantity10

class Consignment3(base_types._BaseFieldType):

	__slots__ = ["_TtlQty", "_TtlWght", "_TtlVol"]
	@property
	def TtlQty(self):
		return self._TtlQty

	@TtlQty.setter
	def TtlQty(self, value):
		self._TtlQty = value if type(value) != auto else self.make_default("TtlQty")

	@TtlQty.deleter
	def TtlQty(self):
		del self._TtlQty
		self._TtlQty = None

	@property
	def TtlWght(self):
		return self._TtlWght

	@TtlWght.setter
	def TtlWght(self, value):
		self._TtlWght = value if type(value) != auto else self.make_default("TtlWght")

	@TtlWght.deleter
	def TtlWght(self):
		del self._TtlWght
		self._TtlWght = None

	@property
	def TtlVol(self):
		return self._TtlVol

	@TtlVol.setter
	def TtlVol(self, value):
		self._TtlVol = value if type(value) != auto else self.make_default("TtlVol")

	@TtlVol.deleter
	def TtlVol(self):
		del self._TtlVol
		self._TtlVol = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlQty', type=Quantity10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlWght', type=Quantity10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVol', type=Quantity10, min=0, max=1, mutex_group=None, array=False),
	))

