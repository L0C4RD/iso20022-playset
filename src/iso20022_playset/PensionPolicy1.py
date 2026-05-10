from . import base_types
import Max35Text
import AdditionalInformation15

class PensionPolicy1(base_types._BaseFieldType):

	__slots__ = ["_Idr", "_AddtlInf", "_SubIdr"]
	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if type(value) != auto else self.make_default("Idr")

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = None

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
	def SubIdr(self):
		return self._SubIdr

	@SubIdr.setter
	def SubIdr(self, value):
		self._SubIdr = value if type(value) != auto else self.make_default("SubIdr")

	@SubIdr.deleter
	def SubIdr(self):
		del self._SubIdr
		self._SubIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

