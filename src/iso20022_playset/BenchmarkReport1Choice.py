import base_types
import BenchmarkCancellation1
import BenchmarkUpdate1
import BenchmarkCreate1

class BenchmarkReport1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cret", "_Upd", "_Cxl"]
	@property
	def Cret(self):
		return self._Cret

	@Cret.setter
	def Cret(self, value):
		self._Cret = value if type(value) != auto else self.make_default("Cret")

	@Cret.deleter
	def Cret(self):
		del self._Cret
		self._Cret = None

	@property
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if type(value) != auto else self.make_default("Upd")

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = None

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cret', type=BenchmarkCreate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Upd', type=BenchmarkUpdate1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cxl', type=BenchmarkCancellation1, min=0, max=1, mutex_group=1, array=False),
	))

