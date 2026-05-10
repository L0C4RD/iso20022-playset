from . import base_types
from .Period11 import Period11

class CorporateActionPeriod13(base_types._BaseFieldType):

	__slots__ = ["_ParllTradgPrd", "_ActnPrd", "_PricClctnPrd"]
	@property
	def ParllTradgPrd(self):
		return self._ParllTradgPrd

	@ParllTradgPrd.setter
	def ParllTradgPrd(self, value):
		self._ParllTradgPrd = value if type(value) != auto else self.make_default("ParllTradgPrd")

	@ParllTradgPrd.deleter
	def ParllTradgPrd(self):
		del self._ParllTradgPrd
		self._ParllTradgPrd = None

	@property
	def ActnPrd(self):
		return self._ActnPrd

	@ActnPrd.setter
	def ActnPrd(self, value):
		self._ActnPrd = value if type(value) != auto else self.make_default("ActnPrd")

	@ActnPrd.deleter
	def ActnPrd(self):
		del self._ActnPrd
		self._ActnPrd = None

	@property
	def PricClctnPrd(self):
		return self._PricClctnPrd

	@PricClctnPrd.setter
	def PricClctnPrd(self, value):
		self._PricClctnPrd = value if type(value) != auto else self.make_default("PricClctnPrd")

	@PricClctnPrd.deleter
	def PricClctnPrd(self):
		del self._PricClctnPrd
		self._PricClctnPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ParllTradgPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
	))

