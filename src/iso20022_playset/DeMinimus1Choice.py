from . import base_types
import DeMinimusApplicable1
import DeMinimusNotApplicable1

class DeMinimus1Choice(base_types._BaseFieldType):

	__slots__ = ["_DeMnmsAplbl", "_DeMnmsNotAplbl"]
	@property
	def DeMnmsAplbl(self):
		return self._DeMnmsAplbl

	@DeMnmsAplbl.setter
	def DeMnmsAplbl(self, value):
		self._DeMnmsAplbl = value if type(value) != auto else self.make_default("DeMnmsAplbl")

	@DeMnmsAplbl.deleter
	def DeMnmsAplbl(self):
		del self._DeMnmsAplbl
		self._DeMnmsAplbl = None

	@property
	def DeMnmsNotAplbl(self):
		return self._DeMnmsNotAplbl

	@DeMnmsNotAplbl.setter
	def DeMnmsNotAplbl(self, value):
		self._DeMnmsNotAplbl = value if type(value) != auto else self.make_default("DeMnmsNotAplbl")

	@DeMnmsNotAplbl.deleter
	def DeMnmsNotAplbl(self):
		del self._DeMnmsNotAplbl
		self._DeMnmsNotAplbl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DeMnmsAplbl', type=DeMinimusApplicable1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DeMnmsNotAplbl', type=DeMinimusNotApplicable1, min=0, max=1, mutex_group=1, array=False),
	))

