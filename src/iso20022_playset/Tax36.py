import base_types
import DateQuarter1Choice
import AdditionalInformation15

class Tax36(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_DtOrPrd"]
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

	@property
	def DtOrPrd(self):
		return self._DtOrPrd

	@DtOrPrd.setter
	def DtOrPrd(self, value):
		self._DtOrPrd = value if type(value) != auto else self.make_default("DtOrPrd")

	@DtOrPrd.deleter
	def DtOrPrd(self):
		del self._DtOrPrd
		self._DtOrPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtOrPrd', type=DateQuarter1Choice, min=1, max=1, mutex_group=None, array=False),
	))

