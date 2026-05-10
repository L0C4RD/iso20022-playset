import base_types
import SecuritiesEntryType3Code
import SignedQuantityFormat14

class HoldingBalance13(base_types._BaseFieldType):

	__slots__ = ["_BalTp", "_Bal"]
	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if type(value) != auto else self.make_default("BalTp")

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTp', type=SecuritiesEntryType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat14, min=1, max=1, mutex_group=None, array=False),
	))

