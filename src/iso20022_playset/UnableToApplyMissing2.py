import base_types
import MissingData1Choice
import Max140Text

class UnableToApplyMissing2(base_types._BaseFieldType):

	__slots__ = ["_AddtlMssngInf", "_Tp"]
	@property
	def AddtlMssngInf(self):
		return self._AddtlMssngInf

	@AddtlMssngInf.setter
	def AddtlMssngInf(self, value):
		self._AddtlMssngInf = value if type(value) != auto else self.make_default("AddtlMssngInf")

	@AddtlMssngInf.deleter
	def AddtlMssngInf(self):
		del self._AddtlMssngInf
		self._AddtlMssngInf = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlMssngInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MissingData1Choice, min=1, max=1, mutex_group=None, array=False),
	))

