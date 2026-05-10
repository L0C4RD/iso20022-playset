import base_types
import Period1

class CorporateActionPeriod2(base_types._BaseFieldType):

	__slots__ = ["_PrvlgSspnsnPrd", "_RvcbltyPrd", "_ParllTradgPrd", "_AssntdLinePrd", "_PricClctnPrd", "_SellThruIssrPrd", "_ActnPrd"]
	@property
	def PrvlgSspnsnPrd(self):
		return self._PrvlgSspnsnPrd

	@PrvlgSspnsnPrd.setter
	def PrvlgSspnsnPrd(self, value):
		self._PrvlgSspnsnPrd = value if type(value) != auto else self.make_default("PrvlgSspnsnPrd")

	@PrvlgSspnsnPrd.deleter
	def PrvlgSspnsnPrd(self):
		del self._PrvlgSspnsnPrd
		self._PrvlgSspnsnPrd = None

	@property
	def RvcbltyPrd(self):
		return self._RvcbltyPrd

	@RvcbltyPrd.setter
	def RvcbltyPrd(self, value):
		self._RvcbltyPrd = value if type(value) != auto else self.make_default("RvcbltyPrd")

	@RvcbltyPrd.deleter
	def RvcbltyPrd(self):
		del self._RvcbltyPrd
		self._RvcbltyPrd = None

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
	def AssntdLinePrd(self):
		return self._AssntdLinePrd

	@AssntdLinePrd.setter
	def AssntdLinePrd(self, value):
		self._AssntdLinePrd = value if type(value) != auto else self.make_default("AssntdLinePrd")

	@AssntdLinePrd.deleter
	def AssntdLinePrd(self):
		del self._AssntdLinePrd
		self._AssntdLinePrd = None

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
	def SellThruIssrPrd(self):
		return self._SellThruIssrPrd

	@SellThruIssrPrd.setter
	def SellThruIssrPrd(self, value):
		self._SellThruIssrPrd = value if type(value) != auto else self.make_default("SellThruIssrPrd")

	@SellThruIssrPrd.deleter
	def SellThruIssrPrd(self):
		del self._SellThruIssrPrd
		self._SellThruIssrPrd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvlgSspnsnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParllTradgPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssntdLinePrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellThruIssrPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnPrd', type=Period1, min=0, max=1, mutex_group=None, array=False),
	))

