import base_types
import NotAvailable1Code
import ISINOct2015Identifier

class SecurityIdentification26Choice(base_types._BaseFieldType):

	__slots__ = ["_Id", "_NotAvlbl"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def NotAvlbl(self):
		return self._NotAvlbl

	@NotAvlbl.setter
	def NotAvlbl(self, value):
		self._NotAvlbl = value if type(value) != auto else self.make_default("NotAvlbl")

	@NotAvlbl.deleter
	def NotAvlbl(self):
		del self._NotAvlbl
		self._NotAvlbl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotAvlbl', type=NotAvailable1Code, min=0, max=1, mutex_group=1, array=False),
	))

