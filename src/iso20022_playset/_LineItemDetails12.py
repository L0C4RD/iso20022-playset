# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import Max70Text
from . import PercentageTolerance1
from . import ProductCategory1Choice
from . import ProductCharacteristics1Choice
from . import ProductIdentifier2Choice
from . import Quantity9

class LineItemDetails12(base_types._BaseFieldType):

	__slots__ = ["_AccptdAmt", "_AccptdQty", "_LineItmId", "_OrdrdAmt", "_OrdrdQty", "_OutsdngAmt", "_OutsdngQty", "_PdctChrtcs", "_PdctCtgy", "_PdctIdr", "_PdctNm", "_PdgAmt", "_PdgQty", "_PricTlrnce", "_QtyTlrnce"]
	@property
	def AccptdAmt(self):
		return self._AccptdAmt

	@AccptdAmt.setter
	def AccptdAmt(self, value):
		self._AccptdAmt = value if value is not None else base_types.UninitialisedField(self, 'AccptdAmt', CurrencyAndAmount, False)

	@AccptdAmt.deleter
	def AccptdAmt(self):
		del self._AccptdAmt
		self._AccptdAmt = base_types.UninitialisedField(self, 'AccptdAmt', CurrencyAndAmount, False)

	@property
	def AccptdQty(self):
		return self._AccptdQty

	@AccptdQty.setter
	def AccptdQty(self, value):
		self._AccptdQty = value if value is not None else base_types.UninitialisedField(self, 'AccptdQty', Quantity9, False)

	@AccptdQty.deleter
	def AccptdQty(self):
		del self._AccptdQty
		self._AccptdQty = base_types.UninitialisedField(self, 'AccptdQty', Quantity9, False)

	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if value is not None else base_types.UninitialisedField(self, 'LineItmId', Max70Text, False)

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = base_types.UninitialisedField(self, 'LineItmId', Max70Text, False)

	@property
	def OrdrdAmt(self):
		return self._OrdrdAmt

	@OrdrdAmt.setter
	def OrdrdAmt(self, value):
		self._OrdrdAmt = value if value is not None else base_types.UninitialisedField(self, 'OrdrdAmt', CurrencyAndAmount, False)

	@OrdrdAmt.deleter
	def OrdrdAmt(self):
		del self._OrdrdAmt
		self._OrdrdAmt = base_types.UninitialisedField(self, 'OrdrdAmt', CurrencyAndAmount, False)

	@property
	def OrdrdQty(self):
		return self._OrdrdQty

	@OrdrdQty.setter
	def OrdrdQty(self, value):
		self._OrdrdQty = value if value is not None else base_types.UninitialisedField(self, 'OrdrdQty', Quantity9, False)

	@OrdrdQty.deleter
	def OrdrdQty(self):
		del self._OrdrdQty
		self._OrdrdQty = base_types.UninitialisedField(self, 'OrdrdQty', Quantity9, False)

	@property
	def OutsdngAmt(self):
		return self._OutsdngAmt

	@OutsdngAmt.setter
	def OutsdngAmt(self, value):
		self._OutsdngAmt = value if value is not None else base_types.UninitialisedField(self, 'OutsdngAmt', CurrencyAndAmount, False)

	@OutsdngAmt.deleter
	def OutsdngAmt(self):
		del self._OutsdngAmt
		self._OutsdngAmt = base_types.UninitialisedField(self, 'OutsdngAmt', CurrencyAndAmount, False)

	@property
	def OutsdngQty(self):
		return self._OutsdngQty

	@OutsdngQty.setter
	def OutsdngQty(self, value):
		self._OutsdngQty = value if value is not None else base_types.UninitialisedField(self, 'OutsdngQty', Quantity9, False)

	@OutsdngQty.deleter
	def OutsdngQty(self):
		del self._OutsdngQty
		self._OutsdngQty = base_types.UninitialisedField(self, 'OutsdngQty', Quantity9, False)

	@property
	def PdctChrtcs(self):
		return self._PdctChrtcs

	@PdctChrtcs.setter
	def PdctChrtcs(self, value):
		self._PdctChrtcs = value if value is not None else base_types.UninitialisedField(self, 'PdctChrtcs', ProductCharacteristics1Choice, True)

	@PdctChrtcs.deleter
	def PdctChrtcs(self):
		del self._PdctChrtcs
		self._PdctChrtcs = base_types.UninitialisedField(self, 'PdctChrtcs', ProductCharacteristics1Choice, True)

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if value is not None else base_types.UninitialisedField(self, 'PdctCtgy', ProductCategory1Choice, True)

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = base_types.UninitialisedField(self, 'PdctCtgy', ProductCategory1Choice, True)

	@property
	def PdctIdr(self):
		return self._PdctIdr

	@PdctIdr.setter
	def PdctIdr(self, value):
		self._PdctIdr = value if value is not None else base_types.UninitialisedField(self, 'PdctIdr', ProductIdentifier2Choice, True)

	@PdctIdr.deleter
	def PdctIdr(self):
		del self._PdctIdr
		self._PdctIdr = base_types.UninitialisedField(self, 'PdctIdr', ProductIdentifier2Choice, True)

	@property
	def PdctNm(self):
		return self._PdctNm

	@PdctNm.setter
	def PdctNm(self, value):
		self._PdctNm = value if value is not None else base_types.UninitialisedField(self, 'PdctNm', Max70Text, False)

	@PdctNm.deleter
	def PdctNm(self):
		del self._PdctNm
		self._PdctNm = base_types.UninitialisedField(self, 'PdctNm', Max70Text, False)

	@property
	def PdgAmt(self):
		return self._PdgAmt

	@PdgAmt.setter
	def PdgAmt(self, value):
		self._PdgAmt = value if value is not None else base_types.UninitialisedField(self, 'PdgAmt', CurrencyAndAmount, False)

	@PdgAmt.deleter
	def PdgAmt(self):
		del self._PdgAmt
		self._PdgAmt = base_types.UninitialisedField(self, 'PdgAmt', CurrencyAndAmount, False)

	@property
	def PdgQty(self):
		return self._PdgQty

	@PdgQty.setter
	def PdgQty(self, value):
		self._PdgQty = value if value is not None else base_types.UninitialisedField(self, 'PdgQty', Quantity9, False)

	@PdgQty.deleter
	def PdgQty(self):
		del self._PdgQty
		self._PdgQty = base_types.UninitialisedField(self, 'PdgQty', Quantity9, False)

	@property
	def PricTlrnce(self):
		return self._PricTlrnce

	@PricTlrnce.setter
	def PricTlrnce(self, value):
		self._PricTlrnce = value if value is not None else base_types.UninitialisedField(self, 'PricTlrnce', PercentageTolerance1, False)

	@PricTlrnce.deleter
	def PricTlrnce(self):
		del self._PricTlrnce
		self._PricTlrnce = base_types.UninitialisedField(self, 'PricTlrnce', PercentageTolerance1, False)

	@property
	def QtyTlrnce(self):
		return self._QtyTlrnce

	@QtyTlrnce.setter
	def QtyTlrnce(self, value):
		self._QtyTlrnce = value if value is not None else base_types.UninitialisedField(self, 'QtyTlrnce', PercentageTolerance1, False)

	@QtyTlrnce.deleter
	def QtyTlrnce(self):
		del self._QtyTlrnce
		self._QtyTlrnce = base_types.UninitialisedField(self, 'QtyTlrnce', PercentageTolerance1, False)

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