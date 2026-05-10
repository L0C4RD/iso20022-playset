from . import base_types
import BICIdentification1

class RequiredSubmission2(base_types._BaseFieldType):

	__slots__ = ["_Submitr"]
	@property
	def Submitr(self):
		return self._Submitr

	@Submitr.setter
	def Submitr(self, value):
		self._Submitr = value if type(value) != auto else self.make_default("Submitr")

	@Submitr.deleter
	def Submitr(self):
		del self._Submitr
		self._Submitr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Submitr', type=BICIdentification1, min=1, max=None, mutex_group=None, array=True),
	))

