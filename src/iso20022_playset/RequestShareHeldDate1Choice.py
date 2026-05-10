from . import base_types
import Max350Text
import DateCalculationMethod1Code

class RequestShareHeldDate1Choice(base_types._BaseFieldType):

	__slots__ = ["_DtClctnMtd", "_DtClctnDesc"]
	@property
	def DtClctnMtd(self):
		return self._DtClctnMtd

	@DtClctnMtd.setter
	def DtClctnMtd(self, value):
		self._DtClctnMtd = value if type(value) != auto else self.make_default("DtClctnMtd")

	@DtClctnMtd.deleter
	def DtClctnMtd(self):
		del self._DtClctnMtd
		self._DtClctnMtd = None

	@property
	def DtClctnDesc(self):
		return self._DtClctnDesc

	@DtClctnDesc.setter
	def DtClctnDesc(self, value):
		self._DtClctnDesc = value if type(value) != auto else self.make_default("DtClctnDesc")

	@DtClctnDesc.deleter
	def DtClctnDesc(self):
		del self._DtClctnDesc
		self._DtClctnDesc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtClctnMtd', type=DateCalculationMethod1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtClctnDesc', type=Max350Text, min=0, max=1, mutex_group=1, array=False),
	))

