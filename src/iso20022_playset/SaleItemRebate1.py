import base_types
import Product6
import Max35Text

class SaleItemRebate1(base_types._BaseFieldType):

	__slots__ = ["_SaleItm", "_RbtLabl"]
	@property
	def SaleItm(self):
		return self._SaleItm

	@SaleItm.setter
	def SaleItm(self, value):
		self._SaleItm = value if type(value) != auto else self.make_default("SaleItm")

	@SaleItm.deleter
	def SaleItm(self):
		del self._SaleItm
		self._SaleItm = None

	@property
	def RbtLabl(self):
		return self._RbtLabl

	@RbtLabl.setter
	def RbtLabl(self, value):
		self._RbtLabl = value if type(value) != auto else self.make_default("RbtLabl")

	@RbtLabl.deleter
	def RbtLabl(self):
		del self._RbtLabl
		self._RbtLabl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SaleItm', type=Product6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RbtLabl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

