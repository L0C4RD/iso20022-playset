from . import base_types
from ._Amount1Choice import Amount1Choice
from ._Max2000Text import Max2000Text

class UndertakingAmount2(base_types._BaseFieldType):

	__slots__ = ["_AmtChc", "_AddtlInf"]
	@property
	def AmtChc(self):
		return self._AmtChc

	@AmtChc.setter
	def AmtChc(self, value):
		self._AmtChc = value if type(value) != base_types.auto else self.make_default("AmtChc")

	@AmtChc.deleter
	def AmtChc(self):
		del self._AmtChc
		self._AmtChc = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtChc', type=Amount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

