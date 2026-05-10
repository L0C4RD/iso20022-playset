import base_types
import SubBalanceType12Choice
import SubBalanceQuantity8Choice
import Max140Text

class AdditionalBalanceInformation22(base_types._BaseFieldType):

	__slots__ = ["_SubBalAddtlDtls", "_SubBalTp", "_Qty"]
	@property
	def SubBalAddtlDtls(self):
		return self._SubBalAddtlDtls

	@SubBalAddtlDtls.setter
	def SubBalAddtlDtls(self, value):
		self._SubBalAddtlDtls = value if type(value) != auto else self.make_default("SubBalAddtlDtls")

	@SubBalAddtlDtls.deleter
	def SubBalAddtlDtls(self):
		del self._SubBalAddtlDtls
		self._SubBalAddtlDtls = None

	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if type(value) != auto else self.make_default("SubBalTp")

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = None

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
		base_types.FieldEntry(name='SubBalAddtlDtls', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType12Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity8Choice, min=1, max=1, mutex_group=None, array=False),
	))

