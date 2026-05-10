import base_types
import Amount17
import Number

class SettlementCategoryTotal2(base_types._BaseFieldType):

	__slots__ = ["_PrcgFee", "_IntrchngFee", "_Amt", "_Cnt"]
	@property
	def PrcgFee(self):
		return self._PrcgFee

	@PrcgFee.setter
	def PrcgFee(self, value):
		self._PrcgFee = value if type(value) != auto else self.make_default("PrcgFee")

	@PrcgFee.deleter
	def PrcgFee(self):
		del self._PrcgFee
		self._PrcgFee = None

	@property
	def IntrchngFee(self):
		return self._IntrchngFee

	@IntrchngFee.setter
	def IntrchngFee(self, value):
		self._IntrchngFee = value if type(value) != auto else self.make_default("IntrchngFee")

	@IntrchngFee.deleter
	def IntrchngFee(self):
		del self._IntrchngFee
		self._IntrchngFee = None

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

	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if type(value) != auto else self.make_default("Cnt")

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgFee', type=Amount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFee', type=Amount17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=Amount17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

