from . import base_types
import CommissionType5Choice
import AmountOrRate3Choice

class Commission21(base_types._BaseFieldType):

	__slots__ = ["_ComssnApld", "_ComssnTp"]
	@property
	def ComssnApld(self):
		return self._ComssnApld

	@ComssnApld.setter
	def ComssnApld(self, value):
		self._ComssnApld = value if type(value) != auto else self.make_default("ComssnApld")

	@ComssnApld.deleter
	def ComssnApld(self):
		del self._ComssnApld
		self._ComssnApld = None

	@property
	def ComssnTp(self):
		return self._ComssnTp

	@ComssnTp.setter
	def ComssnTp(self, value):
		self._ComssnTp = value if type(value) != auto else self.make_default("ComssnTp")

	@ComssnTp.deleter
	def ComssnTp(self):
		del self._ComssnTp
		self._ComssnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComssnApld', type=AmountOrRate3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComssnTp', type=CommissionType5Choice, min=1, max=1, mutex_group=None, array=False),
	))

