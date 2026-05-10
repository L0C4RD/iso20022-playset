from . import base_types
from ._SubBalanceQuantity1Choice import SubBalanceQuantity1Choice
from ._SecuritiesBalanceType2Code import SecuritiesBalanceType2Code
from ._Extended350Code import Extended350Code

class AdditionalBalanceInformation2(base_types._BaseFieldType):

	__slots__ = ["_XtndedSubBalTp", "_Qty", "_SubBalTp"]
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
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if type(value) != base_types.auto else self.make_default("SubBalTp")

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = None

	@property
	def XtndedSubBalTp(self):
		return self._XtndedSubBalTp

	@XtndedSubBalTp.setter
	def XtndedSubBalTp(self, value):
		self._XtndedSubBalTp = value if type(value) != base_types.auto else self.make_default("XtndedSubBalTp")

	@XtndedSubBalTp.deleter
	def XtndedSubBalTp(self):
		del self._XtndedSubBalTp
		self._XtndedSubBalTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SecuritiesBalanceType2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedSubBalTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))

