import base_types
import AmountAndDirection102
import ActiveCurrencyAndAmount

class EndOfDayRequirement1(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnRqrmnt", "_VartnMrgnRqrmnt"]
	@property
	def InitlMrgnRqrmnt(self):
		return self._InitlMrgnRqrmnt

	@InitlMrgnRqrmnt.setter
	def InitlMrgnRqrmnt(self, value):
		self._InitlMrgnRqrmnt = value if type(value) != auto else self.make_default("InitlMrgnRqrmnt")

	@InitlMrgnRqrmnt.deleter
	def InitlMrgnRqrmnt(self):
		del self._InitlMrgnRqrmnt
		self._InitlMrgnRqrmnt = None

	@property
	def VartnMrgnRqrmnt(self):
		return self._VartnMrgnRqrmnt

	@VartnMrgnRqrmnt.setter
	def VartnMrgnRqrmnt(self, value):
		self._VartnMrgnRqrmnt = value if type(value) != auto else self.make_default("VartnMrgnRqrmnt")

	@VartnMrgnRqrmnt.deleter
	def VartnMrgnRqrmnt(self):
		del self._VartnMrgnRqrmnt
		self._VartnMrgnRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnRqrmnt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRqrmnt', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
	))

