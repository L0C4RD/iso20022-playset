import base_types
import Period1

class CorporateActionPeriod1(base_types._BaseFieldType):

	__slots__ = ["_ActnPrd", "_BlckgPrd", "_CmplsryPurchsPrd", "_PricClctnPrd", "_IntrstPrd"]
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
	def BlckgPrd(self):
		return self._BlckgPrd

	@BlckgPrd.setter
	def BlckgPrd(self, value):
		self._BlckgPrd = value if type(value) != auto else self.make_default("BlckgPrd")

	@BlckgPrd.deleter
	def BlckgPrd(self):
		del self._BlckgPrd
		self._BlckgPrd = None

	@property
	def CmplsryPurchsPrd(self):
		return self._CmplsryPurchsPrd

	@CmplsryPurchsPrd.setter
	def CmplsryPurchsPrd(self, value):
		self._CmplsryPurchsPrd = value if type(value) != auto else self.make_default("CmplsryPurchsPrd")

	@CmplsryPurchsPrd.deleter
	def CmplsryPurchsPrd(self):
		del self._CmplsryPurchsPrd
		self._CmplsryPurchsPrd = None

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

	@property
	def IntrstPrd(self):
		return self._IntrstPrd

	@IntrstPrd.setter
	def IntrstPrd(self, value):
		self._IntrstPrd = value if type(value) != auto else self.make_default("IntrstPrd")

	@IntrstPrd.deleter
	def IntrstPrd(self):
		del self._IntrstPrd
		self._IntrstPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlckgPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmplsryPurchsPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
	))

