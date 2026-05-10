import base_types
import ShortLong1Code
import FinancialInstrumentQuantity45Choice

class SignedQuantityFormat14(base_types._BaseFieldType):

	__slots__ = ["_ShrtLngPos", "_Qty"]
	@property
	def ShrtLngPos(self):
		return self._ShrtLngPos

	@ShrtLngPos.setter
	def ShrtLngPos(self, value):
		self._ShrtLngPos = value if type(value) != auto else self.make_default("ShrtLngPos")

	@ShrtLngPos.deleter
	def ShrtLngPos(self):
		del self._ShrtLngPos
		self._ShrtLngPos = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ShrtLngPos', type=ShortLong1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity45Choice, min=1, max=1, mutex_group=None, array=False),
	))

