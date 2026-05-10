from . import base_types
from ._CurrencyAndAmount import CurrencyAndAmount
from ._ProductCharacteristics1Choice import ProductCharacteristics1Choice
from ._ProductIdentifier2Choice import ProductIdentifier2Choice
from ._ProductCategory1Choice import ProductCategory1Choice
from ._Max70Text import Max70Text
from ._PercentageTolerance1 import PercentageTolerance1
from ._Quantity9 import Quantity9

class LineItemDetails12(base_types._BaseFieldType):

	__slots__ = ["_PdgQty", "_PdctNm", "_AccptdAmt", "_OutsdngAmt", "_OutsdngQty", "_OrdrdAmt", "_AccptdQty", "_QtyTlrnce", "_PricTlrnce", "_PdctChrtcs", "_OrdrdQty", "_PdctCtgy", "_PdgAmt", "_LineItmId", "_PdctIdr"]
	@property
	def AccptdAmt(self):
		return self._AccptdAmt

	@AccptdAmt.setter
	def AccptdAmt(self, value):
		self._AccptdAmt = value if type(value) != base_types.auto else self.make_default("AccptdAmt")

	@AccptdAmt.deleter
	def AccptdAmt(self):
		del self._AccptdAmt
		self._AccptdAmt = None

	@property
	def AccptdQty(self):
		return self._AccptdQty

	@AccptdQty.setter
	def AccptdQty(self, value):
		self._AccptdQty = value if type(value) != base_types.auto else self.make_default("AccptdQty")

	@AccptdQty.deleter
	def AccptdQty(self):
		del self._AccptdQty
		self._AccptdQty = None

	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if type(value) != base_types.auto else self.make_default("LineItmId")

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = None

	@property
	def OrdrdAmt(self):
		return self._OrdrdAmt

	@OrdrdAmt.setter
	def OrdrdAmt(self, value):
		self._OrdrdAmt = value if type(value) != base_types.auto else self.make_default("OrdrdAmt")

	@OrdrdAmt.deleter
	def OrdrdAmt(self):
		del self._OrdrdAmt
		self._OrdrdAmt = None

	@property
	def OrdrdQty(self):
		return self._OrdrdQty

	@OrdrdQty.setter
	def OrdrdQty(self, value):
		self._OrdrdQty = value if type(value) != base_types.auto else self.make_default("OrdrdQty")

	@OrdrdQty.deleter
	def OrdrdQty(self):
		del self._OrdrdQty
		self._OrdrdQty = None

	@property
	def OutsdngAmt(self):
		return self._OutsdngAmt

	@OutsdngAmt.setter
	def OutsdngAmt(self, value):
		self._OutsdngAmt = value if type(value) != base_types.auto else self.make_default("OutsdngAmt")

	@OutsdngAmt.deleter
	def OutsdngAmt(self):
		del self._OutsdngAmt
		self._OutsdngAmt = None

	@property
	def OutsdngQty(self):
		return self._OutsdngQty

	@OutsdngQty.setter
	def OutsdngQty(self, value):
		self._OutsdngQty = value if type(value) != base_types.auto else self.make_default("OutsdngQty")

	@OutsdngQty.deleter
	def OutsdngQty(self):
		del self._OutsdngQty
		self._OutsdngQty = None

	@property
	def PdctChrtcs(self):
		return self._PdctChrtcs

	@PdctChrtcs.setter
	def PdctChrtcs(self, value):
		self._PdctChrtcs = value if type(value) != base_types.auto else self.make_default("PdctChrtcs")

	@PdctChrtcs.deleter
	def PdctChrtcs(self):
		del self._PdctChrtcs
		self._PdctChrtcs = None

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if type(value) != base_types.auto else self.make_default("PdctCtgy")

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = None

	@property
	def PdctIdr(self):
		return self._PdctIdr

	@PdctIdr.setter
	def PdctIdr(self, value):
		self._PdctIdr = value if type(value) != base_types.auto else self.make_default("PdctIdr")

	@PdctIdr.deleter
	def PdctIdr(self):
		del self._PdctIdr
		self._PdctIdr = None

	@property
	def PdctNm(self):
		return self._PdctNm

	@PdctNm.setter
	def PdctNm(self, value):
		self._PdctNm = value if type(value) != base_types.auto else self.make_default("PdctNm")

	@PdctNm.deleter
	def PdctNm(self):
		del self._PdctNm
		self._PdctNm = None

	@property
	def PdgAmt(self):
		return self._PdgAmt

	@PdgAmt.setter
	def PdgAmt(self, value):
		self._PdgAmt = value if type(value) != base_types.auto else self.make_default("PdgAmt")

	@PdgAmt.deleter
	def PdgAmt(self):
		del self._PdgAmt
		self._PdgAmt = None

	@property
	def PdgQty(self):
		return self._PdgQty

	@PdgQty.setter
	def PdgQty(self, value):
		self._PdgQty = value if type(value) != base_types.auto else self.make_default("PdgQty")

	@PdgQty.deleter
	def PdgQty(self):
		del self._PdgQty
		self._PdgQty = None

	@property
	def PricTlrnce(self):
		return self._PricTlrnce

	@PricTlrnce.setter
	def PricTlrnce(self, value):
		self._PricTlrnce = value if type(value) != base_types.auto else self.make_default("PricTlrnce")

	@PricTlrnce.deleter
	def PricTlrnce(self):
		del self._PricTlrnce
		self._PricTlrnce = None

	@property
	def QtyTlrnce(self):
		return self._QtyTlrnce

	@QtyTlrnce.setter
	def QtyTlrnce(self, value):
		self._QtyTlrnce = value if type(value) != base_types.auto else self.make_default("QtyTlrnce")

	@QtyTlrnce.deleter
	def QtyTlrnce(self):
		del self._QtyTlrnce
		self._QtyTlrnce = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdQty', type=Quantity9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrdAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrdQty', type=Quantity9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngQty', type=Quantity9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctChrtcs', type=ProductCharacteristics1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctCtgy', type=ProductCategory1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctIdr', type=ProductIdentifier2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgQty', type=Quantity9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTlrnce', type=PercentageTolerance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyTlrnce', type=PercentageTolerance1, min=0, max=1, mutex_group=None, array=False),
	))

