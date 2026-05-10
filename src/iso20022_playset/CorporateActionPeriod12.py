import base_types
import Period6Choice

class CorporateActionPeriod12(base_types._BaseFieldType):

	__slots__ = ["_DpstrySspnsnPrdForWdrwl", "_ActnPrd", "_ParllTradgPrd", "_PrvlgSspnsnPrd", "_PricClctnPrd", "_AcctSvcrRvcbltyPrd", "_RvcbltyPrd"]
	@property
	def DpstrySspnsnPrdForWdrwl(self):
		return self._DpstrySspnsnPrdForWdrwl

	@DpstrySspnsnPrdForWdrwl.setter
	def DpstrySspnsnPrdForWdrwl(self, value):
		self._DpstrySspnsnPrdForWdrwl = value if type(value) != auto else self.make_default("DpstrySspnsnPrdForWdrwl")

	@DpstrySspnsnPrdForWdrwl.deleter
	def DpstrySspnsnPrdForWdrwl(self):
		del self._DpstrySspnsnPrdForWdrwl
		self._DpstrySspnsnPrdForWdrwl = None

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
	def AcctSvcrRvcbltyPrd(self):
		return self._AcctSvcrRvcbltyPrd

	@AcctSvcrRvcbltyPrd.setter
	def AcctSvcrRvcbltyPrd(self, value):
		self._AcctSvcrRvcbltyPrd = value if type(value) != auto else self.make_default("AcctSvcrRvcbltyPrd")

	@AcctSvcrRvcbltyPrd.deleter
	def AcctSvcrRvcbltyPrd(self):
		del self._AcctSvcrRvcbltyPrd
		self._AcctSvcrRvcbltyPrd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DpstrySspnsnPrdForWdrwl', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ParllTradgPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvlgSspnsnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricClctnPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrRvcbltyPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvcbltyPrd', type=Period6Choice, min=0, max=1, mutex_group=None, array=False),
	))

