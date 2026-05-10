from . import base_types
import AdditionalReference10

class References64Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrRef", "_RltdRef"]
	@property
	def OthrRef(self):
		return self._OthrRef

	@OthrRef.setter
	def OthrRef(self, value):
		self._OthrRef = value if type(value) != auto else self.make_default("OthrRef")

	@OthrRef.deleter
	def OthrRef(self):
		del self._OthrRef
		self._OthrRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRef', type=AdditionalReference10, min=1, max=2, mutex_group=1, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=1, max=2, mutex_group=1, array=False),
	))

