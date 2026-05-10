import base_types
import ActiveCurrencyAndAmount

class MarginRequirement1(base_types._BaseFieldType):

	__slots__ = ["_RtrMrgnAmt", "_DlvrMrgnAmt"]
	@property
	def RtrMrgnAmt(self):
		return self._RtrMrgnAmt

	@RtrMrgnAmt.setter
	def RtrMrgnAmt(self, value):
		self._RtrMrgnAmt = value if type(value) != auto else self.make_default("RtrMrgnAmt")

	@RtrMrgnAmt.deleter
	def RtrMrgnAmt(self):
		del self._RtrMrgnAmt
		self._RtrMrgnAmt = None

	@property
	def DlvrMrgnAmt(self):
		return self._DlvrMrgnAmt

	@DlvrMrgnAmt.setter
	def DlvrMrgnAmt(self, value):
		self._DlvrMrgnAmt = value if type(value) != auto else self.make_default("DlvrMrgnAmt")

	@DlvrMrgnAmt.deleter
	def DlvrMrgnAmt(self):
		del self._DlvrMrgnAmt
		self._DlvrMrgnAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RtrMrgnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrMrgnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

