from . import base_types
import Schedule11
import AmountAndDirection106

class NotionalAmount5(base_types._BaseFieldType):

	__slots__ = ["_SchdlPrd", "_Amt"]
	@property
	def SchdlPrd(self):
		return self._SchdlPrd

	@SchdlPrd.setter
	def SchdlPrd(self, value):
		self._SchdlPrd = value if type(value) != auto else self.make_default("SchdlPrd")

	@SchdlPrd.deleter
	def SchdlPrd(self):
		del self._SchdlPrd
		self._SchdlPrd = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchdlPrd', type=Schedule11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
	))

