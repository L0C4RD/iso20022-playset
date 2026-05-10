from . import base_types
import BICIdentifier

class BICIdentification1(base_types._BaseFieldType):

	__slots__ = ["_BIC"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

