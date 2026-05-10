from . import base_types
import Max350Text
import PowerOfAttorneyLegalisation1Code
import DateFormat58Choice

class PowerOfAttorneyRequirements4(base_types._BaseFieldType):

	__slots__ = ["_OthrDcmnttn", "_DocSubmissnDdln", "_LglRqrmnt"]
	@property
	def OthrDcmnttn(self):
		return self._OthrDcmnttn

	@OthrDcmnttn.setter
	def OthrDcmnttn(self, value):
		self._OthrDcmnttn = value if type(value) != auto else self.make_default("OthrDcmnttn")

	@OthrDcmnttn.deleter
	def OthrDcmnttn(self):
		del self._OthrDcmnttn
		self._OthrDcmnttn = None

	@property
	def DocSubmissnDdln(self):
		return self._DocSubmissnDdln

	@DocSubmissnDdln.setter
	def DocSubmissnDdln(self, value):
		self._DocSubmissnDdln = value if type(value) != auto else self.make_default("DocSubmissnDdln")

	@DocSubmissnDdln.deleter
	def DocSubmissnDdln(self):
		del self._DocSubmissnDdln
		self._DocSubmissnDdln = None

	@property
	def LglRqrmnt(self):
		return self._LglRqrmnt

	@LglRqrmnt.setter
	def LglRqrmnt(self, value):
		self._LglRqrmnt = value if type(value) != auto else self.make_default("LglRqrmnt")

	@LglRqrmnt.deleter
	def LglRqrmnt(self):
		del self._LglRqrmnt
		self._LglRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrDcmnttn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocSubmissnDdln', type=DateFormat58Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRqrmnt', type=PowerOfAttorneyLegalisation1Code, min=0, max=4, mutex_group=None, array=True),
	))

