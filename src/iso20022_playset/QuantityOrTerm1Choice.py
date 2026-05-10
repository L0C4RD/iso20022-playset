import base_types
import Schedule10
import QuantityTerm1

class QuantityOrTerm1Choice(base_types._BaseFieldType):

	__slots__ = ["_Term", "_SchdlPrd"]
	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if type(value) != auto else self.make_default("Term")

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = None

	@property
	def SchdlPrd(self):
		return self._SchdlPrd

	@SchdlPrd.setter
	def SchdlPrd(self, value):
		self._SchdlPrd = value if type(value) != auto else self.make_default("SchdlPrd")

	@SchdlPrd.deleter
	def SchdlPrd(self):
		del self._SchdlPrd
		self._SchdlPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Term', type=QuantityTerm1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SchdlPrd', type=Schedule10, min=1, max=None, mutex_group=1, array=True),
	))

