from . import base_types
import ISODate
import Max140Text

class DueDate1(base_types._BaseFieldType):

	__slots__ = ["_DueDt", "_AddtlInf"]
	@property
	def DueDt(self):
		return self._DueDt

	@DueDt.setter
	def DueDt(self, value):
		self._DueDt = value if type(value) != auto else self.make_default("DueDt")

	@DueDt.deleter
	def DueDt(self):
		del self._DueDt
		self._DueDt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DueDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

